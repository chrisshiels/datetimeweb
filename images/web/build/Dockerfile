# 'Dockerfile'.
# Chris Shiels.


from alpine:latest

expose 7000

env PORT=7000
env DATEENDPOINT=date
env TIMEENDPOINT=time

# Note that web has been built for glibc but Alpine uses musl libc.
run mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

cmd exec /web -p $PORT -dateendpoint $DATEENDPOINT -timeendpoint $TIMEENDPOINT

copy web /
