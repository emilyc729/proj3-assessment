from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum


# Create your views here.
def home(request):
    widget_list = Widget.objects.all()
    quantity_total = Widget.objects.aggregate(Sum('quantity'))
    print(quantity_total)
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WidgetForm()
    return render(request, 'home.html', {'widget_form': form, 'widget_list':widget_list, 'total':quantity_total})

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('home')