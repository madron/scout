#!/bin/sh
set -e

if [ "$1" = 'uwsgi' ]; then
    su-exec nobody /src/manage.py wait_for_database --timeout 20
    su-exec nobody /src/manage.py migrate --noinput
    echo su-exec nobody $*
    exec su-exec nobody $*
elif [ "$1" = 'nginx' ]; then
    chown nobody /var/tmp/nginx
    exec nginx -c /src/docker/nginx.conf -g "daemon off;"
else
    exec "$@"
fi
