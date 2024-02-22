from django.urls import path

from mmorpg.views import PostsList, PostDetail, PostCreate, AnswerAdd, PostEdit, Answers, delete_ans, delete_post, \
   allow_ans, news_send

urlpatterns = [
   path('', PostsList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('create/', PostCreate.as_view(), name='postcreate'),
   path('<int:pk>/answer/add', AnswerAdd.as_view(), name='answer_add'),
   path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
   path('answers/', Answers.as_view(), name='answers'),
   path('delete/<int:pk>', delete_ans, name='delete_answer'),
   path('<int:pk>/delete', delete_post, name='delete_post'),
   path('<int:pk>/allow', allow_ans, name='allow_answer'),
   path('send_mails/', news_send, name='send_mails'),
]
