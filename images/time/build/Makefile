# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile time.go
	go build -ldflags "-X main.version=$(VERSION)" time.go
	docker build -t cs/time:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7002:7002 cs/time:$(VERSION)
