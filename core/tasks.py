from openai import OpenAI
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Prompt, PromptContent

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=settings.OPENAI_API_KEY,
)


@shared_task
def generate_text(prompt_id):
    prompt = Prompt.objects.get(pk=prompt_id)
    prompt.status = Prompt.PROCESSING
    prompt.save()

    try:
        response = client.chat.completions.create(
            model="qwen/qwen2.5-vl-3b-instruct:free",  # Или другая подходящая модель
            messages=[
                {"role": "user", "content": prompt.input_text}
            ],
        )

        output_text = response.choices[0].message.content.strip()
        print(output_text)

        PromptContent.objects.create(prompt=prompt, output_text=output_text)
        prompt.status = Prompt.COMPLETED
        prompt.save()

        send_mail(
            'Your generated text',
            output_text,
            settings.DEFAULT_FROM_EMAIL,
            ['example@example.ru'],
            fail_silently=False,
        )

    except Exception as e:
        prompt.status = Prompt.FAILED
        prompt.save()
        print(f"Error generating text: {e}")
