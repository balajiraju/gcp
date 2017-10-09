#!/usr/bin/python
print ("The project name will be same as projectid so please enter unique name")
projectname = raw_input("Please enter the Unique project name:"
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

 
 
credentials = GoogleCredentials.get_application_default()
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
print projectname
project_body = {
                 'name': projectname,
                 'projectId': projectname
               }
request = service.projects().create(body=project_body)
request.execute()
print('New project is created successfully')
