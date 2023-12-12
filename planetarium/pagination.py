from rest_framework import pagination


class UniversalPaginator(pagination.PageNumberPagination):
    page_size = 3
