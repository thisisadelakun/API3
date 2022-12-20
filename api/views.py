from django.shortcuts import render
from rest_framework.decorators import api_view
# from django.http import Response
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    course={
        'Python Fullstack'
    }

    return Response(course)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)  
    return Response(serializer.data)  

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data) 

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(data=request.data, instance=task)  
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('item deleted!!!')

