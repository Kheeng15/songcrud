from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializers, SongSerializers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class_based views
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

class Artiste_listAPIView(APIView):
    def get(self, request):
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializers(artiste, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArtisteSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Artiste_detailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Artiste.objects.get(pk=id)
       
        except Artiste.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        artiste = self.get_object(id)
        serializer = ArtisteSerializers(artiste)
        return Response(serializer.data)
    
    def put(self, request, id):
        artiste = self.get_object(id)
        serializer = ArtisteSerializers(artiste, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        artiste = self.get_object(id)
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class Song_listAPIView(APIView):
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializers(song, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #song = Song.objects.all()
        serializer = SongSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Song_detailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Song.objects.get(pk=id)
       
        except Song.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializers(song)
        return Response(serializer.data)
    
    def put(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializers(song, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        song = self.get_object(id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


