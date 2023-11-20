from google.oauth2 import service_account
from googleapiclient.discovery import build

# 指定你的服務帳戶金鑰 JSON 文件的路徑
SERVICE_ACCOUNT_FILE = 'viewer.json'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.reports.audit.readonly']

def main():
    """Shows basic usage of the Admin SDK Reports API.
    Prints the time, email, and name of the last 10 login events in the domain.
    """
    # 使用服務帳戶金鑰來建立憑證
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # 建立 Admin Reports API 服務
    service = build('admin', 'reports_v1', credentials=creds)

    # Call the Admin SDK Reports API
    print('Getting the last 10 login events')
    results = service.activities().list(userKey='all', applicationName='login', maxResults=10).execute()
    activities = results.get('items', [])

    if not activities:
        print('No logins found.')
    else:
        print('Logins:')
        for activity in activities:
            print(u'{0}: {1} ({2})'.format(activity['id']['time'],
                                           activity['actor']['email'], activity['events'][0]['name']))

if __name__ == '__main__':
    main()





"""import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

credentials_path = 'mplus-video-conference-dev-93c2484c9053.json'

domain = 'taiwanmobile.com'

credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly'])
service = build('admin', 'reports_v1', credentials=credentials)

results = service.activities().list(userKey='all', applicationName='login', maxResults=10).execute()

for r in results:
    print(r)
"""