from telnetlib import STATUS
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#modelos y serializers
from api.models import User, Document
from api.serializers import UserSerializer, DocumentSerializer


@csrf_exempt
def DocumentAPi(request, id = 0):
    if request.method == 'GET':
        documents = Document.objects.all()
        documents_Serializer = DocumentSerializer(documents, many=True)
        response = JsonResponse(documents_Serializer.data, safe=False)
        return response
    elif request.method == 'POST':
        document_data = JSONParser().parse(request)
        documents_Serializer = DocumentSerializer(data=document_data)
        if documents_Serializer.is_valid():
            documents_Serializer.save()
            return JsonResponse("Agregado correctamente", safe=False)
    elif request.method == "PUT":
        document_data = JSONParser().parse(request)
        document = Document.objects.get(documentId=document_data['documentId'])
        documents_Serializer = DocumentSerializer(document, data=document_data)
        if documents_Serializer.is_valid():
            documents_Serializer.save()
            return JsonResponse("Actulizado correctamente", safe=False)
    elif request.method == 'DELETE':
        document = Document.objects.get(documentId=id)
        document.delete()
        return JsonResponse("Eliminado correctamente", safe=False)
    
    
    
@csrf_exempt
def UserAPi(request, id = 0):
    if request.method == 'GET':
        users = User.objects.all()
        users_Serializer = UserSerializer(users, many=True)
        response = JsonResponse(users_Serializer.data, safe=False)
        return response
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_Serializer = UserSerializer(data=user_data)
        if users_Serializer.is_valid():
            users_Serializer.save()
            return JsonResponse("Agregado correctamente", safe=False)
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data['userId'])
        users_Serializer = UserSerializer(user, data=user_data)
        if users_Serializer.is_valid():
            users_Serializer.save()
            return JsonResponse("Actulizado correctamente", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("Eliminado correctamente", safe=False)