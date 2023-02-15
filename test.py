import os
import sys
import boto3  # REQUIRED! - Details here: https://pypi.org/project/boto3/
from botocore.exceptions import ClientError
from botocore.config import Config
from dotenv import load_dotenv  # Project Must install Python Package:  python-dotenv
import requests
import secrets

keyId = '0040fdfeba09c8f0000000001'
keyName = 'caskcatkey'
appKey = 'K004Inl7rmWHRkUhLvx8OpUYzJRVftE'
ENDPOINT = 'https://s3.us-west-004.backblazeb2.com'

def get_b2_resource(endpoint, key_id, application_key):
    b2 = boto3.resource(service_name='s3',
                        endpoint_url=endpoint,                # Backblaze endpoint
                        aws_access_key_id=keyId,              # Backblaze keyID
                        aws_secret_access_key=appKey, # Backblaze applicationKey
                        config = Config(
                            signature_version='s3v4',
                    ))
    return b2

def upload_file(bucket, directory, file, b2, b2path=None):
    file_path = file
    remote_path = b2path
    if remote_path is None:
        remote_path = file
    try:
        response = b2.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)

    return response


def upload_file_ojb(bucket, directory, file, b2, b2path=None):
    file_path = file
    remote_path = b2path
    if remote_path is None:
        remote_path = file
    try:
        response = b2.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)

    return response

b2 = get_b2_resource(ENDPOINT, keyId, appKey)

name = str(secrets.token_hex(nbytes=32))
url = "https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg"
r = requests.get(url, stream=True)
with open(name, 'wb') as f:
    for chunk in r:
        f.write(chunk)
rtn = upload_file('caskcat', '', name,  b2, 'mom/2022/12/'+name)
os.remove(name)
print(rtn)