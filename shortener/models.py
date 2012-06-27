from django.db import models
from django import forms

from shortener.associator import Associator

associator = Associator()

class URLAssociation(models.Model):
	global associator
	actual_url = models.URLField()
	created = models.DateTimeField(auto_now_add=True)

	def code(self):
		return associator.encode(self.pk)

	@staticmethod
	def get_from_code(code):
		return URLAssociation.objects.get(pk=associator.decode(code))

class URLForm(forms.ModelForm):
	class Meta:
		model = URLAssociation
