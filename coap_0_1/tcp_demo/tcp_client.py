'''
Author: geekli
Date: 2021-01-25 10:58:26
LastEditTime: 2021-01-25 10:59:34
LastEditors: your name
Description: 
FilePath: /coap_0_1/tcp_demo/tcp_client.py
'''
import asyncio
# replace ip address here
raspberry_ip_addrss = '192.168.1.8'
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

loop = asyncio.get_event_loop()
message = 'Hello World!'
coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                              raspberry_ip_addrss, 8090)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()