from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Produto, Compra
from .serializers import UserSerializer, ProdutoSerializer, CompraSerializer

import json

# consulta de todos os usuarios


@api_view(['GET'])
def get_user(request):  # recebe o request

    if request.method == 'GET':
        users = User.objects.all()  # função para devolver user

        # serializa transform querySet (json), mais de um objeto many=True
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# busca por genero
@api_view(['GET'])
def get_genero(request, gnr):

    if request.method == 'GET':

        genero_busca = User.objects.filter(genero=gnr)
        serializer = UserSerializer(genero_busca, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# consulta de todos os produtos
@api_view(['GET'])
def get_produto(request):

    if request.method == 'GET':
        produto = Produto.objects.all()

        # mais de um produto tem que colocar many=True
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_categoria(request, categoria):

    if request.method == 'GET':
        sep_categoria = Produto.objects.filter(categoria_produto=categoria)

        serializar = ProdutoSerializer(sep_categoria, many=True)
        return Response(serializar.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# consulta de todas as compras
@api_view(['GET'])
def get_compra(request):

    if request.method == 'GET':
        compra = Compra.objects.all()

        serializer = CompraSerializer(compra, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# crud de usuarios
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def crud_usuario(request):

    if request.method == 'GET':

        try:
            # pega o valor de user passado na url
            if request.GET['user']:
                user_name = request.GET['user']

                try:
                    # se retoranar verdadeiro (algo)
                    user = User.objects.filter(nome=user_name)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # criação de usuario
    if request.method == 'POST':

        # pega o objeto inteiro passado pelo request
        new_user = request.data

        # por serializar não serializar objeto e sim, dados tem que ter data=
        serializer = UserSerializer(data=new_user)

        # is_valid verifica se os dados são validos para salvar
        if serializer.is_valid():
            serializer.save()  # salvar no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # edição de usuario
    if request.method == 'PUT':

        # vendo o id que quer mudar'
        idBusca = request.data['id']
        nick = User.objects.get(pk=idBusca)

        # por ser uma edição usa o 1 parametro para o obejeto original e o 2 para o que quer add
        serializer = UserSerializer(nick, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # deletar usuario
    if request.method == 'DELETE':

        try:
            # tenta fazer a busca no banco de dados pelo id do request
            delte_user = User.objects.get(id=request.data['id'])
            delte_user.delete()

            return Response(status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# crud de produtos
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def crud_produto(request):

    if request.method == 'GET':
        try:

            if request.GET['produto']:
                produto_busca = request.GET['produto']

                try:
                    produto = Produto.objects.filter(
                        nome_produto=produto_busca)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                # coloca many por ser mais de um
                serializer = ProdutoSerializer(produto, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # criação de produtos
    if request.method == 'POST':

        # por não ser objeto, ser dados tem que colocar data
        serializer = ProdutoSerializer(data=request.data)

        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # edição de produto
    if request.method == 'PUT':

        edit_id = request.data['id_produto']
        produto = Produto.objects.get(id_produto=edit_id)

        print(produto)

        serializer = ProdutoSerializer(produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete de produto
    if request.method == 'DELETE':
        try:
            produto_del = Produto.objects.get(
                id_produto=request.data['id_produto'])
            produto_del.delete()
            produto_id = request.data.get('id_produto')
            return Response(f'Produto id: {produto_id} excluido', status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# crud compra
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def crud_compra(request):

    if request.method == 'GET':
        try:
            # procura compra e verifica se ele tem valor
            if request.GET['compra']:
                idCompra = request.GET['compra']

                try:
                    # procurar/ pode dar errado
                    compra = Compra.objects.get(pk=idCompra)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializar = CompraSerializer(compra)
                return Response(serializar.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # para criar uma compra
    if request.method == 'POST':

        # por não ser um objeto ser dados, tem que colocar data=
        serializar = CompraSerializer(data=request.data)

        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)

        return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)

    # ediação de compra
    if request.method == 'PUT':

        edit_id = request.data['id_compra']
        compra = Compra.objects.get(id_compra=edit_id)

        serializar = CompraSerializer(compra, data=request.data)

        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # delete compra
    if request.method == 'DELETE':
        try:
            compra_del = Compra.objects.get(
                id_compra=request.data['id_compra'])
            compra_del.delete()
            result = request.data['id_compra']
            return Response(f'Compra id {result} excluido', status=status.HTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
