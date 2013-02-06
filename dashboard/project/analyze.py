import shutil
import os

from git import Git
from code_quality_tools import CodeQualityCheck


def git_clone(url_git, name=None):
    if name is None:
        Git().clone(url_git)
    else:
        Git().clone(url_git, name)


def code_analysis(project, task=None):
    base_path = os.getcwd()
    clean_clones(project, base_path)
    os.chdir('/tmp')

    check = CodeQualityCheck()
    git_clone(project.url_git, project.name)

    os.chdir('%s/%s' % (project.name, project.path))

    if task:
        task = "get_%s_errors" % task
        task = getattr(check, task, lambda: 'invalid task')
        analysis_result = task()
    else:
        analysis_result = check.get_all_errors()

    clean_clones(project, base_path)

    return analysis_result


def clean_clones(project, return_path):
    try:
        os.chdir('/tmp')
        shutil.rmtree(project.name)
        os.chdir(return_path)
    except:
        pass
