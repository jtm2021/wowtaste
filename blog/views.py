from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ArticlesList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles.html'
    paginate_by = 6


class AddedPostsByUsers(LoginRequiredMixin, generic.ListView):
    model = Post
    author = Post.author
    login_url = 'account_login'
    template_name = 'myposts.html'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author=self.request.user, status=1).order_by('-created_on')


class AddMyPost(View):
    def get(self, request):
        context = {'form': PostForm()}
        return render(request, 'add_my_post.html', context)

    def post(self, request):
        """
        allow user to share new articles to
        the site for others to see.
        """

        if request.method == 'POST':
            form = PostForm(request.POST, initial={
                'author': request.user.email
                })
            if form.is_valid():
                form.instance.email = request.user.email
                form.instance.name = request.user.username
                form.instance.author = self.request.user
                form.save()
                messages.success(request, 'Your post is awaiting approval.')
                return redirect('home')
            else:
                messages.error(request, 'Error: Something is wrong, please try again!')  
                context = {'form': form}
                return render(request, 'add_my_post.html', context)
        else:
            form = PostForm()

        context = {'form': form}
        return render(request, 'index.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
