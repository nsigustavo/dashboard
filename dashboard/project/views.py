from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings
from django.utils import simplejson

from models import Project, ProjectForm, Analysis

from analyze import code_analysis


def detail(request, project_id):
    list_project_analysis = Analysis.objects.filter(
        project_id=project_id
    ).order_by('-date_executed')

    if not list_project_analysis:
        raise Http404

    project_analysis = list_project_analysis[0]

    return render_to_response(
        'detail.html',
        {
            'analysis': project_analysis,
            'result': eval(project_analysis.result)
        },
        context_instance=RequestContext(request)
    )


def analyze(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    result_analysis = code_analysis(project)

    analysis = Analysis()
    analysis.project = project
    analysis.pep8 = result_analysis['pep8']['total_errors']
    analysis.pyflakes = result_analysis['pyflakes']['total_errors']
    analysis.clonedigger = result_analysis['clonedigger']['total_errors']
    analysis.jshint = result_analysis['jshint']['total_errors']
    analysis.csslint = result_analysis['csslint']['total_errors']
    analysis.result = result_analysis
    analysis.save()

    return HttpResponse('done')


def all_projects(request):
    projects = Project.objects.all()
    return render_to_response('show_projects.html', {'projects': projects})


def run_task(request, project_id, task):
    project = get_object_or_404(Project, pk=project_id)
    errors = code_analysis(project, task=task)

    analysis = Analysis.objects.filter(
        project_id=project_id
    ).order_by('-date_executed')[0]

    try:
        analysis_task = getattr(analysis, task)
    except AttributeError:
        raise Http404

    analysis_task = errors['total_errors']
    analysis.save()

    return HttpResponse(analysis_task)


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm()

    return render_to_response(
        'create_project.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def history(request, project_id, metric_name):
    if metric_name not in settings.METRICS:
        raise Http404

    dates = []
    metric_analysis = []

    if 'numberOfElements' in request.GET:
        limit = request.GET['numberOfElements']
    else:
        limit = 10

    analysis_history = Analysis.objects.filter(
        project_id=project_id
    ).order_by('date_executed')[:limit]

    for analysis in analysis_history:
        dates.append(analysis.date_executed_for_humans)
        metric_erros = getattr(analysis, metric_name)
        metric_analysis.append(metric_erros)

    history = simplejson.dumps({
        'dates': dates,
        'metric_analysis': metric_analysis
    })

    return HttpResponse(history, mimetype='application/json')
