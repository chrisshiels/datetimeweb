# 'Makefile'.
# Chris Shiels.


VERSION = latest


build:	Dockerfile web.go
	go build -ldflags "-X main.version=$(VERSION)" web.go
	docker build -t cs/web:$(VERSION) .


run:	build
	docker run --rm -i -t -p 7000:7000 cs/web:$(VERSION)
