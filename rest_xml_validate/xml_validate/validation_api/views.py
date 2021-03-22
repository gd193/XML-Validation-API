from validation_api.serializers import MetaDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from validation_api.parsers import PlainTextParser
from validation_api.models import MetaData
# Create your views here.


class AddMetaDataView(APIView):
    queryset = MetaData.objects.all()
    parser_classes = (PlainTextParser, )

    def post(self, request, version):
        request.data.update({'version': version})
        serializer = MetaDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['data'], status=status.HTTP_201_CREATED)
        else:
            if 'version' in serializer.errors and serializer.errors['version'][0].code == 404:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateMetaDataView(APIView):
    queryset = MetaData.objects.all()
    parser_classes = (PlainTextParser, )

    def post(self, request, version):
        request.data.update({'version': version})
        serializer = MetaDataSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data['data'], status=status.HTTP_200_OK)
        else:
            if 'version' in serializer.errors and serializer.errors['version'][0].code == 404:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)