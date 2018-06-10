from .models import Post, Lang
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostDetailSerializer, LangDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class PostApiView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    def put(self, request):
        serializer = PostDetailSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PostDetaokAPIView(APIView):
    def get(self, request, pk):
        query = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(query)
        return Response(serializer.data)
    def delete(self, request, pk):
        query = get_object_or_404(Post, pk=pk)
        query.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class LangApiView(APIView):
    def get(self, request):
        queryset = Lang.objects.all()
        serializer = LangDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    def put(self, request):
        serializer = LangDetailSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LangDetaokAPIView(APIView):
    def get(self, request, pk):
        query = get_object_or_404(Lang, pk=pk)
        serializer = LangDetailSerializer(query)
        return Response(serializer.data)
    def delete(self, request, pk):
        query = get_object_or_404(Lang, pk=pk)
        query.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




