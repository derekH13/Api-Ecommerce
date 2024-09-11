from django.contrib import admin
from .models import User, Produto, Compra


# logo depois de registrar tem que fazer um superUser
# Registra as tabelas que seram usadas do models
admin.site.register(User)
admin.site.register(Produto)
admin.site.register(Compra)
