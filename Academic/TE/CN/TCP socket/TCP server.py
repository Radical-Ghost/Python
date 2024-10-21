import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"Server listening on {ip}:{port}")

    while True:
        client, address = server.accept()
        print("Connection Established - " + str(address[0]) + ":" + str(address[1]))
        message = client.recv(1024)
        message = message.decode("utf-8")
        print("Client: ", message)
        message = input("Enter reply: ")
        client.send(bytes(message, "utf-8"))
        client.close()