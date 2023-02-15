import os
import secrets
import requests
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import urllib.request
from .data import *

keyId = '0040fdfeba09c8f0000000001'
keyName = 'caskcatkey'
appKey = 'K004Inl7rmWHRkUhLvx8OpUYzJRVftE'
endpoint = 'https://s3.us-west-004.backblazeb2.com'
host = 'https://f004.backblazeb2.com/file/caskcat'

def get_b2(endpoint, key_id, application_key):
    return boto3.resource(service_name='s3',
                        endpoint_url=endpoint,
                        aws_access_key_id=keyId,
                        aws_secret_access_key=appKey,
                        config = Config(
                            signature_version='s3v4',
                    ))

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

def upload_image(img_url, website):
    ext = os.path.splitext(img_url)[1].split('?')[0]
    name = str(secrets.token_hex(nbytes=32)) + ext
    headers = eval(website+'_headers') if website == 'mom' else {}
    img = requests.get(img_url, headers=headers)
    if img.status_code == 200:        
        with open(name, 'wb') as f:
            for chunk in img:
                f.write(chunk)
        rtn = upload_file('caskcat', '', name,  b2, website+'/'+name)
        os.remove(name) 
    else:
        print("Failed to download image. Status code:", img.status_code)
    print(host + '/' + website+'/' + name)
    return host + '/' + website+'/' + name
    
b2 = get_b2(endpoint, keyId, appKey)