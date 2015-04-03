from django.shortcuts import render
from apiclient.errors import HttpError
import pprint
from apiclient.discovery import build
import httplib2
import time
import os
from oauth2client.client import flow_from_clientsecrets, AccessTokenRefreshError, SignedJwtAssertionCredentials, GoogleCredentials
# from oauth2client.appengine import OAuth2DecoratorFromClientSecrets
from oauth2client.file import Storage
from oauth2client import tools

# GOOGLE_APPLICATION_CREDENTIALS =

CLIENT_SECRETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'client_secrets.json')
# decorator = OAuth2DecoratorFromClientSecrets(CLIENT_SECRETS_PATH, scope='https://www.googleapis.com/auth/bigquery')


def authorize_credentials():

    flow = flow_from_clientsecrets(CLIENT_SECRETS_PATH, scope='https://www.googleapis.com/auth/bigquery')
    storage = Storage('bigquery_credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        print '\nRun oauth2 flow with default arguments.'
        credentials = tools.run_flow(flow, storage, tools.argparser.parse_args([]))
    else:
        print '\ncredentials valid'

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('bigquery', 'v2', http=http)  # developerKey, model

    return service


def queryTable(service, projectId, datasetId, destinationTableId, queryStr, http=None):
    try:
        jobCollection = service.jobs()
        # note: other instance methods are datasets(), projects(), tabledata(), and tables()
        # https://developers.google.com/resources/api-libraries/documentation/bigquery/v2/python/latest/
        print '\njobCollection'
        print jobCollection
        print '\n'
        jobData = {
            'projectId': projectId,  # why isn't this in jobReference nested object?
            'configuration': {
                'query': {
                    'allowLargeResults': True,
                    'destinationTable': {
                        'datasetId': datasetId,
                        'projectId': projectId,
                        'tableId': destinationTableId,
                    },
                    'query': queryStr
                }
            }
        }

        query_response = jobCollection.insert(projectId=projectId, body=jobData).execute(http)

        print '\nquery_response:'
        print query_response

        # Ping for status until it is done, with a short pause between calls.
        while True:
            job = jobCollection.get(projectId=projectId,
                                     jobId=query_response['jobReference']['jobId']).execute()
            if 'DONE' == job['status']['state']:
                print 'Done Querying!'
                return

            if 'errorResult' in job['status']:
                print 'Error querying table: ', pprint.pprint(job)
                return

            print 'Waiting for query to complete...'
            time.sleep(10)

    except HttpError as err:
        print 'Error in queryTable: ', pprint.pprint(err.resp)  # or err.reason?

    except AccessTokenRefreshError:
        print ("Credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


def authorize_credentials_with_jwt():

    PROJECT_NUMBER = '982660750330'
    SERVICE_ACCOUNT_EMAIL = "982660750330-88vug9a5ojumrrqksb7dndfevb4lg2q9@developer.gserviceaccount.com"

    f = file('Authentication-Test-key.pem', 'rb')  # notasecret
    key = f.read()
    f.close()

    credentials = SignedJwtAssertionCredentials(
        SERVICE_ACCOUNT_EMAIL,
        key,
        scope='https://www.googleapis.com/auth/bigquery')

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('bigquery', 'v2')  # , http=http)

    return service, http


def authorize_credentials_with_Google():
    SCOPES = ['https://www.googleapis.com/auth/bigquery']
    credentials = GoogleCredentials.get_application_default().create_scoped(SCOPES)
    credentials = GoogleCredentials.from_stream('Authentication-Test-key.json')

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('bigquery', 'v2', http=http)

    return service


def bq_home(request):

    service = authorize_credentials_with_Google()

    print '\nservice'
    print service

    projectId = '982660750330'
    datasetId = 'dataset01'
    destinationTableId = 'query_table04'
    queryStr = 'SELECT sample, gender, disease_code from [dataset01.table01] limit 10;'
    queryTable(service, projectId, datasetId, destinationTableId, queryStr)

    return render(request, 'bq_app/bq_home.html')
