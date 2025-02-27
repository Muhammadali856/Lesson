from blogs.models import BlogCategoryModel


def run():
    #cat2 = BlogCategoryModel.objects.create(title='Blog category 2')
    #cat2 = BlogCategoryModel.objects.create(title='Blog category 2')


    # cat = BlogCategoryModel.objects.get(id=2)
    # cat.title = "Yangi title"
    # cat.save()

    # select * from blog_category
    # cat = BlogCategoryModel.objects.all()
    # print(cat)

    # select title from blog_category
    # cats = BlogCategoryModel.objects.values('title', 'created_at')
    # print(cats)

    # select * from blog_category id > 2
    """
    __gt > 
    __gte >=
    __lt<
    __lte<= 
    __isnull
    """
    cats = BlogCategoryModel.objects.filter(id__gte=2).values('title', 'updated_at')
    print(cats)