from django.shortcuts import render

def home_page_views(request):
    return render(request, template_name='index.html')

