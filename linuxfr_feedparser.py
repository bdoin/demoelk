#!/usr/bin/python3

import elasticsearch
import feedparser

es=elasticsearch.Elasticsearch('http://localhost:9200')
data=feedparser.parse('http://linuxfr.org/news.atom')
for news in data.entries:
   print(es.index(index='linuxfr',doc_type='news',body=news))
