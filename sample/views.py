from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    data = Blog.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'sample/index.html', params)

def create(request):
    params = {
        'form': BlogForm(),
    }
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog(title=title, content=content)
        blog.save()
        return redirect(to='/sample')
    return render(request, 'sample/create.html', params)


def detail(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	params = {
            'id': blog_id,
        	'obj': blog,
        }
	return render(request, 'sample/detail.html', params)


def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect(to='/sample')
    else:
        form = BlogForm(initial={
            'title': blog.title,
            'content': blog.content,
        })
        params = {
            'id': blog_id,
            'form': form,
        }
        return render(request, 'sample/edit.html', params)

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.delete()
        return redirect(to='/sample')
    else:
        params = {
            'id': blog_id,
            'obj': blog,
        }
        return render(request, 'sample/delete.html', params)