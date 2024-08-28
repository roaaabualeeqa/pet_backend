from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pet
        fields = '__all__' # to get the id in the frontend
        # fields = ('name', 'owner', 'des', 'breed', 'birth_date')