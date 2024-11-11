from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogPost


def post_list(request):
    posts_per_page = request.GET.get('posts_per_page', 5)

    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, posts_per_page)

    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    page_range = range(max(1, posts.number - 2),
                         min(posts.paginator.num_pages + 1, posts.number + 3))

    context = {
        'posts': posts,
        'page_range': page_range,
        'posts_per_page': int(posts_per_page),
        'per_page_options':[5, 10, 20, 50]
    }

    return render(request,'blog/post_list.html', context)
