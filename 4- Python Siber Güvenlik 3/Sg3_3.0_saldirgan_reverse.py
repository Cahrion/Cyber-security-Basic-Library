import socket
host="0.0.0.0"
port = 5000
soket = socket.socket()
soket.bind((host,port))
soket.listen()
conn, addr = soket.accept()
print("Baglanti Saglandi: ", str(conn))
mesaj = "Baglanti saglandi".encode()
conn.send(mesaj)
while True:
    komut = input("Komut: ")
    conn.send(komut.encode())
    if komut.lower()=="exit":
        break
    sonuc = conn.recv(1024).decode()
    print(sonuc)
conn.close()
soket.close()