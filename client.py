import argparse
import socket
import sys
import time

parser = argparse.ArgumentParser(description="A server which acts as an speedtest.net end point", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('-i', '--server-ip', help="IP Address the server runs on (default: localhost)", type=str, default="localhost")
parser.add_argument('-p', '--port-no', help="Port Number the server runs on (default: 23645)", type=int, default=23645)

args = vars(parser.parse_args(sys.argv[1:]))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    host = socket.gethostbyname(args['server_ip'])
except Exception, e:
    sys.stderr.write("Invalid IP Address specified\n")
    sys.exit(1)

try:
    port = int(args['port_no'])
    assert port > 0
except Exception, e:
    sys.stderr.write("Port Number must be positive\n")
    sys.exit(2)

try:
    sock.connect((host, port))
except socket.error, msg:
    sys.stderr.write("Could not connect to server\n")
    sys.exit(2)

file_size = 24045
data = ""
start = time.time()
while len(data) < file_size:
    data += sock.recv(file_size)
end = time.time()
if len(data) != 24045:
    sys.stderr.write("Could not download the entire file\n")
    sys.exit(3)
else:
    print "Download speed = %s Bits/sec" % (str((24045*8)/(end-start)))

sock.send(data)
upload_speed = float(sock.recv(1024))
print "Upload speed = %s Bits/sec" % (str((24045*8)/(end-start)))
