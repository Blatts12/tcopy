from rest_framework import pagination


class FeedPagination(pagination.CursorPagination):
    page_size = 32
    ordering = "-pub_date"
