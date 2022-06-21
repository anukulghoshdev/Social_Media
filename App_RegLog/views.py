from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from App_RegLog.forms import SignUpForm, LogInForm, UserProfileEditForm
from App_Posts.forms import PostsForm

from django.contrib.auth.models import User

from App_RegLog.models import UserProfile, Follow
from App_Posts.models import Post



# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registration=False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registration=True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_RegLog:log_in'))
    return render(request, 'App_RegLog/sign_up.html', context={'form':form})




def log_in(request):
    form = LogInForm()
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home'))
    return render(request, 'App_RegLog/log_in.html', context={'form':form})



@login_required
def profile_edit(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserProfileEditForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = UserProfileEditForm(instance=request.user)
            return HttpResponseRedirect(reverse('App_RegLog:user_profile'))
    return render(request, 'App_RegLog/profile_edit.html', context={'form':form})



@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_RegLog:log_in'))

@login_required
def user_profile(request):
    form = PostsForm()
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_RegLog:user_profile'))
    return render(request, 'App_RegLog/user_profile.html', context={'form':form})



@login_required
def other_user_profile(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_RegLog:user_profile'))
    return render(request, 'App_RegLog/other_user_profile.html', context={'user_other':user_other, 'already_followed':already_followed})



@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following = following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following = following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_RegLog:other_user_profile', kwargs={'username':username}))


@login_required
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_RegLog:other_user_profile', kwargs={'username':username}))

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'App_RegLog/image_show.html', context={'post':post})
