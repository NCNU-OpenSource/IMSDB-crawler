# IMSDB-crawler
---
# Group 1
# Group member
1. 資工四 104321021 劉肇中
2. 資工四 104321024 蔡旻勳

## 功能
- 使用 docker 建立 crawler-image
- 建立多個 container 高效爬下所有IMSDB的劇本之編劇、類型以及腳本
- 使用 bcardiff/rclone image 備份至 google drive
- 定時從網站更新內容
- 文字分析並統計

![gen](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/IMSDB_genre.png)
![scr](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/IMSDB_word.png)
## 開發環境
- Ubuntu 16.04
- Docker version 18.09.6
- Python 3.5

## 套件安裝
### Python
### nltk(Natural Language Tool Kit)
```
pip3 install nltk
python3 -m nltk.downloader punkt
python3 -m nltk.downloader wordnet
```
### Docker
- set up the repository
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent       software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"

```
- install docker-ce
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-cache madison docker-ce
```

## 主要程式介紹
-main.py : 將[IMSDB](https://www.imsdb.com/alphabetical/A)之URL做成list
-crawl_script.py : 爬傳入URL中的資料(名稱、類別、腳本...)
-create.sh : 將list中之URL傳給crawl_script.py 
-check.py : 每日定時檢查是否有新電影劇本上架，有則呼叫crawl_script.py


## 程式設定 and 執行
### nltk
```
def main():
    count = 1
    sen = "has was is he his playing ... played happier ? "
    lemmatizer = WordNetLemmatizer()
    words_list = nltk.word_tokenize(sen)
    word_list = nltk.pos_tag(words_list,tagset='universal')
    for words in word_list:
        if words[1] != '.':
            print(words[0],end = ' ->')
            word =lemmatizer.lemmatize( words[0], pos= 'v' ) 
            print (lemmatizer.lemmatize( word ) ,end = ' ')
            print(words[1])
```
![nltk](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/nltk_image.png)


### rclone 備份
- Pull image
```
mkdir config
docker run --rm -it -v $(pwd)/config:/config bcardiff/rclone
```
```
INFO: No SYNC_SRC and SYNC_DEST found. Starting rclone config
2019/06/19 13:46:18 NOTICE: Config file "/config/rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> kent1201-google-drive
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / A stackable unification remote, which can appear to merge the contents of several remotes
   \ "union"
 2 / Alias for a existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Dropbox
   \ "dropbox"
 9 / Encrypt/Decrypt a remote
   \ "crypt"
10 / FTP Connection
   \ "ftp"
11 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
12 / Google Drive
   \ "drive"
13 / Hubic
   \ "hubic"
14 / JottaCloud
   \ "jottacloud"
15 / Koofr
   \ "koofr"
16 / Local Disk
   \ "local"
17 / Mega
   \ "mega"
18 / Microsoft Azure Blob Storage
   \ "azureblob"
19 / Microsoft OneDrive
   \ "onedrive"
20 / OpenDrive
   \ "opendrive"
21 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
22 / Pcloud
   \ "pcloud"
23 / QingCloud Object Storage
   \ "qingstor"
24 / SSH/SFTP Connection
   \ "sftp"
25 / Webdav
   \ "webdav"
26 / Yandex Disk
   \ "yandex"
27 / http Connection
   \ "http"
Storage> 12 (選擇12使用Google Drive)
** See help for drive backend at: https://rclone.org/drive/ **
Google Application Client Id
Setting your own is recommended.
See https://rclone.org/drive/#making-your-own-client-id for how to create your own.
If you leave this blank, it will use an internal key which is low performance.
Enter a string value. Press Enter for the default ("").
client_id> (Enter)
Google Application Client Secret
Setting your own is recommended.
Enter a string value. Press Enter for the default ("").
client_secret> (Enter)
Scope that rclone should use when requesting access from drive.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Full access all files, excluding Application Data Folder.
   \ "drive"
 2 / Read-only access to file metadata and file contents.
   \ "drive.readonly"
   / Access to files created by rclone only.
 3 | These are visible in the drive website.
   | File authorization is revoked when the user deauthorizes the app.
   \ "drive.file"
   / Allows read and write access to the Application Data folder.
 4 | This is not visible in the drive website.
   \ "drive.appfolder"
   / Allows read-only access to file metadata but
 5 | does not allow any access to read or download file content.
   \ "drive.metadata.readonly"
scope> 1
ID of the root folder
Leave blank normally.
Fill in to access "Computers" folders. (see docs).
Enter a string value. Press Enter for the default ("").
root_folder_id> 
Service Account Credentials JSON file path 
Leave blank normally.
Needed only if you want use SA instead of interactive login.
Enter a string value. Press Enter for the default ("").
service_account_file> 
Edit advanced config? (y/n)
y) Yes
n) No
y/n> n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No
y/n> n
If your browser doesn't open automatically go to the following link: https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=202264815644.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&state=841997832a956e419f6690addc02ead5
Log in and authorize rclone for access
```
- 複製上面 link 貼至瀏覽器
- 取得授權碼
- 返回 terminal 貼上授權碼
```
Log in and authorize rclone for access
Enter verification code> 4/bQFzBS6Kwr986Q6r_cnREuNh2gLvB5TUOjTCF6TjP6PL-mCG6CxLU6sJF0
Configure this as a team drive?
y) Yes
n) No
y/n> y
Fetching team drive list...
Choose a number from below, or type in your own value
 1 / 1071 LSA 第六組
   \ "0AKdXyui8JclVyUk9PVA"
 2 / 1072-LSA 
   \ "0AJQlxhBDCrtDLUk9PVA"
 3 / LAB307
   \ "0ABgbXs4H5t2I5UkG9PVA"
Enter a Team Drive ID> 2
--------------------
[kent1201-google-drive]
type = drive
scope = drive
token = {"access_token":"ya29.GlssdB5bjJ3c-iRWPfiATPrmMcr74ejkPOyidw01cLd_ewWqdKWwFEDIkjuxD_NX3PglETenoRYRq2pPw9LhtWiOlc0euHg_-L9dXTfCl7o8hSQI_2pV1fEMqsl_Wj2","token_type":"Bearer","refresh_token":"1/Cgzoe4lvzpjAvFjLmpNLenTh6_J2cf5Swl6x-AUoUB5G8yvj6RUCshTjsAcA4eEgZ","expiry":"2019-06-19T14:51:15.356901904Z"}
team_drive = 0AJQSlxhBDCrtLUWk9PVA
--------------------
) Yes this is OK
e) Edit this remote
d) Delete this remote
y/e/d> y
Current remotes:

Name                 Type
====                 ====
kent1201-google-drive drive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
INFO: Define SYNC_SRC and SYNC_DEST to start sync process.

```
- 申請 check url
  - 請去 https://healthchecks.io/ sign up 申請, 個人提供 : https://hc-ping.com/7069af96-66ed-4787-a0b5-518fb55a62ec
- rclone 設定

- 設定參數 & 執行備份
- 參數說明:
  - `-v`/在本機要共享的資料夾/container 中的資料夾`
  - `-e SYNC_SRC` 備份來源
  - `-e SYNC_DEST` 備份目的地
  - `-e TZ` 時區設定
  - `-e CRON` 執行備份時間
  - `-e CRON_ABORT` 停止執行備份時間
  - `-e FORCE_SYNC=1` 默認為 1
  - `-e CHECK_URL` 幫助檢查 rclone
```
sudo docker run -idt -v $(pwd)/config:/config -v /path/to/your/directory:/source -e SYNC_SRC="/source" -e SYNC_DEST="your-google-drive:team-drive" -e TZ="Asia/Taipei" -e CRON="0 1 * * *" -e CRON_ABORT="0 6 * * *" -e FORCE_SYNC=1 -e CHECK_URL=Your check url bcardiff/rclone
```
### build image
- 切換到下載的目錄
```
sudo docker build --rm -t image_name .
```
- Pull image from docker hub
```
sudo docker pull 104321024/imsdb-crawler
```
- 執行最初的爬網站
```
sudo docker run --rm -dit -v /path/to/Dockershare:/Dockershare -e EXE="main.py" 104321024/imsdb-crawler or your_image_name
```
- 檢查每日更新
```
sudo docker run -dit -v /path/to/Dockershare:/Dockershare -e CRON="0 0 * * *" -e EXE="check.py" 104321024/imsdb-crawler or your_image_name
```
- 每日爬資源
  - /path/to/download-directory/create.sh
  - 修改 path : to download-directory
  - 修改 image_name
 
```
(crontab -e) 30 0 * * * /path/to/download-directory/create.sh
```

## 成果展示
![list](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/list.png)
![crawler](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/crawler.png)
![analyze](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/analyze.png)
![rclone](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/rclone.png)
![drive1](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/drive1.png)
![drive2](https://github.com/NCNU-OpenSource/IMSDB-crawler/blob/master/%E6%88%90%E6%9E%9C%E5%B1%95%E7%A4%BA/drive2.png)


## 注意事項
1. crontab 請使用絕對路徑
2. 使用前請先檢查路徑
3. Dockershare 為預設 container 之間共享，更動前請注意 
4. 注意 shell or .py 是否給予執行權限
5. 進入執行中的 container `sudo docker exec -it container CMD`
6. 給予 Docker 權限 `sudo usermod -a -G docker $USER`
7. 查看 container logs or error `docker logs -f container_id`
8. 一次清理大量停止 container `sudo docker container prune`

## 未來改進
- 目前由於安裝套件 pyodbc 的問題與時間緣故，無法進行連線資料庫

## 參考
- [LSA-1072 Docker](https://docs.google.com/presentation/d/1wYhJkBQkx0jS-oyJG-2imdI7p93wti4XZqR9Jc49PxE/edit?usp=sharing)　
- [bcardiff/rclone](https://hub.docker.com/r/bcardiff/rclone/)
- [鳥哥的私房菜](http://linux.vbird.org/)
- [docker push image](https://docs.docker.com/v17.12/docker-cloud/builds/push-images/)

## 分工
- 104321021 劉肇中 : 撰寫核心爬蟲程式 main.py, check.py, crul_script.py
- 104321024 蔡旻勳 : 建立 docker image 相關, rclone 備份雲端


