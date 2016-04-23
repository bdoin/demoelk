#!/bin/bash

echo 'Create index /adl'
curl -XPUT 'http://localhost:9200/adl/'; echo
echo 'Create mapping in /adl/all'
curl -XPUT 'http://localhost:9200/adl/_mapping/all' -d '{
  "properties" : {
    "coordinates" : {
      "type" : "geo_point"
    }
  }
}'; echo
