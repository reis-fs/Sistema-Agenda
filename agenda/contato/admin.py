from django.contrib import admin
from agenda.contato.models import contato

class contatoAdmin(admin.ModelAdmin):
    model: contato
    list_display = ['contato_nome', 'contato_email', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(contato, contatoAdmin)

