from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save(commit=False)
            Post.save()
            messages.success(request, 'Your Post has been successfully received!.')
            return redirect(reverse_lazy('blog:post_new'))
        else:
            messages.error(request, 'Please correct the errors below.')
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = PostForm()

    context = {'form': form}    
    return render(request, 'blog/post_new.html', context)

