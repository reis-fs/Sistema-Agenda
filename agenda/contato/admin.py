from django.contrib import admin
from agenda.contato.models import contato, tarefa, conta


class ContatoAdmin(admin.ModelAdmin):

    model = contato
    list_display = ['contato_nome', 'contato_email', 'contato_estado_civil', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(contato, ContatoAdmin)


class TarefaAdmin(admin.ModelAdmin):

    model = tarefa
    list_display = ['tarefa_nome', 'tarefa_data_inicio', 'concluido']
    search_fields = ['tarefa_nome']
    save_on_top = True
admin.site.register(tarefa, TarefaAdmin)


class ContaAdmin(admin.ModelAdmin):

    model = conta
    list_display = ['conta_nome', 'conta_data_vencimento', 'pago']
    search_fields = ['conta_nome']
    list_filter = ['pago']
    save_on_top = True
admin.site.register(conta, ContaAdmin)
