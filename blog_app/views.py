from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Blog



@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("blog_title")
        content = request.POST.get("blog_content")

        blog = Blog.objects.create(
            blog_title=title,
            blog_content=content,
            author=request.user
        )

        return redirect("blog_detail", blog_id=blog.blog_id)

    return render(request, "blog/create_post.html")

@login_required(login_url='login')
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "blog/my_blogs.html", {"blogs": blogs})


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, "blog/home.html", {"blogs": blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, blog_id=blog_id)
    return render(request, "blog/blog_detail.html", {"blog": blog})

@login_required(login_url='login')
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, blog_id=blog_id)

    # 🔥 Security Check (VERY IMPORTANT)
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this blog.")

    if request.method == "POST":
        blog.blog_title = request.POST.get("blog_title")
        blog.blog_content = request.POST.get("blog_content")
        blog.save()

        return redirect("blog_detail", blog_id=blog.blog_id)

    return render(request, "blog/edit_blog.html", {"blog": blog})

@login_required(login_url='login')
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, blog_id=blog_id)

    # 🔥 Security Check
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog.")

    if request.method == "POST":
        blog.delete()
        return redirect("my_blogs")

    return render(request, "blog/delete_blog.html", {"blog": blog})