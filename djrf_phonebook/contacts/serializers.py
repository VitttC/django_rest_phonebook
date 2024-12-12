from rest_framework import serializers
from django.contrib.auth.models import User

from contacts.models import Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'contacts']


class ContactSerializer(serializers.ModelSerializer):
    """
    Expliciting which fields are required
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    first_name =   serializers.CharField(required=True, allow_blank=False, max_length=30)
    phone_number = serializers.CharField(required=True, allow_blank=False, max_length=10)

    class Meta:
        model = Contact
        fields = ['url','id', 'first_name', 'last_name', 'country_code', 'phone_number']

    def create(self, validated_data):
        """
        Create and return a new "Contact" instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing "Contact" instance.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)   
        instance.save()
        return instance
    
