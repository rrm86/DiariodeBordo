from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated','trecord','category')#Tabela Principal
    list_filter = ('created','updated','category')#Tabela dos Filtros
    search_fields = ('title', 'body')#Não está funcionando corretamente
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Record, RecordAdmin)
