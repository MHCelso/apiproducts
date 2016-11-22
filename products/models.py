from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=45, verbose_name='nombre')
	mark = models.CharField(max_length=45, verbose_name='marca')
	price = models.PositiveIntegerField(verbose_name='precio')
	provider = models.CharField(max_length=45, verbose_name='proveedor')
	image = models.ImageField(upload_to = 'pict_folder/', verbose_name='imagen')
	def __unicode__(self):
		return self.name


