from django.contrib import admin
from django.urls import path
from translator import views

urlpatterns = [
    path('morse_to_text/',views.morse_translator_view,name='morse to txt'),
    path('text_to_morse/',views.text_translator_view,name='text to morse')
]