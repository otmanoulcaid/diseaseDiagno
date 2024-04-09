import json
from django.http import JsonResponse
from diseasediagno.MachineLearning.predict import trained_model_prediction, symptoms

def post_request_managing(request):
    if request.method == 'POST':
        # data = request.POST  # If form data is sent in simple format (we get it as dictionary)
        data_json_str = request.body.decode('utf-8')
        # Convert the JSON string to a Python list
        data_list = json.loads(data_json_str)
        # print("Received data:", data_list) # for the moment
        return JsonResponse(trained_model_prediction(data_list))
        # return JsonResponse({'status': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

def getSymptoms(request):
    if request.method == 'GET':
        return JsonResponse(symptoms())
        # return JsonResponse({'status': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
