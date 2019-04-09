from django import forms
from .models import Instagram, transisi, tujuan, gudangracking, status_product, productperpalet

class productperpaletform(forms.ModelForm):
	class Meta:
		model = productperpalet
		fields = '__all__'

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
		fields = [
			'product_per_palet',
			'status_perpindahan',
			'pengguna'
			#'update_time'
		]

		widgets = {
			'product_per_palet' : forms.Select(
				attrs = {
					# 'hidden':'hidden'
				}
				)
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
		widgets = {
			'blok' : forms.Select(
				attrs = {
					# 'hidden':'hidden'
				}
				)
		}
