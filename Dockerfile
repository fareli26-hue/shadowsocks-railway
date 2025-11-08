FROM ghcr.io/shadowsocks/shadowsocks-libev:latest

ENV SERVER_ADDR=0.0.0.0 \
    SERVER_PORT=8388 \
    PASSWORD=${PASSWORD} \
    METHOD=chacha20-ietf-poly1305

EXPOSE 8388

CMD exec ss-server -s $SERVER_ADDR -p $SERVER_PORT -k $PASSWORD -m $METHOD --fast-open
