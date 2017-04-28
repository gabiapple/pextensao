from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Alarme)
admin.site.register(Pessoa)
admin.site.register(UsuarioApp)
admin.site.register(Fechadura)
admin.site.register(Lampada)
admin.site.register(TipoDocumento)
admin.site.register(ControleLampada)
admin.site.register(HistoricoAlarme)
admin.site.register(AcessoFechadura)