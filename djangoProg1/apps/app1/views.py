from rest_framework import viewsets
from rest_framework.response import Response
from djangoProg1.apps.app1.serializer import InterviewSerializer, ListIntSerializer
from djangoProg1.apps.app1.models import Interview
from django.shortcuts import get_object_or_404

class InterviewViewSet(viewsets.ModelViewSet):
    model = Interview
    queryset = Interview.objects.all().order_by()
    serializer_class = InterviewSerializer

    def list(self, request, *args, **kwargs):
        data = self.get_queryset()
        return Response(ListIntSerializer(data, many=True).data)

    def create(self, request, *args, **kwargs):


    def retrieve(self, request, pk=None):
        queryset = Interview.objects.all()
        return Response(InterviewSerializer(get_object_or_404(queryset, pk=pk)).data)