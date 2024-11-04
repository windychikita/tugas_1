NIM  : 24051905004 <br>
NAMA : Windy Chikita Cornia Putri <br>

TUGAS<br>
Buatlah implementasi client-server socket yang mensimulasikan "load balancing" secara sederhana Python dengan detail sebagai berikut:<br>
1 Ditulis dalam bahasa Python.<br>
2 Server utama (broker) menerima request dari client dan mendistribusikan ke 3 server lain (worker) dalam "cluster".<br>
3 Terdapat 2 pendekatan alokasi:<br>
	a. pemerataan jumlah request yang sudah dilayani oleh masing-masing server pekerja <br>
	b. berurutan sesuai dengan server-id berdasar counter pada server utama <br>
4 Masing-masing worker server mempunyai 2 jenis aplikasi yang dilayani (bisa dimisalkan saja (tanpa implementasi): <br>
	a. Long ⇒ seperti perhitungan yang kompleks <br>
	b. Short ⇒ seperti echo atau perhitungan sederhana <br>
5 Client mengirim sintaks ke broker dengan menyebutkan Application ID ⇒ Silakan definisikan sintaks/protokol/messaging format. <br>
6 Broker mencetak pesan informasi ke layar. <br>
