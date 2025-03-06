from django.shortcuts import render
from pages.forms import ContactPageForm, ContactAboutPageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required



@login_required(login_url='login/')
def about_page_views(request):
    return render(request, template_name='pages/about.html')


@permission_required('pages.view_contactmodel')
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
        

def home_page_views(request):
    return render(request, template_name='index.html')


def author_page_views(request):
    return render(request, template_name='pages/author.html')

def single_author_page_views(request):
    return render(request, template_name='pages/single_author.html')

def category_page_views(request):
    return render(request, template_name='recipe/category.html')

def blog_page_views(request):
    return render(request, template_name='blog/blog_list.html')

def recipe_page_views(request):
    return render(request, template_name='recipe/recipe_with_sidebar.html')

def shop_page_views(request):
    return render(request, template_name='shop/shop.html')