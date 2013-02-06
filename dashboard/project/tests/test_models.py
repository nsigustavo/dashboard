from django.test import TestCase
from dashboard.project.models import ProjectForm, Project


class TestModelsProject(TestCase):
    fixtures = ['project.json', 'analysis.json']

    def setUp(self):
        self.project = Project.objects.get(id=1)

    def test_get_analysis_history_should_return_dict(self):
        analysis_history = self.project.get_analysis_history('pep8')
        self.assertEqual(type(analysis_history), type({}))
        self.assertTrue(analysis_history['dates'] > 0)
        self.assertTrue(analysis_history['metric_analysis'] > 0)


class TestModelsProjectForm(TestCase):

    def test_should_create_project_with_form(self):
        project_form = ProjectForm({'name': 'Testing', 'url_git': 'git_url', 'path': 'src'})
        self.assertEqual(project_form.is_valid(), True)

    def test_should_return_erro_in_form_if_send_form_blank(self):
        project_form = ProjectForm({'name': '', 'url_git': ''})
        self.assertEqual(project_form.is_valid(), False)

    def test_should_create_project_and_return_name_already_exists(self):
        project_form = ProjectForm({'name': 'Testing', 'url_git': 'git_url', 'path': 'src'})
        self.assertEqual(bool(project_form.save()), True)
        project_form_2 = ProjectForm({'name': 'Testing', 'url_git': 'git_url', 'path': 'src'})
        self.assertEqual(project_form_2.is_valid(), False)
