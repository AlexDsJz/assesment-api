from app.models import Process, User
from django.shortcuts import get_object_or_404
from domain.algorithm import characters_uniques, decimal_to_roman

def create_process(decimal, user_id):
    user = get_object_or_404(User, pk = user_id)
    numberConverted = str(decimal_to_roman(decimal))
    
    process = Process.objects.create(input = decimal, result = numberConverted, user = user)
    process.save()
    
    return numberConverted


def get_characters(id):
    process = get_object_or_404(Process, pk = id)
    characters = characters_uniques(process.result)
    return characters