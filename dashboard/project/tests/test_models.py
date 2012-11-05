from django.test import TestCase
from dashboard.project.models import ProjectForm


class TestModels(TestCase):

    def test_should_create_user_with_form(self):
        project_form = ProjectForm({'name': 'Testing', 'url_git': 'git_url'})
        self.assertEqual(project_form.is_valid(), True)

    def test_should_return_erro_in_form_if_send_form_blank(self):
        project_form = ProjectForm({'name': '', 'url_git': ''})
        self.assertEqual(project_form.is_valid(), False)