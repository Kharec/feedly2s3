#!/bin/sh

if [ ! -f /usr/bin/sudo ]
then
  echo "Just move bin/feedly2s3.py to any location which will be in your PATH."
  exit 1
fi

sudo pip install -r requirements.txt
sudo mkdir -p /opt/bin/
sudo mv bin/feedly2s3.py /opt/bin/feedly2s3

echo "Done, don't forget to add /opt/bin to your PATH."
