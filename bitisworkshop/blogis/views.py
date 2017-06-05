

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView

from blogis.models import BlogPost
from .forms import PostForm
from django.shortcuts import redirect


class BlogView(TemplateView):
    def get(self, request):
        context = {}
        context['name'] = "Amit"
        context['subject'] = 'Python'
        context['framework'] = 'Django'
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        context['days'] = days
        posts = BlogPost.objects.all
        context['posts'] = posts
        return render(request, 'blogis/pages/show_blogs.html', context)

    def post(self, request, slug=None, id=None):
        pass


class SingleBlogPost(TemplateView):
    def get(self, request, pk):
        print(pk)
        context = {}
        post = BlogPost.objects.get(pk=pk)
        context['post'] = post
        return render(request, 'blogis/pages/single_blog.html', context)

    def post(self, request, slug=None, id=None):
        pass

def index(request):
    return HttpResponse("Hello, world. You're at the blogis index.")


class HomeView(TemplateView):
    def get(self, request):
        context = {}
        context['name'] = "Amit"
        context['subject'] = 'Python'
        context['framework'] = 'Django'
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        context['days'] = days
        posts = BlogPost.objects.all
        context['posts'] = posts
        return render(request, 'blogis/pages/home.html', context)

    def post(self, request, slug=None, id=None):
        pass


class AddBlogView(TemplateView):
    def get(self, request):
        context = {}
        form = PostForm()
        context['form'] = form
        return render(request, 'blogis/pages/add_blog.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/blogs/post/' + str(post.pk) + '/')



