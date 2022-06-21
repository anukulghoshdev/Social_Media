from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from App_RegLog.models import UserProfile, Follow
from App_Posts.models import Post, Like

from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))

    #like er kaj ekhane o achy
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)


    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)

    return render(request, 'App_Posts/home.html', context={'search':search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list })


@login_required
def like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(user=user, post=post)
    if not already_liked:
        liked_post = Like(post=post, user=user)
        liked_post.save()

    return HttpResponseRedirect(reverse('App_Posts:home'))


@login_required
def unlike(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(user=user, post=post)
    already_liked.delete()

    return HttpResponseRedirect(reverse('App_Posts:home'))
