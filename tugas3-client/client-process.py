import socket
from concurrent.futures import ThreadPoolExecutor


def send_request():
    ''' Membuka port di port 45000 dengan transport TCP '''
    server_address = ('0.0.0.0', 45000)
    '''
    Request ke server hanya dilayani dengan ketentuan:
    Diawali dengan string “TIME dan diakhiri dengan karakter 13 dan karakter 10”
    '''
    request = "TIME\r\n"

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STEAM)

    try:
        # Connect to the server
        sock.connect(server_address)

        # Send the request
        sock.sendall(request.encode('utf-8'))

        # Receive and print the response
        response = sock.recv(1024).decode('utf-8')
        print(response)

    finally:
        # CLose the socket
        sock.close()

# Create multiple processes to send requests concurrently
for i in range(5:
    process = multiprocessing.Process(target=send_request)
    process.start()