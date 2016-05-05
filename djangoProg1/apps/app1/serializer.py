from rest_framework import serializers
from djangoProg1.apps.app1.models import Interview

class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = ("first_name", "second_name", "email", "text", "date")