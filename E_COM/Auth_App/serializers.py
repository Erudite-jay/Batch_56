from rest_framework import serializers
from . models import Contact

#normal serializer
# class ContactSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     phone=serializers.CharField()
#     message=serializers.CharField()
    

#model serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'