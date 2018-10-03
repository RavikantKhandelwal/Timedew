from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
    # this is important for importing handlers
        import blog.signals.handlers