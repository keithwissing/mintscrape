none:

build:
	docker build -f Dockerfile -t mintscrape .

build-no-cache:
	docker build --no-cache -f Dockerfile -t mintscrape .

test-run:
	docker run -it --rm --env-file=.env mintscrape

