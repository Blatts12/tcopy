from rest_framework import pagination


class FeedPagination(pagination.CursorPagination):
    page_size = 12
    ordering = "-pub_date"
