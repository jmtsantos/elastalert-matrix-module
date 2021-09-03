# elastalert-matrix-module

A module for [elastalert](https://github.com/Yelp/elastalert) to send alert notifications directly to a Matrix server.

## Usage

As per elastalert documentation, just copy this repo to your `elastalert_modules` folder and for each rule set the required configurations. 


```
name: cpu usage
index: metricbeat-*
type: metric_aggregation

metric_agg_key: system.cpu.total.pct
metric_agg_type: max
query_key: host.name
ignore_null: true

buffer_time:
  minutes: 20
bucket_interval:
  minutes: 10
 
max_threshold: 2

filter:
- query:
    query_string:
      query: "metricset.name: cpu"

alert_text: "<h3>metricbeat - {0} - CPU usage</h3><pre>"
alert_text_type: aggregation_summary_only
alert_text_args: 
  - host.name
  - system.cpu.total.pct

alert: "elastalert_modules.matrix.MatrixAlerter"
server: "matrix.myserver.tld"
room: "<roomID>:myserver.tld"
api_token: "<api token>"
```