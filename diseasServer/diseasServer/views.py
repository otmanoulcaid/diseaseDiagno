from django.http import JsonResponse

def post_request_managing(request):
    if request.method == 'POST':
        # data = request.POST  # If form data is sent in simple format (we get it as dictionary)
        data_json_str = request.body.decode('utf-8')
        # Convert the JSON string to a Python list
        data_list = json.loads(data_json_str)
        # Process the received data here
        print("Received data:", data_list) # for the moment
        return JsonResponse({'status': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
