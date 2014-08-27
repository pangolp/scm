# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

ROL_CHOICES = (
	('administrador','Administrador'),
	('cobrador','Cobrador'),
	('dirigente','Dirigente'),
	('vendedor','Vendedor'),
)

SOCIO_CHOICES = (
	('si','Si'),
	('no','No'),
)

class Persona(models.MODEL):
	usuario = models.ForeignKey(User)
	telefono = models.CharField('telefono de contacto', max_length=20, blank=True, help_text='Ej: 02221-452672')
	rol = models.CharField(max_length=15, choices=ROL_CHOICES, help_text='Rol de usuario')
	creador = models.ForeignKey(User, editable=False, verbose_name='creador')
	fecha_alta = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s %s' % (self.rol, self.usuario)

	def save(self):
		self.telefono = self.telefono.lower()
		super(Persona, self).save()

	class Meta:
		ordering = ['rol', 'usuario']
		unique_together = ('usuario', 'rol')
		verbose_name_plural = 'persona'

class Comprador(models.MODEL):
	apellido = models.CharField(max_length=50, help_text='Ej: Fernandez Rodriguez')
	nombre = models.CharField(max_length=50, help_text='Ej: Santiago Osvaldo')
	dni = models.CharField(max_length=8, unique=True, help_text='Ej: 12345689')
	domicilio = models.CharField(max_length=100, blank=True, help_text='Ej: Barrio 22 de Febrero manzana 5 casa 10')
	telefono = models.CharField(max_length=20, blank=, help_text='02221-452672')
	email = models.EmailField('e-mail', blank=True, help_text='Ej: info@scm.com.ar')
	socio = models.CharField(max_length=2, choices=SOCIO_CHOICES)
	observaciones = models.TextField(help_text='Introduzca de ser necesario alguna observación')
	fecha_alta = models.DateTimeField(auto_now_add=True)
	creador = models.ForeignKey(Persona, editable=False, verbose_name='creador')

	def __unicode__(self):
		return '%s, %s - %s' % (self.apellido, self.nombre, self.dni)

	def save(self):
		self.apelldo = self.apelldo.lower()
		self.nombre = self.nombre.lower()
		self.dni = self.dni.lower()
		self.domicilio = self.domicilio.lower()
		self.telefono = self.telefono.lower()
		super(Comprador, self).save()

	class Meta:
		ordering = ['apellido', 'nombre', 'dni']
		verbose_name_plural = 'compradores'

class Rifa(models.MODEL):
	numero_uno = models.PositiveIntegerField(help_text='Ej: 0 - 499')
	numero_dos = models.PositiveIntegerField(editable=False)
	observaciones = models.TextField(help_text='Introduzca de ser necesario alguna observación')
	fecha_alta = models.DateTimeField()
	creador = models.ForeignKey(User, editable=False, verbose_name='creador')
	cobrador = models.ForeignKey(Persona, editable=False, verbose_name='cobrador')
	comprador = models.ForeignKey(Comprador, verbose_name='comprador')

	def __unicode__(self):
		return '%d %d' % (self.numero_uno, self.numero_dos)