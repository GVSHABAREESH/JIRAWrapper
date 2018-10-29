from __future__ import unicode_literals
from jira.client import JIRA
from rest_framework.response import Response
from rest_framework import status


class jirawrapper(object):

    def __init__(self):
        self.jira = self.__authenticate()

    def __authenticate(self):
        options = {'server': 'https://gelivimanindl.atlassian.net'}
        jira = JIRA(options, basic_auth=('gmani9052@gmail.com', '9494123456a!'))
        return jira

    def project_creation(self,data):
        try:
            project = self.jira.create_project(name=data['name'], key=data['key'], template_name=data['template_name'])
            data = []
            data.append({'name':project['projectName'],'key':project['projectKey'],'id':project['projectId']})
            return data
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_projectlist(self):
        project = self.jira.projects()
        return project

    def issue_creation(self,data):
        try:
            project = self.jira.create_issue(project=data['project'], summary=data['summary'],description=data['description'],issuetype=data['issuetype'])
            return project
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_issues(self):
        # issue = self.jira.search_issues('issuetype=Bug')
        # issue = self.jira.search_issues('issuetype=Task')
        issue = self.jira.search_issues('issuetype=Story')
        return issue

    def subtask_creation(self,data):
        try:
            sub_task = self.jira.create_issue(project=data['project'], summary=data['summary'],description=data['description'],issuetype=data['issuetype'],parent=data['parent'])
            return sub_task
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_sub_tasks(self):
        project_issues = self.jira.search_issues('issuetype=Bug')
        return project_issues

    def creating_sprint(self,data):
        try:
            Sprints = self.jira.create_sprint(name=data['name'],board_id=data['board_id'])#,startDate=data['None'],endDate=data['None'])
            return Sprints
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_sprints(self):
        sprint_list = self.jira.sprints(board_id=2)
        return sprint_list

    def adding_component(self,data):
        try:
            Components = self.jira.create_component(name=data['name'],project=data['project'],description=data['description'],leadUserName=data['leadUserName'])
            return Components
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_components_of_project(self):
        comps = self.jira.project_components('MNP')
        return comps

    def adding_comment(self,data):
        try:
            comment = self.jira.add_comment(issue=data['issue'],body=data['body'])
            return comment
        except:
            return Response("Data Is Miss Matched and Not Found", status=status.HTTP_200_OK)

    def get_all_comments_of_project(self):
        comms = self.jira.comment(issue='SSP-1', comment=10012)
        print comms


    def get_all_Sprint_issues_of_project(self):
        sprintlist = self.jira.search_issues('issuetype=Story')
        return sprintlist

