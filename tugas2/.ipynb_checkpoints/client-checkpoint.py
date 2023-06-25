import socket

def main():
    server_address = ('172.16.16.101', 45000)
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        sock.connect(server_address)
        
        # Send request to the server
        request = "TIME\r\n"
        sock.sendall(request.encode('utf-8'))
        
        # Receive and print the response
        response = sock.recv(32).decode('utf-8')
        print(response)
        
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    main()
