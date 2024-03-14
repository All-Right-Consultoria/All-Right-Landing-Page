from django.contrib import admin
from .models import Case, Depoimento, CadastroHomePage

# Register your models here.
admin.site.register(Case)
admin.site.register(Depoimento)
admin.site.register(CadastroHomePage)