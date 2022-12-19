from django.contrib import admin
from seminarioAPP.models import seminario
# Register your models here.

class SeminarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombreR', 'telefono','institucion', 'fechareserva','estado', 'observacion']

admin.site.register(seminario, SeminarioAdmin)