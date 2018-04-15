# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile date.go
	go build -ldflags "-X main.version=$(VERSION)" date.go
	docker build -t cs/date:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7001:7001 cs/date:$(VERSION)
