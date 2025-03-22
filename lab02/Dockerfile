FROM alpine

# Instala lighttpd
RUN apk update && apk add lighttpd rm -rf /var/cache/apk/*

# Crear estructura del sitio
RUN mkdir -p /var/www/localhost/htdocs/css \
    && mkdir -p /var/www/localhost/htdocs/js

# Copiar archivos al contenedor
COPY index.html /var/www/localhost/htdocs/
COPY css/ /var/www/localhost/htdocs/css/
COPY js/ /var/www/localhost/htdocs/js/

# Comando de inicion del servidor
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]