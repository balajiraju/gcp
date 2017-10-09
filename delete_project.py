#!/usr/bin/python
projectname = raw_input("Please enter the Unique project name:")
print ("The project name will be same as projectid")
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

 
 
credentials = GoogleCredentials.get_application_default()
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
print projectname

project_id = 'projectname'  # TODO: Update placeholder value.

request = service.projects().delete(projectId=project_id)
request.execute()
print('Project deleted successfully')
