#!/bin/bash

date

if [[ z$1 != z-n ]]; then
    docker build -f Dockerfile -t mintscrape .
fi

docker run -d --rm --name mintscrape \
    --env-file .env \
    -v /etc/localtime:/etc/localtime:ro \
    -v /data/mintscrape:/data \
    kwissing/mintscrape

