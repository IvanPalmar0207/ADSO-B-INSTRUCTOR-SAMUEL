from django.contrib import admin
from usuariosGestion.models import tb_rol, tb_tpDocumento, tb_usuarios

# Register your models here.

admin.site.register(tb_rol)
admin.site.register(tb_tpDocumento)
admin.site.register(tb_usuarios)