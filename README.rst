==========================================
Présentation Elasticsearch Logstash Kibana
==========================================

Objectif
========

L'objectif de cette présentation est de faire découvrir rapidement les
grands concepts derrière les outils `Elasticsearch
<https://www.elastic.co/products/elasticsearch>`_ `Logstash
<https://www.elastic.co/products/logstash>`_ `Kibana
<https://www.elastic.co/products/kibana>`_

Comment ça marche
=================

La présentation utilise `reavel.js
<http://lab.hakim.se/reveal-js/#/>`_. Pour la visualiser : ::

  git clone git@github.com:bdoin/demoelk.git
  cd demoelk
  git submodule update --init revealjs
  firefox demoelk.html

Démo applaudimètre
==================

Le script *applaudimetre.sh* écoute le micro de votre PC avec
*arecord*. Vérifions d'abbord que la commande suivante fonctionne bien
chez vous : ::

  arecord -D hw:1 -c 2 -d 10000 -f S16_LE -vvv /dev/null 2>&1

Vous devriez voir des lignes défiler avec le niveau sonore en pourcent
comme cela : ::

  Pic max. (8192 échantillons): 0x00001423 ####                 15%

Si ça marche, lancer l'applaudimètre avec : ::

  ./applaudimetre.sh

Dans Kibana, créer une visualisation sur le champs *volume* de l'index
type record/volume.

Démo agenda du libre
====================

Dans cette démonstration, on récupère le flux json des prochains
événements de l'agenda du libre et nous les affichons sur une carte
dans Kibana.

Il nous faut d'abbord créer un mapping pour Elasticsearch car sinon il
ne sait pas détecter que nous avons un *geo_point* : ::

  ./adl_mapping.sh

Ensuite on peut importer les données de l'agenda du libre et les
sauver dans Elasticsearch avec : ::

  ./adl.py | curl -s -XPOST localhost:9200/adl/all/_bulk --data-binary "@-"; echo

Dans Kibana, faire une visualisation de type *tyle map* sur le champs
*coordinates*.
