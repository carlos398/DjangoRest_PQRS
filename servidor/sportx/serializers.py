from rest_framework import serializers
from .models import PQRS

class PqrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQRS
        fields = '__all__'
        fields = ('id', 'identification', 'identification_type', 'name', 'last_name', 'movil', 'phone', 'email', 'title', 'description', 'status', 'created_at')

