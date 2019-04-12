from django import forms
from .models import Instagram, transisi, tujuan, gudangracking, status_product, productperpalet, product

class productperpaletform(forms.ModelForm):
	class Meta:
		model = productperpalet
		fields = '__all__'
		widgets = {
			'tanggal_produksi' : forms.TextInput(
				attrs = {
					'readonly':'readonly'
				}
				),
			'pengguna' : forms.Select(
				attrs = {
					'class':'form-control m-input m-input--square'
				}
				),
			'kode_product' : forms.Select(
				attrs = {
					'class':'form-control m-input m-input--square'
				}
				)
		}


class productform(forms.ModelForm):
	class Meta:
		model = product
		fields = '__all__'
		widgets = {
			'update_time' : forms.TextInput(
				attrs = {
					'readonly':'readonly'
				}
				),
			'pengguna' : forms.Select(
				attrs = {
					'class':'form-control m-input m-input--square'
				}
				),
		}

class InstagramForm(forms.ModelForm):
	class Meta:
		model = Instagram
		fields =[
			'nama_depan',
			'nama_belakang',
			'username',
		]

class transisiform(forms.ModelForm):
	class Meta:
		model = transisi
		fields = '__all__'
		labels = {
			"status_perpindahannya":"Lokasi product"
		}

class lokasi_product_form(forms.ModelForm):
	class Meta:
		model = transisi
		fields = '__all__'

		labels = {
			"status_perpindahanya":"Lokasi product"
		}

class status_product_form(forms.ModelForm):
	class Meta:
		model  = status_product
		fields = [
			'product_per_palet',
			'status_product',
			'pengguna'
		]

		
		
class gudangrackingform(forms.ModelForm):
	class Meta:
		model = gudangracking
		fields = [
			'product_per_palet',
			'blok',
			'tingkat',
			'lorong',
			'baris',
			'pengguna'
		]
		
