#free flost ftp_offset.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ipv4 and tcp socket

s.connect(('ip 주소', 21))

