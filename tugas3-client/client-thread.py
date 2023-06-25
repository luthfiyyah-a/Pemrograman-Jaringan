import socket
import threading


def send_request():
    server_address = ('0.0.0.0', 45000)
    request = "TIME\r\n"

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the serer
        sock.connect(server_address)

        # send the request
        sock.sendall(request.encode('utf-8'))

        # Receive and print the response
        response = sock.recv(1024).decode('utf-8')
        print(response)

    finally:
        # Close the socket
        sock.close

# Create multiple threads to send requests concurrently
for i in range(5):
    thread = threading.Thread(target=send_request)
    thread.start()