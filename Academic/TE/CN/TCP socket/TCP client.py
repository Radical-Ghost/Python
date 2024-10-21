import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    message = input("Enter string: ")
    client.send(bytes(message, "utf-8"))
    ack = client.recv(1024)
    ack = ack.decode("utf-8")
    print("Server: ", ack)
    client.close()