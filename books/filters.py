from django_filters import rest_framework as filters


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")
    publication_year = filters.NumberFilter(lookup_expr="exact")
    edition = filters.CharFilter(lookup_expr="contains")
    authors__name = filters.CharFilter(lookup_expr="contains")
