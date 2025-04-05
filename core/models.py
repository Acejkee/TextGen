from django.db import models


class Prompt(models.Model):
    PENDING = 'PENDING'
    PROCESSING = 'PROCESSING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),

    ]

    title = models.CharField(max_length=255)
    input_text = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PromptContent(models.Model):
    prompt = models.OneToOneField(Prompt, on_delete=models.CASCADE, related_name='content')
    output_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
