import socket

HOST = "79.114.19.165"  # Standard loopback interface address (localhost)
PORT = 5003  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.bind((HOST, PORT))
    # s.listen()
    s.connect((HOST,PORT))
        # conn, addr = s.accept()
    with open("received", "wb") as dest:
        while True:
            data = s.recv(104857600)
            dest.write(data)
            if not data:
                print("Client disconected!")
                break
        print("file recived")
