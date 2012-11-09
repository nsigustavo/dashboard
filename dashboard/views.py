from django.http import HttpResponseNotFound


def view_404(request):
    return HttpResponseNotFound()
