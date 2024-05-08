import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MachineLearning.predict import trained_model_prediction, symptoms, Description

def predict(request):
    if request.method == 'POST':
        data_json_str = request.body.decode('utf-8')
        # Convert the JSON string to a Python list
        data_list = json.loads(data_json_str)
        prediction = trained_model_prediction(data_list) #call the predictif model
        object_result = {
            'condition' : prediction[0],
            'description' : Description(prediction[0])[0]
        }
        return JsonResponse(object_result, safe=False)
    return JsonResponse(['Only POST requests are allowed'], safe=False)

@csrf_exempt
def getSymptoms(request):
    if request.method == 'GET':
        result = symptoms()
        return JsonResponse(result, safe=False)
    return JsonResponse(['Only GET requests are allowed'])

@csrf_exempt
def getDescription(request, ds):
    if ds is None:
        return JsonResponse(['you should pass a condition as an argument'])
    if request.method == 'GET':
        result = Description(ds)
        return JsonResponse(result, safe=False)
    return JsonResponse(['Only POST requests are allowed'])

@csrf_exempt
def getfiltredData(request):
    if request.method == 'GET':
        data = {
            'skin' : ['nta', 'ras', 'lgr3a'],
            'exemple' : ['khod', 'hadi', 'exemple']
            'php' : ['MVC', 'login', 'les regle']
        }
        return JsonResponse(result, safe=False)
    return JsonResponse(['Only POST requests are allowed'])
