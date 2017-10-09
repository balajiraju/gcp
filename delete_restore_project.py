#!/usr/bin/python

import sys, getopt

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1beta1', credentials=credentials)


def delete(delproj):
   
   project_id = delproj  # TODO: Update placeholder value.
   request = service.projects().delete(projectId=project_id)
   request.execute()
   print "Deleting",delproj,"project successfully"

def restore(resprojectid):
   
   project_id = resprojectid  # TODO: Update placeholder value.
   undelete_project_request_body = {}
   request = service.projects().undelete(projectId=project_id, body=undelete_project_request_body)
   request.execute()
   print "Restoring",resprojectid, "project successfully"


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hd:r:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -d <project id to delete> -r <project id to restore>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -d <project id to delete> -r <project id to restore>'
         sys.exit()
      elif opt in ("-d", "--ifile"):
         inputfile = arg
      elif opt in ("-r", "--ofile"):
         outputfile = arg
   
   if inputfile:
      delete(inputfile)
   else:
      restore(outputfile)
  # print 'Project id to delete"', inputfile
  # delete(inputfile)
  # print 'Project id to restore"', outputfile
  # restore(outputfile)

if __name__ == "__main__":
  
   main(sys.argv[1:])
