# 'Dockerfile'.
# Chris Shiels.


from alpine:latest

expose 7002

env PORT=7002

# Note that time has been built for glibc but Alpine uses musl libc.
run mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

cmd exec /time -p $PORT

copy time /
