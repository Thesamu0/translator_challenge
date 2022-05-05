from django.shortcuts import render
from django.views.defaults import bad_request
from django.core.exceptions import FieldError
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view


from .utils import morse_to_text,text_to_morse

# Create your views here.

@api_view(['POST'])
def morse_translator_view(request):
    received_string = JSONParser().parse(request)

    if 'morse' in received_string:
        if isinstance(received_string['morse'], str):
            translated = morse_to_text(received_string['morse'])
            return JsonResponse({'translated': translated}, status=status.HTTP_200_OK)

    return bad_request(request=request, exception=FieldError)


@api_view(['POST'])
def text_translator_view(request):
    received_string = JSONParser().parse(request)

    if 'text' in received_string:
        if isinstance(received_string['text'], str):
            translated = text_to_morse(received_string['text'])
            return JsonResponse({'translated': translated}, status=status.HTTP_200_OK)
    return bad_request(request=request, exception=FieldError)