import git
import shutil

from code_quality_tools import CodeQualityCheck


def git_clone(url_git, name=None):
    if name is None:
        git.Git().clone(url_git)
    else:
        git.Git().clone(url_git, name)


def code_analysis(project, task=None):
    check = CodeQualityCheck()
    git_clone(project.url_git, project.name)

    if task:
        task = "get_%s_errors" % task
        task = getattr(check, task, lambda: 'task invalida')
        analysis_result = task()
    else:
        analysis_result = check.get_all_errors(project.name)

    shutil.rmtree(project.name)

    return analysis_result
