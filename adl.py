#!/usr/bin/python3
#
# This script get the agenda du libre json page and makes a new json
# format more suitable for an Elasticsearch document
#
# http://www.agendadulibre.org/maps.json?region=all
# ./adl.py| curl -s -XPOST localhost:9200/adl/all/_bulk --data-binary "@-"; echo
#
import json
import requests

req = requests.get('http://www.agendadulibre.org/maps.json?region=all',
                      headers = {'Accept' : 'application/json'})

adl = json.loads(req.text)

bulk = ""
for event in adl:
    bulk += json.dumps({'index': { '_id': event['properties']['id'] } }) + '\n'
    event2 = event['properties']
    del event2['id']
    event2['coordinates'] = event['geometry']['coordinates']
    bulk += json.dumps(event2) + '\n'

print(bulk)
