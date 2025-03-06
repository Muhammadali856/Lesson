from django.shortcuts import render

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