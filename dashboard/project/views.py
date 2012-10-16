from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from models import Project, Analysis
from analyze import code_analysis


def detail(request, project_id):
    try:
        project_analysis = Analysis.objects.filter(project_id=project_id).order_by('-date_executed')[0]
    except Exception:
        raise Http404

    return render_to_response('detail.html', {'analysis': project_analysis},
                               context_instance=RequestContext(request))


def analyze(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    result_analysis = code_analysis(project)

    analysis = Analysis()
    analysis.project = project
    analysis.pep8 = result_analysis['pep8']['total_errors']
    analysis.pyflakes = result_analysis['pyflakes']['total_errors']
    analysis.clonedigger = result_analysis['clonedigger']['percentage_clones']
    analysis.jshint = result_analysis['jshint']['total_errors']
    analysis.csslint = result_analysis['csslint']['total_errors']
    analysis.result = result_analysis
    analysis.save()

    return HttpResponse('done')
