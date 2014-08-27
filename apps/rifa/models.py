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

ESTADO_CHOICES = (
	('activa','Activa'),
	('baja','Baja'),
)

ESTADO_SORTEO_CHOICES = (
	('vacante','Vacante'),
	('ganado','Ganado'),
)

TIPO_PREMIO = (
	('mensual','Mensual'),
	('1erfinal','1er Premio Final'),
	('2dofinal','2do Premio Final'),
	('3erfinal','3er Premio Final'),
)

class Persona(models.Model):
	usuario = models.ForeignKey(User, related_name='+')
	telefono = models.CharField(max_length=20, blank=True, help_text='Ej: 02221-452672')
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
		verbose_name_plural = 'personas'

class Comprador(models.Model):
	apellido = models.CharField(max_length=50, help_text='Ej: Fernandez Rodriguez')
	nombre = models.CharField(max_length=50, help_text='Ej: Santiago Osvaldo')
	dni = models.CharField(max_length=8, unique=True, help_text='Ej: 12345689')
	domicilio = models.CharField(max_length=100, blank=True, help_text='Ej: Barrio 22 de Febrero manzana 5 casa 10')
	telefono = models.CharField(max_length=20, blank=True, help_text='02221-452672')
	email = models.EmailField('e-mail', blank=True, help_text='Ej: info@scm.com.ar')
	socio = models.CharField(max_length=2, choices=SOCIO_CHOICES)
	observaciones = models.TextField(blank=True, help_text='Introduzca de ser necesario alguna observación')
	fecha_alta = models.DateTimeField(auto_now_add=True)
	creador = models.ForeignKey(Persona, editable=False, verbose_name='creador')

	def __unicode__(self):
		return '%s - %s - %s' % (self.apellido, self.nombre, self.dni)

	def save(self):
		self.apellido = self.apellido.lower()
		self.nombre = self.nombre.lower()
		self.dni = self.dni.lower()
		self.domicilio = self.domicilio.lower()
		self.telefono = self.telefono.lower()
		super(Comprador, self).save()

	class Meta:
		ordering = ['apellido', 'nombre', 'dni']
		verbose_name_plural = 'compradores'

class Rifa(models.Model):
	numero_uno = models.PositiveIntegerField('Numero uno', help_text='Ingrese numero sorteo')
	numero_dos = models.PositiveIntegerField(editable=False)
	observaciones = models.TextField(blank=True, help_text='Introduzca de ser necesario alguna observación')
	fecha_alta = models.DateTimeField(auto_now_add=True)
	creador = models.ForeignKey(Persona, editable=False, verbose_name='creador', related_name='+')
	cobrador = models.ForeignKey(Persona, editable=False, verbose_name='cobrador', related_name='+')
	comprador = models.ForeignKey(Comprador, verbose_name='comprador', related_name='+')
	estado = models.CharField(max_length=6, choices=ESTADO_CHOICES, default='activa')

	def __unicode__(self):
		return '%s - %s' % (str(self.numero_uno), str(self.numero_dos))

	def save(self):
		self.numero_dos = self.numero_uno + 500
		super(Rifa, self).save()

	class Meta:
		ordering = ['comprador', 'numero_uno']
		verbose_name_plural = 'rifas'

class Sorteo(models.Model):
	fecha_sorteo = models.DateField('Fecha del sorteo', help_text='Ej: 21/10/2014')
	tipo_premio = models.CharField('Tipo de premio', max_length=10, choices=TIPO_PREMIO)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	numero_sorteado = models.PositiveIntegerField('Numero sorteado', help_text='Ingrese numero sorteo')
	estado = models.CharField(max_length=7, choices=ESTADO_SORTEO_CHOICES)
	creador = models.ForeignKey(Persona, editable=False, verbose_name='creador')
	nombre = models.CharField(max_length=50, editable=False)
	apellido = models.CharField(max_length=50, editable=False)
	observacion = models.TextField(blank=True, help_text='Ingrese una observación de ser necesario')

	def __unicode__(self):
		return '%s - %d - %s' % (self.fecha_sorteo, self.numero_sorteo, self.estado)

	class Meta:
		ordering = ['fecha_sorteo', 'numero_sorteado']
		verbose_name_plural = 'sorteos'

class Pago(models.Model):
	fecha_alta = models.DateTimeField(auto_now_add=True)
	creador = models.ForeignKey(Persona, editable=False, related_name='+')
	fecha_pago = models.DateField('Fecha pago', help_text='21/08/2014')
	numero_cuota = models.PositiveIntegerField('Numero de cuota', help_text='Numero de couta a pagar')
	observaciones = models.TextField(help_text='Ingrese una observacion de ser necesaria')
	rifa = models.ForeignKey(Rifa)
	comprador = models.ForeignKey(Comprador, editable=False, verbose_name='comprador')
	cobrador = models.ForeignKey(Persona, editable=False, verbose_name='cobrador')

	def __unicode__(self):
		return '%s - %d - %s' % (self.fecha_pago, self.numero_cuota, self.rifa)

	class Meta:
		ordering = ['rifa', 'numero_cuota', 'fecha_pago']
		verbose_name_plural = 'pagos'

class Actividad(models.Model):
	observacion = models.CharField(max_length=150)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	persona = models.ForeignKey(Persona, verbose_name='persona')

	def __unicode__(self):
		return '%s - %s' % (self.fecha_alta, self.persona)

	class Meta:
		ordering = ['fecha_alta', 'persona']
		verbose_name_plural = 'actividades'
