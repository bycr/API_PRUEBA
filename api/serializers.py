from dataclasses import field, fields
from rest_framework import serializers
from api.models import User, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('documentId', 'documentName')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'Tipe_document', 'document', 'names', 'surnames', 'hobbie')