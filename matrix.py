from elastalert.alerts import Alerter, BasicMatchString

import requests
import time
import json

class MatrixAlerter(Alerter):
    required_options = set(['server','room','api_token'])

    # Alert is called
    def alert(self, matches):

        # Matches is a list of match dictionaries.
        # It contains more than one match when the alert has
        # the aggregation option set
        for match in matches:

            url = 'https://{0}/_matrix/client/r0/rooms/{1}/send/m.room.message/{2}?access_token={3}'.format(self.rule['server'],\
			self.rule['room'], time.time(), self.rule['api_token'])

            # basic_match_string will transform the match into the default
            # human readable string format
            match_string = str(BasicMatchString(self.rule, match))

            jsonMessage={
	        "msgtype": "m.text",
		"format": "org.matrix.custom.html",
		"body": match_string,
		"formatted_body": match_string,
	    }

            headers = {b"Content-Type": b"application/json"}
		
            r = requests.put(url , data=json.dumps(jsonMessage), headers=headers)
            r.raise_for_status()

    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'Matrix Alerter',
                'server': self.rule['server'],
                'room': self.rule['room']}
