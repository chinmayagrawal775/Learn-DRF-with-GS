from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

# Create your views here.

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if(id is not None):
            stu = Student.objects.get(pk=id)
            serialize = StudentSerializers(stu)
            return Response(serialize.data)
        stu = Student.objects.all()
        serialize = StudentSerializers(stu, many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Entry Created'})
        return Response(serializer.errors)
    
    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Entry Updated'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'Partial Entry Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Entry Deleted'})