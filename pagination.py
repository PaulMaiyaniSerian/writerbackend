# myapp/pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow client to override, e.g., ?page_size=20
    max_page_size = 100  # Maximum limit allowed when using `page_size`
