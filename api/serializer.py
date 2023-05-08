from rest_framework import serializers
from todolist.models import *

class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'