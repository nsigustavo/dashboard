from django.test import TestCase
from dashboard.project.models import ProjectForm


class TestModels(TestCase):

    def test_should_create_project_with_form(self):
        project_form = ProjectForm({'name': 'Testing', 'url_git': 'git_url'})
        self.assertEqual(project_form.is_valid(), True)

    def test_should_return_erro_in_form_if_send_form_blank(self):
        project_form = ProjectForm({'name': '', 'url_git': ''})
        self.assertEqual(project_form.is_valid(), False)

    def test_should_create_project_and_return_name_already_exists(self):
        project_form = ProjectForm({'name': 'Testing', 'url_git': 'git_url'})
        self.assertEqual(bool(project_form.save()), True)
        project_form_2 = ProjectForm({'name': 'Testing', 'url_git': 'git_url'})
        self.assertEqual(project_form_2.is_valid(), False)