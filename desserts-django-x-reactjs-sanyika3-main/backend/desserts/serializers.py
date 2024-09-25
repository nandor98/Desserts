from rest_framework import serializers
from .models import Dessert,DesertCategory

class DessertSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = "__all__"
        
class DesertCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = DesertCategory
        fields = "__all__"
        depth = 1
