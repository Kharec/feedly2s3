#!/bin/sh

if [ ! -f /usr/bin/sudo ]
then
  exit 1
fi

echo -n "Feedly's API token: "
read token
sed -i "s/TOKEN =/TOKEN = "\"$token\""/g" bin/feedly2s3.py

echo -n "AWS S3 bucket's name: "
read s3name
sed -i "s/BUCKET =/BUCKET = "\"$s3name\""/g" bin/feedly2s3.py

sudo pip install -r requirements.txt
sudo mkdir -p /opt/bin/
sudo mv bin/feedly2s3.py /opt/bin/feedly2s3

echo "Done, don't forget to add /opt/bin to your PATH."
