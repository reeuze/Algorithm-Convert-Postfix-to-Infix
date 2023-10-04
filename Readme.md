Subject : Data structure and algorithm Assesment #5

Create a program that will change from infix to postfix.
This is the example of Infix convert to Postfix :

![alt text](https://github.com/reeuze/Algorithm-Convert-Postfix-to-Infix/blob/main/Image/Postfix%20to%20Infix%20(1).jpg?raw=true)

The Algorithm :
1. Lakukan konversi input dari berbentuk string menjadi bentuk stack
2. Cek satu persatu elemen dalam stack input
3. Apabila elemen berupa operator +,-,*,/, atau ^; maka lakukan penggabungan dengan 2 angka sebelumnya
4. Lakukan terus sampai panjang stack input sama dengan 1
5. Tampilkan stack input dalam bentuk string sebagi hasil akhir