# Python example modified from https://cloud.google.com/bigquery/loading-data-into-bigquery
from apiclient.errors import HttpError
import pprint
from apiclient.discovery import build
import httplib2
import time
import os
from oauth2client.client import flow_from_clientsecrets, AccessTokenRefreshError
from oauth2client.file import Storage
from oauth2client import tools
import json


# Loads the table from Google Cloud Storage and prints the table.
def queryTable(service, projectId, datasetId, destinationTableId, queryStr):
    try:
        jobCollection = service.jobs()
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

        query_response = jobCollection.insert(projectId=projectId, body=jobData).execute()

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

def main():

    client_secrets_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'client_secrets.json')

    flow = flow_from_clientsecrets(client_secrets_path, scope='https://www.googleapis.com/auth/bigquery')
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
    destinationTableId = 'query_table02'
    queryStr = 'SELECT sample, gender, disease_code from [dataset01.table01] limit 10;'
    queryTable(service, projectId, datasetId, destinationTableId, queryStr)


if __name__ == '__main__':
    main()

# columns in clinMut_62_v2
# 'sample'
# 'percent_lymphocyte_infiltration'
# 'percent_monocyte_infiltration'
# 'percent_necrosis'
# 'percent_neutrophil_infiltration'
# 'percent_normal_cells'
# 'percent_stromal_cells'
# 'percent_tumor_cells'
# 'percent_tumor_nuclei'
# 'gender'
# 'history_of_neoadjuvant_treatment'
# 'icd_o_3_histology'
# 'prior_dx'
# 'vital_status'
# 'country'
# 'disease_code'
# 'histological_type'
# 'icd_10'
# 'icd_o_3_site'
# 'tumor_tissue_site'
# 'tumor_type'
# 'age_at_initial_pathologic_diagnosis'
# 'days_to_birth'
# 'days_to_initial_pathologic_diagnosis'
# 'year_of_initial_pathologic_diagnosis'
# 'days_to_last_known_alive'
# 'tumor_necrosis_percent'
# 'tumor_nuclei_percent'
# 'tumor_weight'
# 'person_neoplasm_cancer_status'
# 'pathologic_N'
# 'radiation_therapy'
# 'pathologic_T'
# 'race'
# 'days_to_last_followup'
# 'ethnicity'
# 'TP53'
# 'RB1'
# 'NF1'
# 'APC'
# 'CTNNB1'
# 'PIK3CA'
# 'PTEN'
# 'FBXW7'
# 'NRAS'
# 'ARID1A'
# 'CDKN2A'
# 'SMAD4'
# 'BRAF'
# 'NFE2L2'
# 'IDH1'
# 'PIK3R1'
# 'HRAS'
# 'EGFR'
# 'BAP1'
# 'KRAS'
# 'sampleType'
# 'DNAseq_data'
# 'mirnPlatform'
# 'cnvrPlatform'
# 'methPlatform'
# 'gexpPlatform'
# 'rppaPlatform'