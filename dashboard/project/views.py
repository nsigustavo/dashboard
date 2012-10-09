from django.http import HttpResponse


def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)
