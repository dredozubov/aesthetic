from django.views.generic import DetailView, ListView
from blog.models import Post


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = "posts"
    paginate_by = 3

post_detail = PostDetailView.as_view()
post_list = PostListView.as_view(
            queryset=Post.objects.order_by('-created_at'),
            )
