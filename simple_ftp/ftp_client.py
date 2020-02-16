import socket
import os

with socket.socket() as soc:
    soc.connect(("192.168.1.27", 1234))

    ##file transfer
    with open("test.txt", "wb") as f:
        file_size = int(soc.recv(1024).decode())
        total_sent = 0
        while total_sent < file_size:
            buffer = soc.recv(256)
            f.write(buffer)
            total_sent += len(buffer)

    print("file transferd! bye!")

input()