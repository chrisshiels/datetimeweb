# 'Dockerfile'.
# Chris Shiels.


from alpine:latest

expose 7001

env PORT=7001

# Note that date has been built for glibc but Alpine uses musl libc.
run mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

cmd exec /date -p $PORT

copy date /
