
from .models import RequestModel
from django import forms


class RequestForm(forms.ModelForm):
  class Meta:
    model = RequestModel
    fields = '__all__'