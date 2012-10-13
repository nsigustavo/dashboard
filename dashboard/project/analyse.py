import git
import shutil
from code_quality_tools.code_quality_tools import CodeQualityCheck


def git_clone(url_git, name=None):
    if name is None:
        git.Git().clone(url_git)
    else:
        git.Git().clone(url_git, name)


def code_analysis(project):
    check = CodeQualityCheck()
    git_clone(project.url_git, project.name)
    analysis_result = check.get_all_errors(project.name)
    shutil.rmtree(project.name)

    return analysis_result
