import socket
import sys

# a list of places to send block notificates as UDP packets. Powerpool
# is setup to listen for these packets
endpoints = [("127.0.0.1", 9000)]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
for endpoint in endpoints:
    sock.sendto(sys.argv[1] + " " + sys.argv[2], endpoint)
