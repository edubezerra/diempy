from django.core.exceptions import ValidationError
from pycpfcnpj import cpfcnpj


def validate_cnpj(value):
    if not cpfcnpj.validate(value):
        raise ValidationError('CNPJ inválido')