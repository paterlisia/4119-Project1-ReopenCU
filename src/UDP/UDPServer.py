import socket

class UDPServer:

    def __init__(self, ip_address, port_number, buffer_size):
        self.ip_address = ip_address
        self.port_number = port_number
        self.buffer_size = buffer_size
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # method to start the udp server
    def start(self):
        try:
            # a hello message from server to client at the very beginning
            msgFromServer = "Hello UDP Client"
            self.UDPServerSocket.bind((self.ip_address, self.port_number))
            print("UDP server starts successfully with ip", str(self.ip_address))
            # Listen for incoming datagrams
            while (True):
                message, address = self.UDPServerSocket.recvfrom(self.buffer_size)
                client_msg = "Message from Client:{}".format(message)
                client_ip = "Client IP Address:{}".format(address)
                print(client_msg)
                print(client_ip)
                self.send(msgFromServer, address)
        except Exception as e:
            print(e)

    # method to send message to client
    def send(self, msg, client_ip):
        self.UDPServerSocket.sendto(msg.encode(), client_ip)
        print("Successfully send message to client", str(client_ip[0]))

    # method to close udp server
    # def close(self):

if __name__ == '__main__':

    localIP = "127.0.0.1"

    localPort = 20001

    bufferSize = 1024

    udp_server = UDPServer(localIP, localPort, bufferSize)
    udp_server.start()


    