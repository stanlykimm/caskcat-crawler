import secrets
import requests

img_url = 'https://www.htfw.com/media/catalog/product/cache/eb03fb83d059c87eddc7a56651d2b8cf/l/p/lp13204_1.jpg'
name = str(secrets.token_hex(nbytes=32))
img = requests.get(img_url)
if img.status_code == 200:        
    with open(name, 'wb') as f:
        for chunk in img:
            f.write(chunk)
else:
  print(img.text)
  print('error %s = ', img.status_code)