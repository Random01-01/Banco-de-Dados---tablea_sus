from django.contrib import admin
from .models import Medicamento, Doenca, Preco, Tratamento

admin.site.register(Medicamento)
admin.site.register(Doenca)
admin.site.register(Preco)
admin.site.register(Tratamento)