from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
# Create your views here.

#CRUD create retrieve update delete

#List all the posts
def post_list_view(request):
	post_objects = Post.objects.all()
	context = {
			'post_objects': post_objects
	}
	return render(request, "posts/index.html", context)

class StoryDetailView(DetailView):
	model = Post
	template_name = 'posts/story1.html'
