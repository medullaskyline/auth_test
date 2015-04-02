# Python example modified from https://cloud.google.com/bigquery/loading-data-into-bigquery
from urllib2 import HTTPError
import pprint
from apiclient.discovery import build
import httplib2
import time
import os
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools


# Loads the table from Google Cloud Storage and prints the table.
def loadTable(service, projectId, datasetId, targetTableId, sourceCSV):
    try:
        jobCollection = service.jobs()
        jobData = {
            'projectId': projectId,
            'configuration': {
                'load': {
                    'sourceUris': sourceCSV,
                    'schema': {
                        'fields': [
                            {
                                'name': 'sample',
                                'type': 'STRING'
                            },
                            {
                                'name': 'gender',
                                'type': 'STRING'
                            },
                            {
                                'name': 'disease_code',
                                'type': 'STRING'
                            },
                            {
                                'name': 'age_at_initial_pathologic_diagnosis',
                                'type': 'FLOAT'
                            }

                        ]
                    },
                    'destinationTable': {
                        'projectId': projectId,
                        'datasetId': datasetId,
                        'tableId': targetTableId
                    },
                }
            }
        }

        insertResponse = jobCollection.insert(projectId=projectId,
                                              body=jobData).execute()

        # Ping for status until it is done, with a short pause between calls.
        while True:
            job = jobCollection.get(projectId=projectId,
                                     jobId=insertResponse['jobReference']['jobId']).execute()
            if 'DONE' == job['status']['state']:
                print 'Done Loading!'
                return

            if 'errorResult' in job['status']:
                print 'Error loading table: ', pprint.pprint(job)
                return

            print 'Waiting for loading to complete...'
            time.sleep(10)



    except HTTPError as err:
        print 'Error in loadTable: ', pprint.pprint(err.resp)  # or err.reason?


def main():

    client_secrets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'client_secrets.json')

    flow = flow_from_clientsecrets(client_secrets_path,
                                   scope='https://www.googleapis.com/auth/bigquery')
    storage = Storage('bigquery_credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        # Run oauth2 flow with default arguments.
        credentials = tools.run_flow(flow, storage, tools.argparser.parse_args([]))

    http = httplib2.Http()
    http = credentials.authorize(http)


    service = build('bigquery', 'v2', http=http)
    projectId = '982660750330'
    datasetId = 'dataset01'
    targetTableId = 'table01'
    sourceCSV = ['gs://test-authentic-bucket01/clinMut_62_v2.csv']
    loadTable(service, projectId, datasetId, targetTableId, sourceCSV)



if __name__ == '__main__':
    main()