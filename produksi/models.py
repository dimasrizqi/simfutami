from django.db import models

class Instagram(models.Model):
	nama_depan	  	= models.CharField(max_length=100)
	nama_belakang 	= models.CharField(max_length=100)
	username		= models.CharField(max_length=100)

	def __str__(self):
		return "{}".format(self.username)

# Create your models here.
class departement(models.Model):
	departement_id = models.AutoField(primary_key=True)
	departement = models.CharField(max_length=100)
	def __str__(self):
		return str(self.departement)

class pengguna(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	nama_lengkap = models.CharField(max_length=100)
	departement = models.ForeignKey('departement')

	def __str__(self):
		return "{}".format(self.username)

class Release(models.Model):
	produksi_id = models.AutoField(primary_key=True)
	nomor_batch = models.IntegerField()
	nomor_palet  = models.IntegerField()
	jumlah_dus  = models.IntegerField()
	jumlah_botol  = models.IntegerField()
	status = models.CharField(max_length=10)
	rak = models.CharField(max_length=10)
	lantai = models.CharField(max_length=10)
	baris = models.CharField(max_length=10)

	def __str__(self):
		return str(self.status)


class jenis_status(models.Model):
	status_id = models.AutoField(primary_key=True)
	status = models.CharField(max_length=100)
	warna = models.CharField(max_length=100)

	def __str__(self):
		return "{}-{}".format(self.status,self.warna)

class status_product(models.Model):
	product_per_palet =  models.ForeignKey('productperpalet')
	status_product =  models.ForeignKey('jenis_status')
	pengguna = models.ForeignKey('pengguna')
	update_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}-{}".format(self.status_product,self.product_per_palet)


class product(models.Model):
	id_product = models.AutoField(primary_key=True)
	kode_product = models.CharField(max_length=5)
	nama_product = models.CharField(max_length=100)
	varian =  models.CharField(max_length=100)
	deskripsi =  models.CharField(max_length=200)
	pengguna = models.ForeignKey('pengguna')
	update_time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return (self.kode_product)

class productperpalet(models.Model):
	productperpalet_id = models.AutoField(primary_key=True)
	kode_product = models.ForeignKey('product')
	nomor_batch = models.CharField(max_length=100)
	nomor_palet = models.CharField(max_length=100)
	tanggal_produksi = models.DateTimeField(auto_now_add=True)
	jumlah_dus  = models.IntegerField()
	jumlah_botol  = models.IntegerField()
	pengguna = models.ForeignKey('pengguna')
	update_time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%s-%s-%s-%s" % (self.productperpalet_id, self.nomor_batch, self.nomor_palet, self.kode_product)

class lokasipenyimpanan(models.Model):
	lokasi_penyimpanan_id = models.AutoField(primary_key=True)
	tempat = models.CharField(max_length=100)

class transisi(models.Model):
	choose_status_perpindahan = (
		('CONVEYOR' , 'CONVEYOR'),
		('GUDANG TRANSISI' , 'GUDANG TRANSISI'),
		('GUDANG HCI' , 'GUDANG HCI'),
		('GUDANG RACKING' , 'GUDANG RACKING')
		)
	transisi_id = models.AutoField(primary_key=True)
	product_per_palet =  models.ForeignKey('productperpalet')
	status_perpindahan = models.CharField(max_length=100, choices=choose_status_perpindahan)
	pengguna = models.ForeignKey('pengguna')
	update_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}.{}.{}.{}".format(self.update_time,self.transisi_id,self.status_perpindahan,self.product_per_palet)
		

class gudangracking(models.Model):
	choose_blok = (
		('A' , 'A'),
		('B' , 'B'),
		('C' , 'C'),
		('D' , 'D'),
		('E' , 'E'),
		('F' , 'F'),
		('G' , 'G'),
		)
	choose_tingkat = (
		('1' , '1'),
		('2' , '2'),
		('3' , '3'),
		('4' , '4'),
		('5' , '5'),
		)
	choose_lorong = (
		('1' , '1'),
		('2' , '2'),
		('3' , '3'),
		('4' , '4'),
		('5' , '5'),
		('6' , '6'),
		('7' , '7'),
		('8' , '8'),
		('9' , '9'),
		('10' , '10'),
		('11' , '11'),
		('12' , '12'),
		('13' , '13'),
		('14' , '14'),
		('15' , '15'),
		('16' , '16'),
		('17' , '17'),
		('18' , '18'),
		('19' , '19'),
		('20' , '20'),
		('21' , '21'),
		('22' , '22'),
		('23' , '23'),
		('24' , '24'),
		('25' , '25'),
		('26' , '26'),
		('27' , '27'),
		('28' , '28'),
		('29' , '29'),
		('30' , '30'),
		)
	choose_baris = (
		('1' , '1'),
		('2' , '2'),
		('3' , '3'),
		('4' , '4'),
		('5' , '5'),
		('6' , '6'),
		)

	gudangracking_id = models.AutoField(primary_key=True)
	product_per_palet =  models.ForeignKey('productperpalet')
	blok = models.CharField(max_length=10, choices=choose_blok)
	tingkat = models.CharField(max_length=10, choices=choose_tingkat)
	lorong = models.CharField(max_length=10, choices=choose_lorong)
	baris = models.CharField(max_length=10, choices=choose_baris)
	pengguna = models.ForeignKey('pengguna')
	update_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Kode Product {} - Blok {}, Tingkat {}, Lorong {}, Baris {} ".format(self.product_per_palet,self.blok,self.tingkat,self.lorong,self.baris)

class tujuan(models.Model):
	tujuan_id = models.AutoField(primary_key=True)
	nama_tujuan = models.CharField(max_length=200) 
	alamat_tujuan = models.CharField(max_length=500)

	def __str__(self):
		return str(self.nama_tujuan)

class productkeluar(models.Model):
	choose_referensi_qc = (
		('OK' , 'OK'),
		('NOT OK' , 'NOT OK'),
	)
	productkeluar_id = models.AutoField(primary_key=True)
	tujuan = models.ForeignKey('tujuan')
	list_product = models.CharField(max_length=500)
	nomor_segel = models.CharField(max_length=20) 
	referensi_qc =  models.CharField(max_length=10, choices=choose_referensi_qc)
	nomor_do = models.CharField(max_length=20)
	update_time = models.DateTimeField(auto_now_add=True)
	pengguna = models.ForeignKey('pengguna')

	def __str__(self):
		return "%s - %s - %s" % str(self.tujuan,self.nomor_segel,self.nomor_do)