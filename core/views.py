from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Prompt
from .serializers import PromptSerializer
from .tasks import generate_text


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        generate_text.delay(serializer.instance.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
