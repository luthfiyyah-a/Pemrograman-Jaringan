import socket
import threading
import time
import logging


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
        # Connect to the serer
        sock.connect(server_address)

        # send the request
        sock.sendall(request.encode('utf-8'))

        # Receive and print the response
        response = sock.recv(1024).decode('utf-8')
        print(response)

    finally:
        # Close the socket
        sock.close()

# Create multiple threads to send requests concurrently
# for i in range(100):
#     thread = threading.Thread(target=send_request)
#     thread.start()

if __name__ == "__main__":
    
#     menguji jumlah thread maksimum
    thread_count = 0
    start_time = time.time()
    
#     looping selama 30 detik untuk membuat thread
    while time.time() - start_time < 30:
        thread = threading.Thread(target=send_request)
        thread.start()
        thread_count += 1
    logging.warning(f"Total thread created: {thread_count}")
    