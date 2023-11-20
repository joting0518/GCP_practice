 # 任務說明：
    *整個專案是為了幫公司建立一個雲端平台的soc監控系統，利用api去抓出所有log，以dashboard的方式進行監控（原來是寄到主管信箱，但監控效果不佳）  
# 主要任務：  
    *閱讀gcp api文件  
    *Google Cloud SDK  
    *iam權限設定  
    *service_account、oauth2金鑰設定  
    *寫程式利用api撈必要資訊  
# 難點：  
    *主管指出gcp的資料不好抓，只能撈到general的而非詳細的資料  
    *公司的proxy設定  
# 功能：
cert.py 查詢存放所有SSL/TLS 證書的地方  
cred_getinfo.py 使用Admin SDK Reports API，並使用https://www.googleapis.com/auth/admin.reports.audit.readonly範圍的功能，用oauth2功能進行認證，可以取得帳號們的logs  
sa_getinfo.py 同上，但用service_account  
post_issue.py 使用 Google Cloud Pub/Sub 服務，其中包括發佈（publish）消息到主題（topic）和訂閱（subscribe）消息，可以獲取pubsub區的消息  
get_admin.py 可以獲取總共有哪些admin帳號                                      
get_log.py 查看log                                    
upload_file.py 上傳file到storage 
