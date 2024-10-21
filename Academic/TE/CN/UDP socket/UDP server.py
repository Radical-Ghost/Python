import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        if data == "!EXIT":
            print("Client disconnected...")
            break
        print("Client: " + str(data))
        data = data.upper()
        data = data.encode("utf-8")
        server.sendto(data, addr)
    
    server.close()