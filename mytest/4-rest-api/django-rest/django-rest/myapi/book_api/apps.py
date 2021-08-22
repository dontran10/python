from django.apps import AppConfig


class BookApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_api'
    verbose_name = 'Book API Service'
