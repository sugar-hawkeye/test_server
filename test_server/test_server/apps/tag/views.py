from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Tag
from .serializers import TagSerializer

############# regular Django views

# @csrf_exempt
# def tag_list(request):
#     if request.method == 'GET':
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TagSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
# @csrf_exempt
# def tag_detail(request, pk):
#
#     try:
#         tag = Tag.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = TagSerializer(tag)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TagSerializer(tag, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         tag.delete()
#         return HttpResponse(status=204)





############  function-based views

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET', 'POST'])
# def tag_list(request, format=None):
#     if request.method == 'GET':
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tag_detail(request, pk, format=None):
#     try:
#         tag = Tag.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TagSerializer(tag,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





######### class-based views

from rest_framework.views import APIView
#
#
# class TagList(APIView):
#
#     def get(self, request, format=None):
#         tag = Tag.objects.all()
#         serializer = TagSerializer(tag, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TagDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Tag.objects.get(pk=pk)
#         except:
#             return Response(status.HTTP_404_NOT_FOUND)
#
#
#     def get(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






########### Using Mixins

from rest_framework import mixins
from rest_framework import generics

# class TagList(mixins.ListModelMixin,
#               mixins.CreateModelMixin,
#               generics.GenericAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, kwargs)
#
#
#
# class TagDetail(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




########## using generic class-based views
#
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
#
# class TagList(generics.ListCreateAPIView):
#     """
#         get:
#         返回所有的tag
#
#         post:
#         创建一个新的tag
#     """
#
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class TagDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
#
#
#
#
#
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
#
# from rest_framework.reverse import reverse
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'tags': reverse('tag-list', request=request, format=format)
#     })
#






############ ViewSet

# from rest_framework import viewsets
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class TagViewSet(viewsets.ModelViewSet):

#
#
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)




######## query url


class TagList(APIView):

    def get(self, request, format=None):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(APIView):

    def get_object(self,is_publish,priority):
        try:
            return Tag.objects.filter(is_publish=is_publish,priority=priority)
        except:
            return Response(status.HTTP_404_NOT_FOUND)


    def get(self, request, format=None):
        tags = self.get_object(self.request.query_params['is_publish'],self.request.query_params['priority'])
        serializer = TagSerializer(tags,many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        tag = self.get_object(self.request.query_params['tagid'])
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        tag = self.get_object(self.request.query_params['tagid'])
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)