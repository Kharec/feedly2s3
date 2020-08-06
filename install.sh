#!/bin/sh

if [ ! -f /usr/bin/sudo ]
then
  exit 1
fi

sudo pip install -r requirements.txt
sudo mkdir -p /opt/bin/
sudo cp bin/feedly2s3.py /opt/bin/feedly2s3

echo -n "Feedly's API token: "
read token
sudo sed -i "s/TOKEN =/TOKEN = "\"$token\""/g" /opt/bin/feedly2s3

echo -n "AWS S3 bucket's name: "
read s3name
sudo sed -i "s/BUCKET =/BUCKET = "\"$s3name\""/g" /opt/bin/feedly2s3

echo "Done, don't forget to add /opt/bin to your PATH."
