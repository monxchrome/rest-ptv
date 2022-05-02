from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .mixins import OwnerOrReadOnly
from .models import Post, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import PostForm
from .filters import PostFilterSet


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'gallery/post_list.html', {'object_list': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'gallery/post_detail.html', {'object': post})


def post_likes(request, slug):
    post = get_object_or_404(Post, slug=slug)
    page = request.GET.get('page', 1)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('post_list') + f"?page={page}")


def create_post(request):
    form = PostForm
    if request.method == 'GET':
        return render(request, 'gallery/post_form.html', {'form': form})
    data = PostForm(request.POST, request.FILES)
    if data.is_valid():
        post = data.save(commit=False)
        post.user = request.user
        post.save()
    return redirect('post_list')


class PostList(ListView):
    model = Post
    paginate_by = 8

    def get_queryset(self):
        qs = Post.objects.select_related('user').prefetch_related('likes')
        filtered_list = PostFilterSet(self.request.GET, queryset=qs)
        return filtered_list.qs


class PostDetail(DetailView):
    model = Post

    # def get_object(self, queryset=None):
    #     return super(PostDetail, self).get_object().select_related('user').prefetch_related('likes')

    def get_queryset(self):
        return super(PostDetail, self).get_queryset().\
            select_related('user').\
            prefetch_related('likes').\
            prefetch_related('comments')


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'file', 'description')
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(OwnerOrReadOnly, UpdateView):
    model = Post
    fields = ('title', 'file', 'description')
    template_name_suffix = "_update_form"
    success_url = '/gallery/'


class PostDelete(OwnerOrReadOnly, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


def create_comment(request, slug):
    if request.method == 'POST':
        text = request.POST.get('comment')
        parent_id = request.POST.get('parent_id')
        if parent_id == "":
            parent_id = None
        post = get_object_or_404(Post, slug=slug)
        comment = Comment.objects.create(
            title=text, user=request.user, post=post, parent_id=parent_id
        )
    return redirect('post_detail', post.slug)
