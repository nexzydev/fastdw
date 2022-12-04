import socket, requests

s = socket.socket()         
 
s.bind(('', 8888 ))
s.listen(0)                 
 
while True:
    client, addr = s.accept()

    while True:
        content = client.recv(2042)
        if len(content) == 0:
           break
        else:
            print(f"enviando o arquivo {content.decode()}")
            req = requests.get(content.decode("utf-8"))
            client.send(req.content)
            print("Arquivo enviado, fim da conexao")
    client.close()
