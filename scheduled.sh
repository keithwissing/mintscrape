#!/bin/bash

date

if [[ z$1 != z-n ]]; then
    docker build -f Dockerfile -t mintscrape .
fi

docker run -d --rm --name mintscrape \
    -v /etc/localtime:/etc/localtime:ro \
    -v /data/mintscrape:/data mintscrape

