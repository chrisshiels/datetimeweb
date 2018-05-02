# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile time.go
	go build -ldflags "-X main.version=$(VERSION)" time.go
	chmod 755 time
	docker build -t datetimeweb/time:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7002:7002 datetimeweb/time:$(VERSION)
