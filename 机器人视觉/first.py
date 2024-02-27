import requests
r=requests.get('https://www.ncc.edu.cn/_upload/site/00/0c/12/logo.png')
#print(r.content)
with open('ncc_logo.png','wb')as f:
    f.write(r.content)