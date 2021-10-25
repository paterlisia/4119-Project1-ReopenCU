import socket


check_problems = ['Have you experienced any COVID-19 symptoms in the past 14 days?',
                    'Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days?',
                    'Have you tested positive for COVID-19 in the past 14 days?'
]
class TCPServer:

    def __init__(self, ip_address, port_number, buffer_size):
        self.ip_address = ip_address
        self.port_number = port_number
        self.buffer_size = buffer_size
        self.TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # method to start the tcp server
    def start(self):
        try:
            # a hello message from server to client at the very beginning
            self.TCPServerSocket.bind((self.ip_address, self.port_number))
            print("TCP server starts successfully with ip", str(self.ip_address))
            # Listen for incoming datagrams
            while (True):
                message, address = self.TCPServerSocket.recvfrom(self.buffer_size)
                client_msg = "Message from Client:{}".format(message.decode())
                client_ip = "Client IP Address:{}".format(address)
                print(client_msg)
                print(client_ip)
                # send welcome message to the client
                msgFromServer = "Hello TCP Client"
                self.send(msgFromServer, address)
                status = self.check(address)
                if status:
                    msgFromServer = 'Green Pass'
                else:
                    msgFromServer = 'Red Pass'
                # return the check status to client
                self.send(msgFromServer, address)
        except Exception as e:
            print(e)

    # method to send message to client
    def send(self, msg, client_address):
        self.TCPServerSocket.sendto(msg.encode(), client_address)
        print("Successfully send message to client", str(client_address[0]))


    # method to check health status
    def check(self, client_address):
        index = 0
        while(index < 3):
            self.send(check_problems[index], client_address)
            message, address = self.TCPServerSocket.recvfrom(self.buffer_size)
            print(message.decode().lower())
            if (message.decode().lower() == 'no\n'):
                index += 1
            # red pass
            elif (message.decode().lower() == 'yes\n'):
                return False
            # receive other answer, reask the question
            else:
                pass
        return True


if __name__ == '__main__':

    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024

    tcp_server = TCPServer(localIP, localPort, bufferSize)
    tcp_server.start()


    