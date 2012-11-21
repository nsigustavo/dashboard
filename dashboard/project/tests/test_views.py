from django.test import TestCase
from django.test.client import RequestFactory

from dashboard.project.views import run_task
from dashboard.project.models import Analysis


class TestViews(TestCase):
    fixtures = ['project.json', 'analysis.json']

    def setUp(self):
        self.analysis = Analysis.objects.get(id=1)

    def test_project_details_should_be_acessible(self):
        url = '/project/%d/' % self.analysis.project.id
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_absent_project_should_not_be_acessible(self):
        url = '/project/999/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_project_analyze_should_be_acessible(self):
        url = '/project/%d/analyze/' % self.analysis.project.id
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_absent_project_analyze_should_not_be_acessible(self):
        url = '/project/999/analyze/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_should_show_projects_and_get_200(self):
        url = "/projects/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_should_visit_create_project_and_get_200(self):
        url = "/projects/create"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestRunTaskView(TestCase):
    fixtures = ['project.json', 'analysis.json']

    def setUp(self):
        self.tasks = ['pep8', 'pyflakes', 'clonedigger', 'jshint', 'csslint']

    def test_acessar_tasks_padrao(self):
        for task in self.tasks:
            response = self.client.get('/project/1/%s/' % task)
            self.assertEqual(200, response.status_code)

    def test_task_deve_retornar_numero_de_erros(self):
        erros_por_task = {
            'pep8': '20',
            'pyflakes': '2',
            'clonedigger': '21',
            'jshint': '102',
            'csslint': '755',
        }

        request = RequestFactory().get('/project/1/task')

        for task in self.tasks:
            response = run_task(request, project_id=1, task=task)
            self.assertEqual(erros_por_task[task], response.content)

    def test_deve_retornar_404_para_task_nao_existente(self):
        response = self.client.get('/project/1/task_inexistente/')
        self.assertEqual(404, response.status_code)

