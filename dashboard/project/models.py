from django.db import models
from django.forms import ModelForm


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    url_git = models.CharField(max_length=256, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'dashboard_project'

    def get_analysis_history(self, metric_name='ALL', limit=10):
        history = {'dates': [], 'metric_analysis': []}
        analysis_history = Analysis.objects.filter(project_id=self.id).order_by('date_executed')[:limit]

        for analysis in analysis_history:
            history['dates'].append(analysis.date_executed_for_humans)
            metric_erros = getattr(analysis, metric_name)
            history['metric_analysis'].append(metric_erros)

        return history

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'url_git')


class Analysis(models.Model):
    project = models.ForeignKey(Project)
    date_executed = models.DateTimeField(auto_now_add=True, editable=False)
    pep8 = models.PositiveIntegerField(default=0)
    pyflakes = models.PositiveIntegerField(default=0)
    clonedigger = models.PositiveIntegerField(default=0)
    jshint = models.PositiveIntegerField(default=0)
    csslint = models.PositiveIntegerField(default=0)
    result = models.TextField(null=True, blank=False)

    class Meta:
        db_table = 'dashboard_analysis'

    @property
    def date_executed_for_humans(self):
        return self.date_executed.strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        project_name = self.project.name
        date_executed = self.date_executed_for_humans
        return 'Analysis of project(%s) on %s' % (project_name, date_executed)

    def __unicode__(self):
        project_name = self.project.name
        date_executed = self.date_executed_for_humans
        return u'Analysis of project(%s) on %s' % (project_name, date_executed)
