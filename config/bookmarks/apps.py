from django.apps import AppConfig


class BookmarksConfig(AppConfig):
    name = 'bookmarks'

    def ready(self):
        import bookmarks.signals
