#!python3
# coding: utf-8
import requests
import boto3
from datetime import datetime
from botocore.exceptions import ClientError as S3Error
from os import remove as delete_file

TOKEN = 
BUCKET = 

class Feedly2S3(object):
    def __init__(self):
        self.token = TOKEN
        self.bucket = BUCKET
        self.url = 'https://cloud.feedly.com/v3/opml'
        self.headers = {'Authorization': 'OAuth '+self.token}
        self.exporter = boto3.client('s3')
        self.filename = "/tmp/feedly-"+datetime.today().strftime('%Y%m%d')+".opml"
        self.objectname = "feedly-"+datetime.today().strftime('%Y%m%d')+".opml"

    def backup(self):
        self.opml = requests.get(url=self.url, headers=self.headers).text
        with open(self.filename, "a") as tmpfile:
            tmpfile.write(self.opml)
        try:
           self.exporter.upload_file(self.filename, self.bucket, self.objectname)
        except S3Error as e:
           print(e)
        delete_file(self.filename)

if __name__ == '__main__':
    job = Feedly2S3()
    job.backup()
