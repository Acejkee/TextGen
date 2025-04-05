from rest_framework import serializers

from .models import Prompt, PromptContent


class PromptContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptContent
        fields = '__all__'


class PromptSerializer(serializers.ModelSerializer):
    content = PromptContentSerializer(read_only=True)

    class Meta:
        model = Prompt
        fields = '__all__'
