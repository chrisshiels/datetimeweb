# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile web.go
	go build -ldflags "-X main.version=$(VERSION)" web.go
	chmod 755 web
	docker build -t datetimeweb/web:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7000:7000 datetimeweb/web:$(VERSION)
