from rest_framework import serializers
from .models import Jus


class JusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Jus
		fields = ['id','name', 'description']

