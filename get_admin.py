from google.oauth2 import service_account
from googleapiclient.discovery import build
#如何取得json:去google cloud IAM & Admin設定一個自己的帳號（service account）再到keys去獲得自己的憑證（json）

#輸入我自己的帳號憑證，以json匯入，用scopes表示自己需要什麼的權限：需要Cloud platform的
credentials = service_account.Credentials.from_service_account_file(
    'mplus-video-conference-dev-93c2484c9053.json', scopes = ['https://www.googleapis.com/auth/cloud-platform']
)
# build an accessible object
iam_service = build('iam', 'v1', credentials=credentials)

response = iam_service.projects().serviceAccounts().list(
    name='projects/mplus-video-conference-dev'
).execute()

account_list = response['accounts']

iam_account = 0
for account in account_list:
    
    if "iam" in account['email']:
        print(account)
        iam_account+=1

print("There are "+ str(iam_account) + " iam accounts out of "+ str(len(account_list)))
print(f"There are '{iam_account}' iam accounts out of {len(account_list)}。")
    




# use pip install google-auth to acquire google.oauth2
# use pip install google-api-python-client to acquire googleapiclient

