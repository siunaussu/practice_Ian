import socket

# create socket service
server_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# config reuseaddr
server_tcp_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind IP and port
server_tcp_client.bind(('0.0.0.0', 9000))

# listen
server_tcp_client.listen(1)

# wait client connect
con_client, addr = server_tcp_client.accept()
print("client connected：", addr)
con_client.send('you have connected successfully!'.encode('utf-8'))

# receive data
while True:
    msg = input(">")

    data = con_client.recv(1024)
    str_data = data.decode("utf-8")
    if str_data == "quit":
        break
    print("client said: ", str_data)


    con_client.send(msg.encode("utf-8"))

# close
con_client.close()
server_tcp_client.close()
