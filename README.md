NIM  : 24051905004   
NAMA : Windy Chikita Cornia Putri

TUGAS
Buatlah implementasi client-server socket yang mensimulasikan "load balancing" secara sederhana Python dengan detail sebagai berikut:
1 Ditulis dalam bahasa Python.
2 Server utama (broker) menerima request dari client dan mendistribusikan ke 3 server lain (worker) dalam "cluster".
3 Terdapat 2 pendekatan alokasi:
	a. pemerataan jumlah request yang sudah dilayani oleh masing-masing
	server pekerja
	b. berurutan sesuai dengan server-id berdasar counter pada server utama
4 Masing-masing worker server mempunyai 2 jenis aplikasi yang dilayani (bisa dimisalkan saja (tanpa implementasi):
	a. Long ⇒ seperti perhitungan yang kompleks
	b. Short ⇒ seperti echo atau perhitungan sederhana
5 Client mengirim sintaks ke broker dengan menyebutkan Application ID ⇒ Silakan definisikan sintaks/protokol/messaging format.
6 Broker mencetak pesan informasi ke layar.
