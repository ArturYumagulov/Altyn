import os
import django

from django.conf import settings
import datetime
import io

from django.core.mail import EmailMessage
from docxtpl import DocxTemplate

# Устанавливаем переменную окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'altyn.settings')

# Инициализируем Django
django.setup()

# Теперь можно импортировать модели и использовать настройки


# Используем модели и настройки
contract_legal_path = os.path.join(settings.BASE_DIR, 'contract/contract_legal.docx')
contract_individual_path = os.path.join(settings.BASE_DIR, 'contract/contract_individual.docx')
contract_empty_path = os.path.join(settings.BASE_DIR, 'contract/contract_empty.docx')


def send_word_via_email(typing, context=None, movie_name="", email=""):
    # Открываем шаблон документа
    if typing == 'legal':
        doc = DocxTemplate(contract_legal_path)
        doc.render(context)
    elif typing == 'individual':
        doc = DocxTemplate(contract_individual_path)
        doc.render(context)
    else:
        doc = DocxTemplate(contract_empty_path)

    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    email = EmailMessage(
        subject='Ваш документ Word',
        body='Пожалуйста, найдите вложение с вашим документом.',
        from_email=settings.EMAIL_HOST_USER,  # Ваш email
        to=[f"{email}"]  # Получатель письма
    )

    email.attach(f'договор_на_фильм_{movie_name}.docx', file_stream.getvalue(),
                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')

    # Отправляем письмо
    if email.send():
        return True
    return False



