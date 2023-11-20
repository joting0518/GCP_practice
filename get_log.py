from google.cloud import logging

project_id = "mplus-video-conference-dev"

# 初始化 Cloud Logging 客戶端
client = logging.Client(project=project_id)

# 定義日誌過濾器 
filter_str = 'severity=ERROR'


# 檢索日誌記錄
entries = client.list_entries()

# 處理檢索的日誌記錄
count = 0  

for entry in entries:
    
    print(entry)
    print()
    log_data = entry.payload
    print("Log Data:", log_data) #imp info part
    
    
    log_name = entry.log_name
    timestamp = entry.timestamp

    print("Log Name:", log_name)
    print("Timestamp:", timestamp)
    count+=1

    if count >=1:
        break


    

"""
step
下載Google Cloud SDK去登入（注意：目錄在～finder 主目錄，要到那裡才能登入,pwd須在該目錄）
除了api 也可以利用Google Cloud SDK 的 gcloud工具  gcloud auth login 或 gcloud auth activate-service-account（已經設定好的身份）去進行身份驗證
"""


