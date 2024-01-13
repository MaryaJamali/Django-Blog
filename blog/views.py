from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date

# Temporary data
all_posts = [
    {
        'slug': 'learning-Django',
        'title': 'Django Course',
        'author': 'Maryam Jamali',
        'image': '2.png',
        'date': date(2023, 11, 25),
        'short_description': 'this is Django course with me from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas!
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas! 
        """
    },
    {
        'slug': 'learning-Django-Rest',
        'title': 'Django-Rest Course',
        'author': 'Maryam Jamali',
        'image': '4.png',
        'date': date(2023, 11, 25),
        'short_description': 'this is django-Rest course with me from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas!
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas! 
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas!
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius excepturi, molestias quam quasi
            repudiandae voluptatibus! Aspernatur aut autem eos et eum, fuga iste modi obcaecati odio officiis
            quo temporibus voluptas! 
        """
    },
]


# Post extraction based on date
def get_date(post):
    return post['date']


# Create your views here.
def home_page_view(request: HttpRequest):
    # Simple sorting is based on date
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-1:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts_page_view(request: HttpRequest):
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'blog/all-posts.html', context=context)


def detail_post_page_view(request: HttpRequest, slug):
    # The first item that matches the condition gets it
    post_as_slug = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/detail-post.html', {
        'post': post_as_slug
    })
