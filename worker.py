# worker.py
import socket
import time

def handle_request(request_type):
    if request_type == "Long":
        # Simulasi proses perhitungan yang kompleks
        time.sleep(2)
        return "Processed Long Task"
    elif request_type == "Short":
        # Simulasi proses perhitungan yang sederhana
        time.sleep(1)
        return "Processed Short Task"
    else:
        return "Unknown Task Type"

def worker_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen()

    print(f"Worker server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Received connection from {addr}")
        
        request_type = client_socket.recv(1024).decode('utf-8')
        response = handle_request(request_type)
        
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

# Jalankan ini pada port 9004, 9005, dan 9006 untuk tiga server pekerja.
if __name__ == "__main__":
    import sys
    port = int(sys.argv[1])  #Jalankan setiap pekerja pada port yang berbeda
    worker_server(port)
