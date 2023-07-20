from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def index(request):
    if request.method =='POST':
        form = forms.DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictions')
    else:
        form = forms.DataForm()
    context ={
        'form':form,
    }
    return render(request,'dashboard/index.html',context)

def predictions(request):
    predictions_sports = models.Data.objects.all()
    context={
        'predicted_sports':predictions_sports,
    }
    return render(request,'dashboard/predictions.html', context)




