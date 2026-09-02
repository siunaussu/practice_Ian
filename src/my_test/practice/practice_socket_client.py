import socket

# create
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect
client_socket.connect(("8.153.154.71",9000))

# send data
while True:
    data = client_socket.recv(1024)
    print(f"server said: {data.decode('utf-8')}")

    msg = input(">")
    client_socket.send(msg.encode('utf-8'))
    if msg == "quit":
        break

# close
client_socket.close()
