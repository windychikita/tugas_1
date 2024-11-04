# client.py
import socket

def send_request(application_id, allocation_type):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8000))
        # Mengirim ID Aplikasi dan metode alokasi
        s.send(f"{application_id},{allocation_type}".encode('utf-8'))
        
        response = s.recv(1024).decode('utf-8')
        print(f"Client received response: {response}")

if __name__ == "__main__":
    # permintaan dengan ID Aplikasi dan metode alokasi
    send_request("Long", "round_robin")      # Menggunakan ID Long dengan metode alokasi round robin
    send_request("Short", "load_balancing")   # Menggunakan ID Short dengan metode alokasi load balancing
    send_request("Long", "load_balancing")    # Menggunakan ID Long dengan metode alokasi load balancing
