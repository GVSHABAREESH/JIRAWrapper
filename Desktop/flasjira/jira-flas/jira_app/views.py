# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jira.client import JIRA
from wrapper import jirawrapper


# Create your views here.

class ProjectListView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            creating_project = jirawrapper().project_creation(data)
            return Response({'Project_Is_Created':creating_project}, status=status.HTTP_201_CREATED)
        except:
            return Response("Project Is Not Created Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            projects = jirawrapper().get_all_projectlist()
            data = []
            for pro in projects:
                data.append({'name': pro.name, 'id': pro.id, 'key': pro.key})
            return Response({'List_of_all_projects':data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Projects Are Not Listed Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

class CreatingIssue(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        print data,"--------------"
        try:
            create_issue = jirawrapper().issue_creation(data)
            issue_data = []
            issue_data.append({'project':data['project'],'summary':data['summary'],'description':data['description'],'bug':str(create_issue)})
            return Response({'Issue_Is_Created':issue_data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Issue Is Not Created Due to Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            issue = jirawrapper().get_all_issues()
            demo = []
            for each in issue:
                demo.append({'key':each.key,'id':each.id})
            return Response({'List_of_all_issues':demo},status=status.HTTP_201_CREATED)
        except:
            return Response("Issue Are Not Listed Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)


class CreatingSubtask(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        print data,'----'
        try:
            create_issue = jirawrapper().subtask_creation(data)
            sub_task_data = []
            sub_task_data.append({'project': data['project'], 'summary': data['summary'], 'description': data['description'],'Sub_Task_created': str(create_issue)})
            return Response({'Sub_task_is_Created':sub_task_data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Sub_task Is Not Created Due to Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            sub_tasks = jirawrapper().get_all_sub_tasks()
            print sub_tasks
            st = []
            for each in sub_tasks:
                if len(each.fields.subtasks) > 0:
                    st.append({'key':each.fields.subtasks[0].key,'id':each.fields.subtasks[0].id})#each.fields.subtasks)
            return Response({'Sub_tasks are':st},status=status.HTTP_201_CREATED)
        except:
            return Response("Sub_Tasks Are Not Listed Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

class CreatingSprint(APIView):

    def post(self, request, *args, **kwargs):
        spr = request.data
        print spr,'---'
        try:
            create_sprint = jirawrapper().creating_sprint(spr)
            sprint_data = []
            sprint_data.append({'name': spr['name'], 'board_id': spr['board_id'],'Sprint_created': str()})
            return Response({'SprintIsCreated':sprint_data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Sprint Is Not Created Due to Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            sprintlist = jirawrapper().get_all_sprints()
            spr_list = []
            for each in sprintlist:
                spr_list.append({'name':each.name,'id':each.id})
            return Response({'List_of_all_Sprints': spr_list}, status=status.HTTP_201_CREATED)
        except:
            return Response("Sprints Are Not Listed Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)


class CreatingComponent(APIView):

    def post(self, request, *args, **kwargs):
        comp = request.data
        print comp
        try:
            create_component = jirawrapper().adding_component(comp)
            comp_data = []
            comp_data.append({'name': comp['name'],'project': comp['project'],'description': comp['description'],'Component_created': str(create_component)})
            return Response({'Component_is_added':comp_data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Component Is Not Created Due to Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            compo = jirawrapper().get_all_components_of_project()
            get_comp = []
            for each in compo:
                get_comp.append({'name':each.name,'id':each.id})
            return Response({'List_of_all_Components':get_comp},status=status.HTTP_201_CREATED)
        except:
            return Response("Components Are Not Listed Due To Some Bad Request",status=status.HTTP_400_BAD_REQUEST)


class AddingComment(APIView):

    def post(self, request, *args, **kwargs):
        comm = request.data
        print comm
        try:
            add_comment = jirawrapper().adding_comment(comm)
            comm_data = []
            comm_data.append({'issue':comm['issue'],'body':comm['body'],'Comment_added':str(add_comment)})
            return Response({'Comment_is_added':comm_data}, status=status.HTTP_201_CREATED)
        except:
            return Response("Commmet Is Not Added Due to Some Bad Request", status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        try:
            comm = jirawrapper().get_all_comments_of_project()
            commnet_info = []
            for each in comm:
                commnet_info.append({'Sprint_id': each.id, 'Issue_key': each.key})
            return Response({'List_of_all_Comments':commnet_info},status=status.HTTP_201_CREATED)
        except:
            return Response("Commmets Are Not Listed Due To Some Bad Request",status=status.HTTP_400_BAD_REQUEST)

class GettingSprintIssues(APIView):

    def get(self,request,*args,**kwargs):
        try:
            sprintlist = jirawrapper().get_all_Sprint_issues_of_project()
            sprint_info = []
            for each in sprintlist:
                sprint_info.append({'sprintid': each.id, 'Story': each.key})
            return Response({'List_of_all_Sprint_issues': sprint_info}, status=status.HTTP_201_CREATED)
        except:
            return Response("Sprint_issues Are Not Listed Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)














