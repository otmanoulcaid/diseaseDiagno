from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Jus
from django.http import JsonResponse
from .serializers import JusSerializer

@api_view(['GET', 'POST'])
def	jus_lister(request):
	if request.method == 'GET':
		jus = Jus.objects.all()
		ser = JusSerializer(jus, many=True)
		return JsonResponse({"items" : ser.data}, status=status.HTTP_200_OK)
	if request.method == 'POST':
		serializer = JusSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

