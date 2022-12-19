from rest_framework import serializers
from seminarioAPP.models import seminario,institucion

class SeminarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = seminario
        fields = '__all__'