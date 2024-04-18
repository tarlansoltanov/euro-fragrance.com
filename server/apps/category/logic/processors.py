from server.apps.category.models import Category


def categories(request):
    """Get Categories."""
    return {"categories": Category.objects.filter(main=None)}
