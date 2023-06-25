import socket
import threading
import logging
import datetime
import sys

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            data = self.connection.recv(32).decode('utf-8')
            if data.startswith('TIME') and data.endswith('\r\n'):
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"JAM {current_time}\r\n"
                self.connection.sendall(response.encode('utf-8'))
            else:
                break
        logging.warning(f"closing connection from {self.address}")
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        # Create a TCP/IP socket -> using param socket.SOCK_STREAM
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        server_address = ('0.0.0.0', 45000)
        self.my_socket.bind(server_address)
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            self.my_socket.listen(1)
            while True:
                self.connection, self.client_address = self.my_socket.accept()
                logging.warning(f"connection from {self.client_address}")

                clt = ProcessTheClient(self.connection, self.client_address)
                clt.start()
                self.the_clients.append(clt)
        
def main():
    svr = Server()
    svr.start()


if __name__  == "__main__":
    main()