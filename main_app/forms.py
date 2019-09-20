from .models import Widget
from django.forms import ModelForm

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = '__all__'