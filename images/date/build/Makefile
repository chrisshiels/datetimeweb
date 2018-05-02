# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile date.go
	go build -ldflags "-X main.version=$(VERSION)" date.go
	chmod 755 date
	docker build -t datetimeweb/date:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7001:7001 datetimeweb/date:$(VERSION)
