from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if(request.method == 'GET'):
        id = pk
        if(id is not None):
            stu = Student.objects.get(pk=id)
            serialize = StudentSerializers(stu)
            return Response(serialize.data)
        stu = Student.objects.all()
        serialize = StudentSerializers(stu, many=True)
        return Response(serialize.data)

    if(request.method == 'POST'):
        serializer = StudentSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Entry Created'})
        return Response(serializer.errors)

    if(request.method == 'PUT'):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Entry Updated'})
        return Response(serializer.errors)

    if(request.method == 'PATCH'):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Partial Entry Updated'})
        return Response(serializer.errors)

    if(request.method == 'DELETE'):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Entry Deleted'})