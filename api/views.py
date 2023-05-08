from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from todolist.models import *
# Create your views here.
@api_view(['GET'])
def tasklist(request):
    tasks = task.objects.all()
    serializer = todoserializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskl(request,pk):
    tasks = task.objects.get(id=pk)
    serializer = todoserializer(tasks)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = todoserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    tasks = task.objects.get(id=pk)
    serializer = todoserializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    tasks = task.objects.get(id=pk)
    tasks.delete()