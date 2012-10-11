import os
import shutil
from django.test import TestCase
from analyse import git_clone, code_analysis
from models import Project


class TestCodeAnalysis(TestCase):
    fixtures = ['project.json']
    project_path = 'code_quality_tools'

    def test_should_be_possible_clone_git_repository(self):
        git_clone('https://github.com/clybob/code_quality_tools.git')
        path_exists = os.path.exists(self.project_path)
        self.assertTrue(path_exists)
        shutil.rmtree(self.project_path)

    def test_should_be_possible_clone_git_repository_passing_directory(self):
        git_clone('https://github.com/clybob/code_quality_tools.git', 'test')
        path_exists = os.path.exists('test')
        self.assertTrue(path_exists)
        shutil.rmtree('test')

    def test_should_return_dictionary_with_quality_information(self):
        project = Project.objects.get(id=1)
        analysis_result = code_analysis(project)
        self.assertTrue(type(analysis_result) is dict)
        self.assertEqual(len(analysis_result), 5)
        shutil.rmtree(project.name)
