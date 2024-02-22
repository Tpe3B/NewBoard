from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from datetime import date
from mmorpg.filters import PostFilter
from mmorpg.forms import PostForm, AnswerForm, SendForm
from mmorpg.models import Post, Answer
from NewBoard import settings
from mmorpg.models import Answer

class PostsList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_logged'] = self.request.user.is_authenticated
        context['current_user'] = self.request.user
        context['user_is_staff'] = self.request.user.is_staff
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers_by_post_id = Answer.objects.filter(post=self.kwargs['pk']).order_by('date')
        context['is_logged'] = self.request.user.is_authenticated
        context['answers'] = answers_by_post_id
        return context

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post_create'
    success_url = '/posts/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'post_edit'
    success_url = '/posts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
class AnswerAdd(CreateView):
    form_class = AnswerForm
    model = Answer
    template_name = 'answer/answer_add.html'
    context_object_name = 'answer_create'
    success_url = '/posts/'

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.author = self.request.user
        answer.post = get_object_or_404(Post, id=self.kwargs['pk'])
        form.save()
        return redirect('post', answer.post.pk)

class Answers(ListView):
    model = Answer
    template_name = 'answer/answer.html'
    context_object_name = 'answers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Answer.objects.filter(author_id=self.request.user.pk).order_by('date')
        context['filter'] = PostFilter(self.request.GET, queryset, request=self.request.user.pk)
        return context


def news_send(request):
    if request.method == 'GET':
        form = SendForm()
        return render(request, 'accounts/email/all_message_mail.html', {'form': form})
    else:
        form = SendForm(request.POST)
        if form.is_valid():
            content_mail = form.cleaned_data.get('content')
            recievers = []
            for user in User.objects.all():
                if user.email != ' ' or user.email != '':
                    recievers.append(user.email)

            html_mail = render_to_string(
                'message_all.html',
                {
                    'text': content_mail,
                }
            )
            message = EmailMultiAlternatives(
                subject=f'Новость!',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=recievers
            )
            message.attach_alternative(html_mail, 'text/html')
            message.send()
            return redirect('/posts/')


def delete_ans(self, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()
    return redirect('/posts/')

def allow_ans(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.is_allowed = True
    html_mail = render_to_string(
        'otklik.html',
        {
            'text': answer.content,
            'post_title': answer.post.title,
            'post_link': f'http://127.0.0.1:8000/posts/{answer.post.pk}',
        }
    )

    message = EmailMultiAlternatives(
        subject=f'Ваш отклик был принят',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[answer.author.email]
    )

    message.attach_alternative(html_mail, 'text/html')
    message.send()
    answer.save()
    return redirect('/posts/')

def delete_post(self, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')

