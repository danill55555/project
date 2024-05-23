import re
from django.core.exceptions import ValidationError

def validate_cyrillic(value):
    if not re.match('^[а-яА-ЯЁё\s]+$', value):
        raise ValidationError('Введенные данные должны содержать только кириллические символы и пробелы.')


def validate_telephone(value):
    if not re.match(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', value):
        raise ValidationError("Телефон должен быть в формате +7(XXX)-XXX-XX-XX")
