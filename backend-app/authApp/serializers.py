from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from .models import CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    # Add your custom fields here
    phone_number = serializers.CharField(max_length=15, required=True)
    role = serializers.ChoiceField(choices=[('client', 'Client'), ('worker', 'Worker')], required=True)
    national_id = serializers.CharField(max_length=20, required=False)

    def get_cleaned_data(self):
        """Extract data from the serializer to pass to the adapter"""
        data = super().get_cleaned_data()
        data['phone_number'] = self.validated_data.get('phone_number', '')
        data['role'] = self.validated_data.get('role', 'client')
        data['national_id'] = self.validated_data.get('national_id', '')
        return data
    
    @transaction.atomic
    def save(self, request):
        """
        Overriding the save method as required by dj-rest-auth docs.
        This method must return the user instance.
        """
        # Call the parent save method which handles user creation via allauth
        user = super().save(request)
        
        # 2. Add your custom logic to populate the CustomUser fields
        user.phone_number = self.validated_data.get('phone_number')
        user.role = self.validated_data.get('role')
        user.national_id = self.validated_data.get('national_id')
        
        # 3. Save the updated user instance
        user.save()
        
        # 4. Return the instance as per the docs requirement
        return user

class CustomLoginSerializer(LoginSerializer):
    # We replace 'username' with 'phone_number'
    username = None  # Remove default username
    phone_number = serializers.CharField(required=True)

    def get_fields(self):
        fields = super().get_fields()
        # Ensure 'username' is not in the fields at all
        fields.pop('username', None)
        return fields

    def validate(self, attrs):
        # Map 'phone_number' back to 'username' so the 
        # internal Django authentication backend can process it.
        attrs['username'] = attrs.get('phone_number')
        return super().validate(attrs)
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'phone_number', 'email', 'role', 'is_verified')
        read_only_fields = ('phone_number', 'role')
