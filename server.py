import argparse
import socket
import sys
import time

parser = argparse.ArgumentParser(description="A server which acts as an speedtest.net end point", formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('-i', '--server-ip', help="IP Address the server runs on (default: localhost)", type=str, default="localhost")
parser.add_argument('-p', '--port-no', help="Port Number the server runs on (default: 23645)", type=int, default=23645)
parser.add_argument('-n', '--connections', help="Number of connections to handle (default: 5)", type=int, default=5)

args = vars(parser.parse_args(sys.argv[1:]))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

FILE = '350x350.jpg'

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
    connections = int(args['connections'])
    assert connections > 0
except Exception, e:
    sys.stderr.write("Number of connections must be positive\n")
    sys.exit(3)

try:
    sock.bind((host, port))
    sock.listen(connections)
    connection, address = sock.accept()
    print "Connected to " + str(address)
    data = None
    with open(FILE, 'rb') as filep:
        data = filep.read()
    if data:
        size = len(data)
        n = connection.send(data)
        start = time.time()
        data = ""
        while len(data) < size:
            data += connection.recv(size)
        end = time.time()
        connection.send(str(end-start))
finally:
    sock.close()
