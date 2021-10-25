import socket

class UDPClient:

    def __init__(self, server_address, buffer_size) -> None:
        self.server_address = server_address
        self.buffer_size = buffer_size
        # create a client udp socket
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    # method to start a connection with udp server
    def start(self):
        msgFromClient = "Hello UDP Server"
        bytesToSend = str.encode(msgFromClient)
        self.send(bytesToSend)

    # method to send message to client
    def send(self, msg):
        self.UDPClientSocket.sendto(msg, self.server_address)
        print("Successfully send message to server", str(self.server_address))

    # method to receive message from server
    def recv(self):
        msgFromServer = self.UDPClientSocket.recvfrom(self.buffer_size)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)


if __name__ == '__main__':

    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024
    udp_client = UDPClient(serverAddressPort, bufferSize)
    udp_client.start()
