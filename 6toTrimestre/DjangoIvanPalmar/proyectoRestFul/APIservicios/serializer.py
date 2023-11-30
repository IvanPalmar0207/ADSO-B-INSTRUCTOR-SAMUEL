from rest_framework import serializers
from APIservicios.models import tb_categoria, tb_servicio, tb_consumo

class tb_categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_categoria
        fields = '__all__'
        
class tb_servicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_servicio
        fields = '__all__'
        
class tb_consumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tb_consumo
        fields = '__all__'