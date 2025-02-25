from django.shortcuts import render

def home_page_views(request):
    return render(request, template_name='index.html')

def about_page_views(request):
    return render(request, template_name='pages/about.html')

def author_page_views(request):
    return render(request, template_name='pages/author.html')

def contact_page_views(request):
    return render(request, template_name='pages/contact.html')

def single_author_page_views(request):
    return render(request, template_name='pages/single_author.html')