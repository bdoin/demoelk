# stdbuf is used to force the pipes to be line buffered
arecord -D hw:1 -c 2 -d 10000 -f S16_LE -vvv /dev/null 2>&1 | stdbuf -oL -eL grep '%' | stdbuf -oL -eL awk -v quote="'" '{ sub(/%/, "", $7); printf "{\"volume\":%s , \"@timestamp\":\"%s\"}\n", $7, strftime("%FT%T,0+0200",systime());  }' | stdbuf -oL -eL parallel --no-notice curl -s -XPOST 'localhost:9200/record/volume' -d {} > /dev/null
