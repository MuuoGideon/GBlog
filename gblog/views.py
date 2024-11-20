from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Post
from django.contrib.auth.models import User
from . forms import PostForm
from django.http import HttpResponseRedirect


def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})

def dashboard(request):
	post_count = Post.objects.all().count()
	return render(request, 'dashboard.html', {'post_count':post_count})

def search_post(request):
	if request.method == "POST":
		searched = request.POST['searched']
		posts = Post.objects.filter(title__contains=searched)
		return render(request, 'search_post.html', {'posts':posts,'searched':searched})

	else:
		return render(request, 'search_post.html', {'searched':searched})

def delete_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	post.delete()
	messages.success(request, ('Post deleted successfully'))
	return redirect('home')

def update_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		messages.success(request, ('Post updated successfully'))
		return redirect('home')
	return render(request, 'update_post.html', {'post':post,'form':form})

def add_post(request):
	submitted = False
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ('Post submitted Successfully'))
			return HttpResponseRedirect('/?submitted=True')
	else:
		form = PostForm()
		if 'submitted' in request.GET:
			submitted = True


	return render(request, 'add_post.html', {'form':form,'submitted':submitted})


def show_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'show_post.html', {'post':post})



def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successful'))
			return redirect('home')
		else:
			messages.success(request, ('Incorrect username or password, please try again'))
			return redirect('login-user')
	else:
		return render(request, 'login_user.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ('Successful Loged out!'))
	return redirect('login-user')