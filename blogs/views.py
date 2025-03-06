from django.shortcuts import render
from .models import BlogModel, BlogCategoryModel, BlogTagModel, BlogCommentModel

def blog_list_view(request):
    blogs = BlogModel.objects.all()
    categories = request.GET.get('categories')
    tags = request.GET.get('tags')
    if categories:
        blogs = blogs.filter(categories=categories)
    elif tags:
        blogs = blogs.filter(tags=tags)
    latest_blogs = BlogModel.objects.all().order_by('-created_at')[:4]
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    context = {
        'blogs': blogs,
        'latest_blogs': latest_blogs,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_detail_view(request, pk):
    try:
        blog = BlogModel.objects.get(pk=pk)
    except BlogModel.DoesNotExist:
        return render(request, 'pages/404.html')
    
    context = {
        'blog': blog,
    }
    return render(request, 'blog/single_blog.html', context=context)
