from django.test import TestCase
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
