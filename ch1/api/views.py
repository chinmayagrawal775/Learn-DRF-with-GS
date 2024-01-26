from django.shortcuts import render
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    stu = Student.objects.get(pk=1)
    stu_many = Student.objects.all()

    serialized_data = StudentSerializer(stu)
    serialized_data_many = StudentSerializer(stu_many, many=True)

    json_data = JSONRenderer().render(serialized_data.data)
    json_data_many = JSONRenderer().render(serialized_data_many.data)
    # return HttpResponse(json_data, content_type='application/json')
    # return HttpResponse(json_data_many, content_type='application/json')

    # return JsonResponse(serialized_data.data)
    return JsonResponse(serialized_data_many.data, safe=False)

@csrf_exempt
def stu_create(request):
    if(request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save()
            res = {'msg':'data inserted'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)