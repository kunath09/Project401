from rest_framework import serializers
from myapp.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'table_no', 'role')