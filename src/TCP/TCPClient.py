import sys
import socket

judge = ['Green Pass', 'Red Pass']
class TCPClient:

    def __init__(self, server_address, buffer_size) -> None:
        self.server_address = server_address
        self.buffer_size = buffer_size
        # create a client tcp socket
        self.TCPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # method to start a connection with tcp server
    def start(self):
        msgFromClient = "Hello TCP Server"
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
        self.TCPClientSocket.sendto(msg.encode(), self.server_address)
        print("Successfully send message to server", str(self.server_address))

    # method to receive message from server
    def recv(self):
        msgFromServer = self.TCPClientSocket.recvfrom(self.buffer_size)
        print(msgFromServer[0].decode())
        return msgFromServer[0].decode()


if __name__ == '__main__':

    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
    tcp_client = TCPClient(serverAddressPort, bufferSize)
    tcp_client.start()
