from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from users.models import User

def profile(request):
    user=User.objects.get(first_name='khaoula')
    posts = Post.objects.filter(author=user).order_by('-created_at')

    for post in posts:
        print(f"Post author is {post.author.first_name}")
    context={
        'user': user,
        'posts': posts
    }
    
    return render(request, 'profile.html',context)

def blog_posts(request):
    # posts = Post.objects.all().order_by('-created_at')
    # context={
    #     'authenticated_user' : User.objects.get(first_name='khaoula'),
    #     'posts': posts
    # }
    # for post in posts:
    #     if post.author == context['authenticated_user']:
    #         print("post author is authenticated user")
    #     post.image.name=post.image.name.replace('/static','/')
    #     print("image url--->"+post.image.name) 

    # return render(request, 'blog.html', context)
    return render(request, 'blog.html')


def blog_category(request, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(categories=category)
    context={
        'category': category,
        'posts': posts
    }
    return render(request, 'category.html', context)

def blog_details(request,blog_id):
    post = Post.objects.get(id=blog_id)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog_details.html', context)

def comments(request):
    return render(request, 'commentSection.html')

def add_comment(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        content = request.POST.get('content')
        
        if content:
            # Create a new comment associated with the post
            new_comment = Comment.objects.create(
                post=post,
                content=content
            )
            print("New comment created:", new_comment.content)
            return redirect('blog_details', blog_id=post.id)  # Redirect to the post detail page
        else:
            # Handle invalid form submission (e.g., empty comment)
            return HttpResponse('Invalid comment data', status=400)
    else:
        # Handle non-POST requests (if any)
        return HttpResponse('Method Not Allowed', status=405)