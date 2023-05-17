from django import forms
from django.forms import ModelForm
from .models import *


class ItemCarritoForm(ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad', 'producto']