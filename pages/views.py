from django.shortcuts import render


def about_page_views(request):
    return render(request, template_name='pages/about.html')

def contact_page_views(request):
    return render(request, template_name='pages/contact.html')