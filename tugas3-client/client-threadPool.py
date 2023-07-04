import socket
from concurrent.futures import ThreadPoolExecutor
import time


def send_request():
    ''' Membuka port di port 45000 dengan transport TCP '''
    server_address = ('172.16.16.101', 45000)
    '''
    Request ke server hanya dilayani dengan ketentuan:
    Diawali dengan string “TIME dan diakhiri dengan karakter 13 dan karakter 10”
    '''
    request = "TIME\r\n"

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

# Create a thread pool with 5 threads
with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(100000):
        # print("send request...")
        executor.submit(send_request)
        
if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        start_time = time.time()
        request_count = 0
        
        while time.time() - start_time < 30: # looping selama 30 detik
            executor.submit(send_request)
            request_count += 1
            
        logging.warning(f"Total request sent: {request_count}")