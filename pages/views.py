from django.shortcuts import render
from pages.forms import ContactPageForm, ContactAboutPageForm
from django.contrib import messages

def home_page_views(request):
    return render(request, template_name='index.html')

def about_page_views(request):
    return render(request, template_name='pages/about.html')

def contact_page_views(request):
    if request.method == 'GET':
        return render(request, template_name='pages/contact.html')
    elif request.method == 'POST':
        form = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully sent to database!')
            return render(request, template_name='pages/contact.html')
        else:
            messages.error(request, 'Error!')
        return render(request, template_name='pages/contact.html')
        
