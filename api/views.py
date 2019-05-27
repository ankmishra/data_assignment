from django.shortcuts import render
from .models import Api
from .serializers import ApiSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
# Create your views here.


class ApiList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    paginate_by = 5
    def get(self, request, format=None):
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        queryset = Api.objects.all()
        queryset = Api.objects.all()
        user = request.query_params.get('user', None)
        sort = request.query_params.get('sort', None)
        limit = int(request.query_params.get('limit', None))
        if user is not None:
            queryset = queryset.filter(first_name=user)
        if sort is not None:
             queryset = queryset.order_by(sort)
        if limit is not None:
            queryset = queryset[0:limit]

        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ApiSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = ApiSerializer(queryset, many=True)
        return Response(serializer.data)
        # if limit is not None:
        #     serializer = ApiSerializer(limit, many=True)
        #     return paginator.get_paginated_response(serializer.data)

        # # limit = paginator.paginate_queryset(queryset, request)
        # # serializer = ApiSerializer(limit, many=True)
        # # return paginator.get_paginated_response(serializer.data)
        # api = Api.objects.all()
        # serializer = ApiSerializer(api, many=True)
        # return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiDetail(APIView):
    """
    Retrieve, update or delete a api instance.
    """
    def get_object(self, pk):
        try:
            return Api.objects.get(pk=pk)
        except Api.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(api)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        api = self.get_object(pk)
        serializer = ApiSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        api = self.get_object(pk)
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)