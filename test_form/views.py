from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import UserFormModel



def test_form(request):
    if request.method == "GET":
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, template_name='form.html', context=context)
    
    elif request.method == "POST":
        print(request.POST)
        form = UserForm(data=request.POST, files=request.FILES)
        form.save()
        return HttpResponse("Data received")
