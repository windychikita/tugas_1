# broker.py
import socket

#  daftar alamat dan port server pekerja (worker server):
WORKERS = [("localhost", 9004), ("localhost", 9005), ("localhost", 9006)]
round_robin_counter = 0
requests_served = [0, 0, 0]  # Lacak jumlah permintaan untuk setiap pekerja

def distribute_request(application_id, allocation_type):
    global round_robin_counter
    if allocation_type == "round_robin":
        worker = WORKERS[round_robin_counter]
        print(f"Allocating to {worker} using Round Robin.")
        round_robin_counter = (round_robin_counter + 1) % len(WORKERS)
    elif allocation_type == "load_balancing":
        min_requests = min(requests_served)
        worker_index = requests_served.index(min_requests)
        worker = WORKERS[worker_index]
        requests_served[worker_index] += 1
        print(f"Allocating to {worker} using Load Balancing (min load).")
    else:
        raise ValueError("Unknown allocation type")
    
    # Menampilkan informasi tentang permintaan yang didistribusikan
    print(f"Broker sending '{application_id}' request to Worker {worker}")
    
    # Kirim permintaan ke pekerja yang telah dipilih
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(worker)
        s.send(application_id.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
    
    print(f"Broker received response from {worker}: {response}")
    return response

def broker_server():
    broker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    broker_socket.bind(('localhost', 8000))
    broker_socket.listen()
    
    print("Broker server listening on port 8000...")
    
    while True:
        client_socket, addr = broker_socket.accept()
        print(f"Connection from {addr}")
        
        # Terima data dari klien
        data = client_socket.recv(1024).decode('utf-8')
        application_id, allocation_type = data.split(',')
        
        # Menampilkan informasi tentang permintaan yang diterima
        print(f"Received request from Client {addr} - Application ID: {application_id}, Allocation Type: {allocation_type}")
        
        # Menyebarkan permintaan ke server pekerja
        response = distribute_request(application_id, allocation_type)
        
        # Kirim respons kembali ke klien
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    broker_server()
