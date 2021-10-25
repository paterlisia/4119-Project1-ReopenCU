import sys
import socket

judge = ['Green Pass', 'Red Pass']
class UDPClient:

    def __init__(self, server_address, buffer_size) -> None:
        self.server_address = server_address
        self.buffer_size = buffer_size
        # create a client udp socket
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # method to start a connection with udp server
    def start(self):
        msgFromClient = "Hello UDP Server"
        self.send(msgFromClient)
        msg_recv = self.recv()
        while True:
            msg_recv = self.recv()
            if msg_recv in judge:
                break
            # get input from keyboard output
            response = sys.stdin.readline()
            # send reponse back to server
            self.send(response)
            

    # method to send message to client
    def send(self, msg):
        self.UDPClientSocket.sendto(msg.encode(), self.server_address)
        print("Successfully send message to server", str(self.server_address))

    # method to receive message from server
    def recv(self):
        msgFromServer = self.UDPClientSocket.recvfrom(self.buffer_size)
        print(msgFromServer[0].decode())
        return msgFromServer[0].decode()


if __name__ == '__main__':

    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
    udp_client = UDPClient(serverAddressPort, bufferSize)
    udp_client.start()
