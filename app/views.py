from django.shortcuts import render
from .forms import *
from .models import *
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.db.models import Q , F
from django.shortcuts import render,get_object_or_404

# Create your views here.
def home(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(active=True)
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'categories': categories,
        'posts':posts,
        'page':page,

    }

    return render(request, 'home.html', context)


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()
            paginator = Paginator(results, 12)
            categories = Category.objects.all()

            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_page)

            context={'results': results,
                     'submitbutton': submitbutton,
                     'page':page,
                     'categories':categories,}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def post_detail(request,slug):
    categories = Category.objects.all()

    post = get_object_or_404(Post,slug=slug,active=True)
    cc = post.category.slug
    cat = get_object_or_404(Category,slug=cc)
    esp = cat.posts.filter(active = True)
    Post.objects.filter(pk=post.id).update(views=F('views') + 1)
    views = post.views + 1  # to show valid counter in the template



    context={
        'title':post.title,
        'post': post,
        'esp':esp,
        'categories':categories



    }

    return render(request,'detail.html',context)


def cat_detail(request,slug):
    cat = get_object_or_404(Category,slug=slug)
    esp = cat.posts.filter(active = True)
    categories = Category.objects.all()



    context={
        'title':cat,
        'esp':esp,
        'cat':cat,
        'categories': categories

    }

    return render(request,'category.html',context)