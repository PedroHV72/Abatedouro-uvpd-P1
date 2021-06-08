from rest_framework import serializers

from aplic.models import Funcionario, Revendedora, Galeria, Produto, Pedido


class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = '__all__'


class RevendedoraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Revendedora
        fields = '__all__'


class GaleriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Galeria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = '__all__'

