#!/usr/bin/python
from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'beta', credentials=credentials)

# Project ID for this request.
project = 'balaji-network-codelabs'  # TODO: Update placeholder value.

network_body = {
  "name": "newtest123",
  "autoCreateSubnetworks": "true"
}
    # TODO: Add desired entries to the request body.


request = service.networks().insert(project=project, body=network_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
