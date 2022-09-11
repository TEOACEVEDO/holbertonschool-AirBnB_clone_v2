#!/usr/bin/env bash

if [ ! -e /var/run/nginx.pid ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo service nginx start
fi

if [[ ! -d /data/ ]]; then
    sudo mkdir /data
fi

if [[ ! -d /data/web_static/ ]]; then
    sudo mkdir /data/web_static
fi

if [[ ! -d /data/web_static/releases/ ]]; then
    sudo mkdir /data/web_static/releases
fi

if [[ ! -d /data/web_static/shared/ ]]; then
    sudo mkdir /data/web_static/shared
fi

if [[ ! -d /data/web_static/releases/test/ ]]; then
    sudo mkdir /data/web_static/releases/test
fi

if [[ ! -f /data/web_static/releases/test/index.html ]]; then
    sudo touch /data/web_static/releases/test/index.html
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html
fi

if [[ !-f /data/web_static/current ]]; then
    sudo ln -s /data/web_static/releases/test/ data/web_static/current
else
    sudo rm data/web_static/current
    sudo ln -s /data/web_static/releases/test/ data/web_static/current
fi

chown -R 755 /data/
