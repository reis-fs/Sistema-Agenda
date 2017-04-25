from django.contrib import admin
from agenda.contato.models import contato, tarefa


class contatoAdmin(admin.ModelAdmin):

    model = contato
    list_display = ['contato_nome', 'contato_email', 'contato_estado_civil', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(contato, contatoAdmin)


class tarefaAdmin(admin.ModelAdmin):

    model = tarefa
    list_display = ['tarefa_nome', 'tarefa_data_inicio', 'concluido']
    search_fields = ['tarefa_nome']
    save_on_top = True
admin.site.register(tarefa, tarefaAdmin)
