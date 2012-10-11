from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import Project
from analyse import code_analysis


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    result_analysis = code_analysis(project)
    context = {'project': project, 'code_analysis': result_analysis}
    return render_to_response('detail.html', context,
                               context_instance=RequestContext(request))
