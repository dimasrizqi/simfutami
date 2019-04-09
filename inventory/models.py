from django.db import models

class jenis(models.Model):
	jenis_id = models.AutoField(primary_key=True)
	nama_jenis = models.CharField(max_length=100)

	def __str__(self):
		return self.nama_jenis

class sistem_operasi(models.Model):
	choose_sistem_operasi = (
		('Win XP', 'Win XP'),
		('Win 7 32bit', 'Win 7 32bit'),
		('Win 7 64bit', 'Win 7 64bit'),
		('Win 8 32bit', 'Win 8 32bit'),
		('Win 8 64bit', 'Win 8 64bit'),
		('Win 10 32bit', 'Win 10 32bit'),
		('Win 10 64bit', 'Win 10 64bit'),	
	)
	sistem_operasi_id = models.AutoField(primary_key=True)
	sistem_operasi = models.CharField(max_length=100, choices=choose_sistem_operasi, default='Win 7 32bit')
	serial_number = models.CharField(max_length=100)
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.sistem_operasi ,self.dipakai_pada_komputer)

class memory(models.Model):
	choose_kapasitas_memory = (
		('1Gb', '1Gb'),
		('2Gb', '2Gb'),
		('4Gb', '4Gb'),
		('8Gb', '8Gb'),
	)

	choose_ddr = (
		('DDR1','DDR1'),
		('DDR2','DDR2'),
		('DDR3','DDR3'),
		('DDR4','DDR4'),
	)

	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)

	memory_id = models.AutoField(primary_key=True)
	merek_memory = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	ddr =  models.CharField(max_length=100, choices=choose_ddr, default='DDR2')
	kapasitas = models.CharField(max_length=100, choices=choose_kapasitas_memory, default='1 Gb')
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	catatan = models.CharField(max_length=255,blank = True,null=True)

	def __str__(self):
	 	return "%s - %s - %s" % (self.merek_memory, self.kapasitas, self.dipakai_pada_komputer)

class storage(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_kapasitas_storage = (
		('40Gb', '40Gb'),
		('80Gb', '80Gb'),
		('120Gb', '120Gb'),
		('250Gb', '250Gb'),
		('320Gb', '320Gb'),
		('500Gb', '500Gb'),
		('1Tb', '1Tb'),
		('2Tb', '2Tb'),
	)
	choose_tipe_storage = (
		('HDD','HDD'),
		('SDD','SDD'),
		('M2','M2'),
		)
	storage_id = models.AutoField(primary_key=True)
	merek_storage = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	kapasitas = models.CharField(max_length=100, choices=choose_kapasitas_storage, default='320 Gb')
	tipe_storage = models.CharField(max_length=100, choices=choose_tipe_storage, default='HDD')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s - %s" % (self.merek_storage , self.kapasitas, self.dipakai_pada_komputer)

class psu(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_kapasitas_psu = (
		('350 Watt','350 Watt'),
		('400 Watt','400 Watt'),
		('450 Watt','450 Watt'),
		('500 Watt','500 Watt'),
		('550 Watt','550 Watt'),
		)
	psu_id = models.AutoField(primary_key=True)
	merek_psu = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	kapasitas_psu = models.CharField(max_length=100, choices=choose_kapasitas_psu, default='400 Watt')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)

	def __str__(self):
	 	return "%s - %s - %s" % (self.merek_psu, self.kapasitas_psu ,self.dipakai_pada_komputer)

class processor(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_merek_processor = (
		('AMD','AMD'),
		('INTEL','INTEL')		
	)
	processor_id = models.AutoField(primary_key=True)
	merek_processor = models.CharField(max_length=100, choices=choose_merek_processor, default='INTEL')
	serial_number = models.CharField(max_length=100)
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_processor ,self.dipakai_pada_komputer)

class motherboard(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	motherboard_id = models.AutoField(primary_key=True)
	tipe_socket = models.CharField(max_length=100)
	merek_motherboard = models.CharField(max_length=100)
	tipe_motherboard = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_motherboard ,self.dipakai_pada_komputer)

class cctv(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	cctv_id = models.AutoField(primary_key=True)
	merek_cctv = models.CharField(max_length=100)
	tipe_cctv = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	lokasi_cctv = models.CharField(max_length=100)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_cctv ,self.lokasi_cctv)

class dvr(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	dvr_id = models.AutoField(primary_key=True)
	merek_dvr = models.CharField(max_length=100)
	tipe_cctv = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	lokasi_dvr = models.CharField(max_length=100)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_dvr ,self.lokasi_dvr)

class pabx(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	pabx_id = models.AutoField(primary_key=True)
	merek_pabx = models.CharField(max_length=100)
	tipe_pabx = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	lokasi_pabx = models.CharField(max_length=100)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_pabx ,self.lokasi_pabx)

# class networking(object):
# 	"""docstring for networking"""
# 	networking_id = models.AutoField(primary_key=True)
	

# 	def __init__(self, arg):
# 		super(networking, self).__init__()
# 		self.arg = arg
		

class mouse(models.Model):
	choose_jenis_mouse = (
		('OPTIK','OPTIK'),
		('BOLA','BOLA')		
	)
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_interface = (
		('PS2','PS2'),
		('USB','USB'),
		('WIRELESS','WIRELESS'),
		('SERIAL','SERIAL'),
	)

	mouse_id = models.AutoField(primary_key=True)
	merek_mouse = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	jenis_mouse = models.CharField(max_length=100, choices=choose_jenis_mouse, default='OPTIK')
	interface = models.CharField(max_length=100, choices=choose_interface, default='USB')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_mouse ,self.dipakai_pada_komputer)

class keyboard(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_interface = (
		('PS2','PS2'),
		('USB','USB'),
		('WIRELESS','WIRELESS'),
		('SERIAL','SERIAL'),
	)
	keyboard_id = models.AutoField(primary_key=True)
	merek_keyboard = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	interface = models.CharField(max_length=100, choices=choose_interface, default='USB')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_keyboard ,self.dipakai_pada_komputer)


class printer(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_interface = (
		('PS2','PS2'),
		('USB','USB'),
		('WIRELESS','WIRELESS'),
		('SERIAL','SERIAL'),
	)
	choose_tipe_printer = (
		('Deskjet','Deskjet'),
		('Inkjet','Inkjet'),
		('Laser','Laser'),
		('Monokrom','Monokrom'),
	)
	printer_id = models.AutoField(primary_key=True)
	merek_printer = models.CharField(max_length=100)
	tipe_printer = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	interface = models.CharField(max_length=100, choices=choose_interface, default='USB')
	tipe_tinta = models.CharField(max_length=100, choices=choose_tipe_printer, default='Inkjet')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_printer ,self.dipakai_pada_komputer)

class pesawat_telephone(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	pesawat_telephone_id = models.AutoField(primary_key=True)
	merek_pesawat_telephone = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	no_extention = models.CharField(max_length=100)
	lokasi_pesawat_telephone = models.CharField(max_length=100)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s - %s" % (self.merek_pesawat_telephone ,self.no_extention, self.lokasi_pesawat_telephone)

class monitor(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_tipe_monitor = (
		('Tabung','Tabung'),
		('LCD','LCD'),
		('LED','LED'),
	)

	choose_ukuran_monitor = (
		('14 Inch','14 Inch'),
		('15 Inch','15 Inch'),
		('16 Inch','16 Inch'),
		('17 Inch','17 Inch'),
		('18 Inch','18 Inch'),
		('19 Inch','19 Inch'),
	)

	choose_input_monitor = (
		('VGA','VGA'),
		('HDMI','HDMI'),
	)

	choose_tipe_power = (
		('AC','AC'),
		('Adaptor','Adaptor'),
	)

	monitor_id = models.AutoField(primary_key=True)
	merek_monitor = models.CharField(max_length=100)
	serial_number = models.CharField(max_length=100)
	tipe_monitor = models.CharField(max_length=100, choices=choose_tipe_monitor, default='LCD')
	ukuran_monitor = models.CharField(max_length=100, choices=choose_ukuran_monitor, default='14 Inch')
	input_monitor = models.CharField(max_length=100, choices=choose_input_monitor, default='VGA')
	tipe_power = models.CharField(max_length=100, choices=choose_tipe_power, default='AC')
	dipakai_pada_komputer =  models.ForeignKey('komputer',blank = True,null=True)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s" % (self.merek_monitor ,self.dipakai_pada_komputer)


class komputer(models.Model):
	choose_kondisi = (
		('OK','OK'),
		('RUSAK','RUSAK')		
	)
	choose_station = (
		('PC','PC'),
		('NComputing','NComputing'),
		('Laptop','Laptop')			
	)
	komputer_id = models.AutoField(primary_key=True)
	serial_number = models.CharField(max_length=100)
	tipe_komputer = models.CharField(max_length=100, choices=choose_station, default='PC')
	hostname = models.CharField(max_length=100)
	departement = models.CharField(max_length=100)
	pengguna = models.CharField(max_length=100)
	ip_address = models.CharField(max_length=100)
	mac_address =  models.CharField(max_length=100)
	kondisi = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
	catatan = models.CharField(max_length=255,blank = True,null=True)
	def __str__(self):
	 	return "%s - %s - %s - %s" % (self.departement ,self.pengguna, self.ip_address, self.hostname)

class merek(models.Model):
	merek_id = models.AutoField(primary_key=True)
	merek = models.CharField(max_length=100)

# class laptop(models.Model):
# 	choose_kondisi = (
# 		('OK','OK'),
# 		('RUSAK','RUSAK')		
# 	)
# 	choose_status = (
# 		('TERPASANG','TERPASANG'),
# 		('STOCK','STOCK'),
# 		('TIDAK ADA','TIDAK ADA'),
# 	)
# 	choose_ukuran_monitor = (
# 		('14 Inch','14 Inch'),
# 		('15 Inch','15 Inch'),
# 		('16 Inch','16 Inch'),
# 		('17 Inch','17 Inch'),
# 		('18 Inch','18 Inch'),
# 		('19 Inch','19 Inch'),
# 	)

# 	choose_kapasitas_storage = (
# 		('40Gb', '40Gb'),
# 		('80Gb', '80Gb'),
# 		('120Gb', '120Gb'),
# 		('250Gb', '250Gb'),
# 		('32Gb', '320Gb'),
# 		('500Gb', '500Gb'),
# 		('1Tb', '1Tb'),
# 		('2Tb', '2Tb'),
# 	)
# 	choose_kapasitas_memory = (
# 		('1Gb', '1Gb'),
# 		('2Gb', '2Gb'),
# 		('4Gb', '4Gb'),
# 		('8Gb', '8Gb'),
# 	)

# 	laptop_id = models.AutoField(primary_key=True)
# 	merek_laptop = models.ForeignKey('merek')
# 	tipe_laptop = models.CharField(max_length=100)
# 	serial_laptop = models.CharField(max_length=100)
# 	ukuran_layar = models.CharField(max_length=100, choices=choose_ukuran_monitor, default='14 Inch')
# 	kondisi_laptop = models.CharField(max_length=100, choices=choose_kondisi, default='OK')

# 	haridisk_laptop = models.CharField(max_length=100, choices=choose_kapasitas_storage, default='320 Gb')
# 	memory_laptop = models.CharField(max_length=100, choices=choose_kapasitas_memory, default='2 Gb')
	
# 	serial_baterai = models.CharField(max_length=100)
# 	kondisi_baterai = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
# 	status_baterai = models.CharField(max_length=100, choices=choose_status, default='OK')
	
# 	serial_adaptor = models.CharField(max_length=100)
# 	kondisi_adaptor = models.CharField(max_length=100, choices=choose_kondisi, default='OK')
# 	status_adaptor = models.CharField(max_length=100, choices=choose_status, default='OK')
		
# 	hostname = models.CharField(max_length=100)
# 	lokasi_penyimpanan =  models.CharField(max_length=100)

# 	catatan = models.CharField(max_length=255,blank = True,null=True)
# 	def __str__(self):
# 	 	return "%s - %s - %s" % (self.merek_laptop ,self.ukuran_layar, self.lokasi_penyimpanan)

