#!/bin/bash

if [[ z$1 != z-n ]]; then
    # docker build --no-cache -f Dockerfile -t mintscrape .
    docker build -f Dockerfile -t mintscrape .
fi

docker run -it --rm --name mintscrape \
    -v /etc/localtime:/etc/localtime:ro \
    -v /data/mintscrape:/data mintscrape

