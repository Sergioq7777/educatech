#from rest_framework import generics
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import render

#from .models import *
#from .serializers import *
#from django.shortcuts import get_object_or_404

#class UsersList(generics.ListCreateAPIView):
#    queryset = Users.objects.all()
#    serializer_class = UsersSerializer

#    def get_object(self):
#        queryset = self.get_queryset()
#        obj = get_object_or_404(
#            queryset,
#            pk=self.kwargs['pk'],
#        )
#        return obj


#class ListVideo(APIView):
#    def get(self, request):
#        videos = Video.objects.all()
#        serializer_video = VideoSerializer(videos, many=True)
#        return Response(serializer_video.data)

#    def post(self, request):
#        serializer_video = VideoSerializer(data=request.data)
#        if serializer_video.is_valid():
#            serializer_video.save()
#            return Response(serializer_video.date, status=201)
#        return Response(serializer_video.erros, status=400)
