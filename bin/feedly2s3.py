#!python3
# coding: utf-8
import requests
import boto3
from datetime import datetime
from botocore.exceptions import ClientError as S3Error

#TOKEN = "" # your feedly token
#BUCKET = "" # your aws s3 bucket

TOKEN = "A1Zpruh9VoMGTL0f6iZ1R4B8eVINNUkmJgbt2HwAenB4ZX5PRToyxmrd9TI4KJPAJwWA525_I2PiON7lHe0wkrKaZfyCMaihJ5iE6wKeO1mCCS5iHiuSJRA1GYIOgnnobdYpL3ryvtoG2wN-4-N2QSIZEosurDkKa0K2sg4GAra1KNK0rIHs8Anm3_mQKjicCxyjsBQm7xR00XxsI4GPLwbG8RnCwf4752dyFJew7tU_Dm2on6LHAVD2VCxn:feedlydev"
BUCKET = "feedly2s3" # your aws s3 bucket

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

if __name__ == '__main__':
    job = Feedly2S3()
    job.backup()
