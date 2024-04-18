from server.apps.base.models import BaseSetting


def settings(request):
    """Get Settings."""
    return {"settings": BaseSetting.objects.first()}
