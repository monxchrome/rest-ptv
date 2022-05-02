import django_filters

from .models import Post


class PostFilterSet(django_filters.FilterSet):
    # title = django_filters.CharFilter(lookup_expr='startswith')

    class Meta:
        model = Post
        fields = {
            'title': ['iexact'],
            'description': ['iexact'],
        }
