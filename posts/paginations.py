from rest_framework import pagination


class FeedPagination(pagination.CursorPagination):
    page_size = 2
    ordering = "-pub_date"
