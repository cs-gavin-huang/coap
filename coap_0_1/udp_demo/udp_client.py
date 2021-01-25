'''
Author: geekli
Date: 2021-01-25 10:30:05
LastEditTime: 2021-01-25 10:38:49
LastEditors: your name
Description: 
FilePath: /coap_0_1/udp_demo/udp_client.py
'''
import asyncio
# replace ip address
raspberry_ip_addrss = '192.168.1.8'
class EchoClientProtocol:
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()

loop = asyncio.get_event_loop()
message = "Hello World!"
connect = loop.create_datagram_endpoint(
    lambda: EchoClientProtocol(message, loop),
    remote_addr=(raspberry_ip_addrss, 5683))
transport, protocol = loop.run_until_complete(connect)
loop.run_forever()
transport.close()
loop.close()
