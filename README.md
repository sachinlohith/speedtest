# Speedtest Python #
A simple speedtest python module to test internet speed. 
> Speeds are measured in Bits/sec

# ASSUMPTIONS #
- While transfering a file over the network to measure the network speed file I/O time is not counted towards network speed

# BUILD #
- Run the following commands for server (after copying both server.py and 350x350.jpg to your desired folder):
```bash
$ python server.py -i IP -p PORT_NO
```
- For help on how to run the server run:
```bash
$ python server.py -h
```
- Run the following commands for the client:
```bash
$ python client.py -i IP -p PORT_NO
```
- For help on how to run the client run:
```bash
$ python client.py -h
```
