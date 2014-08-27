from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^comprador/agregar/', 'apps.rifas.views.agregarComprador', name='rifas_agregar_comprador'),
	url(r'^vendedor/agregar/', 'apps.rifas.views.agregarVendedor', name='rifas_agregar_vendedor'),
	url(r'^rifa/agregar/', 'apps.rifas.views.agregarRifa', name='rifas_agregar_rifa'),
	url(r'^compradores/', 'apps.rifas.views.todosCompradores', name='rifas_ver_todos'),
	url(r'^mis-compradores/', 'apps.rifas.views.misCompradores', name='rifas_mis_compradores'),
	url(r'^mis-vendedores/', 'apps.rifas.views.misVendedores', name='rifas_mis_vendedores'),
	url(r'^vendedores/', 'apps.rifas.views.todosVendedores', name='rifas_compradores_todos'),
	url(r'^cobrador/agregar/', 'apps.rifas.views.agregarCobrador', name='rifas_agregar_cobrador'),
	url(r'^cobradores/', 'apps.rifas.views.todosCobradores', name='rifas_cobradores_ver_todos'),
	url(r'^pagos/agregar/', 'apps.rifas.views.agregarPago', name='rifas_agregar_pago'),
	url(r'^pagos/', 'apps.rifas.views.todosPagos', name='rifas_pagos_todos'), 
	url(r'^rifas/', 'apps.rifas.views.todasRifas', name='rifas_rifas_todas'),
	url(r'^premios/agregar/', 'apps.rifas.views.agregarPremio', name='rifas_agregar_premio'),
	url(r'^ganadores/', 'apps.rifas.views.todosGanadores', name='rifas_ganadores_todos'),
	url(r'^ganador/(?P<id>[-\d]+)/$', 'apps.rifas.views.datosGanador', name='rifas_datos_ganador'),
	url(r'^mis-pagos/', 'apps.rifas.views.misPagos', name='rifas_mis_pagos'),
	url(r'^mis-compradores/', 'apps.rifas.views.misCompradores', name='rifas_mis_compradores'),
	# Dirigentes
	url(r'^dirigente/agregar/', 'apps.rifas.views.agregarDirigente', name='rifas_agregar_dirigente'),
)