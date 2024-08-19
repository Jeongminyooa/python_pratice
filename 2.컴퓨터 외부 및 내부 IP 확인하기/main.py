import socket
import requests
import re

# 내부(와이파이 등 공유기) 로컬호스트 IP 주소
in_addr = socket.gethostbyname(socket.gethostname())
print(f"내부 IP : {in_addr}")

req = requests.get("http://ipconfig.kr/")# Response 200 

# 외부 : 망 사용 KT/LG 등에서 부여
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(f"외부 IP : {out_addr}")