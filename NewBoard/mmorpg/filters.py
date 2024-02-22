from django_filters import FilterSet, ModelChoiceFilter

from mmorpg.models import Answer, Post#answer=reply


class PostFilter(FilterSet):
    post = ModelChoiceFilter(
        empty_label='Все обьявления',
        field_name='post',
        label='Фильтр по обновлениям',
        queryset=Answer.objects.all()#answer=reply
    )

    class Meta:
        model = Answer#answer=reply
        fields = ('post',)

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author_id=kwargs['request'])