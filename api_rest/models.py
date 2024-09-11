from django.db import models

# arquivo que prepara dados para o banco de dados


class User(models.Model):

    # campo e propriedades do banco de dados
    # charfield define que é um campo de character
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default='')
    email = models.EmailField(default='', unique=True)
    genero = models.CharField(default='n', max_length=50)
    idade = models.IntegerField(default=0)
    senha = models.CharField(max_length=25)

    # metodo magico
    def __str__(self):
        return f"Nome: {self.nome} | E-mail: {self.email} | Genero: {self.genero} | idade: {self.idade}"


# para criar o modelo no banco de dados é py manage.py makemigrations, py manage.py migrate

class Produto(models.Model):

    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100, default='')
    descricao_produto = models.TextField(default='...')
    categoria_produto = models.CharField(max_length=100, default='eletronico')
    imagem_produto = models.CharField(default='', max_length=200, blank=True, null=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_produto = models.PositiveIntegerField()

    # metodo magico
    def __str__(self):
        return f"Produto: {self.nome_produto} | Categoria: {self.categoria_produto} | Preço: {self.preco_produto} | Quantidade: {self.estoque_produto}"


class Compra(models.Model):

    id_compra = models.AutoField(primary_key=True)
    # on_delete=models.CASCADE faz com que suma ao referenciado sumir
    user_compra = models.ForeignKey(User, on_delete=models.CASCADE)
    produto_compra = models.ForeignKey(Produto, on_delete=models.CASCADE)
    # garantir que o valor armazenado seja sempre um número inteiro não negativo.
    quantidade_compra = models.PositiveIntegerField()
    # auto_now_add=True preenche com data e hora automaticamente no registro
    data_compra = models.DateTimeField(auto_now_add=True)

    # metodo magico
    def __str__(self):
        return f" User_name: {self.user_compra.nome}  | Objeto: {self.produto_compra.nome_produto} | Quantidade: {self.quantidade_compra} |"
