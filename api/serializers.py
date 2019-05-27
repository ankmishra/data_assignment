from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('id', 'first_name', 'last_name', 'company_name', 'email', 'city','state','web','age','zip')