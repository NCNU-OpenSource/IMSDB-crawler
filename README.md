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

## 開發環境
- Ubuntu 16.04
- Docker version 18.09.6
- Python 3.5

## 套件安裝
### Python
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

## 程式設定 and 執行
### rclone 備份
- Pull image
```
mkdir config
docker run --rm -it -v $(pwd)/config:/config bcardiff/rclone
```
```
No remotes found - make a new one
n) New remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
n/r/c/s/q>n (輸入n)
name> gdrive (可以自取名稱)
Type of storage to configure.
Choose a number from below, or type in your own value
 1 / Amazon Drive
   \ "amazon cloud drive"
 2 / Amazon S3 (also Dreamhost, Ceph, Minio)
   \ "s3"
 3 / Backblaze B2
   \ "b2"
 4 / Dropbox
   \ "dropbox"
 5 / Encrypt/Decrypt a remote
   \ "crypt"
 6 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
 7 / Google Drive
   \ "drive"
 8 / Hubic
   \ "hubic"
 9 / Local Disk
   \ "local"
10 / Microsoft OneDrive
   \ "onedrive"
11 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
12 / SSH/SFTP Connection
   \ "sftp"
13 / Yandex Disk
   \ "yandex"
Storage> 7 (選擇7使用Google Drive)
Google Application Client Id - leave blank normally.
client_id> (按enter即可)
Google Application Client Secret - leave blank normally.
client_secret> (按enter即可)
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine or Y didn't work
y) Yes
n) No
y/n> N (輸入N)
If your browser doesn't open automatically go to the following link: https://accounts.google.com/o/oauth2/auth?client_id=123443211234.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&state=00024d768aaaaaaaaaa8267
```
- 複製上面 link 貼至瀏覽器
- 取得授權碼
- 返回 terminal 貼上授權碼
```
Log in and authorize rclone for access
Enter verification code> 授權碼
#[ketn1201-google-drive]
type = drive
token = {"access_token":"ya29.GlwoB4UL0OqZqqEkL6PZ5XYpp72iumCB7JTe0rvzJVLr5eBl50HBjDfp3rind11LX1ywqGVFtAqYQnIS3EXQxLxmZg-jUi8bDXOp7pS8Wsr0jHtyDgPD0uKsQh4m0w","token_type":"Bearer","refresh_token":"1/7H3aRS9RIHPhMiKJOoL2XcBZ1d4Q-5iEJUMClj17YudSbZ4u6nMMXPGwDHu7bFOk","expiry":"2019-06-14T17:38:39.979031888+08:00"}
team_drive = 0AJQlxhBDCrtLUk9PVA

y) Yes this is OK
e) Edit this remote
d) Delete this remote
y/e/d> y (輸入y)
Current remotes:

Name                 Type
====                 ====
gdrive               drive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q (輸入q)
```
- 申請 check url
  - 請去 https://healthchecks.io/ sign up 申請, 個人提供 : https://hc-ping.com/7069af96-66ed-4787-a0b5-518fb55a62ec
- rclone 設定

- 設定參數 & 執行備份
- 參數說明:
  - `-v`/在本機要共享的資料夾/container 中的資料夾`
  - `-e SC_SRC` 備份來源
  - `-e SYNC_DEST` 備份目的地
  - `-e TZ` 時區設定
  - `-e CRON` 執行備份時間
  - `-e CRON_ABORT` 停止執行備份時間
  - `-e FORCE_SYNC=1` 默認為 1
  - `-e CHECK_URL` 幫助檢查 rclone
```
sudo docker run -idt -v $(pwd)/config:/config -v /path/to/your/directory:/source -e SC_SRC="/source" -e SYNC_DEST="your-google-drive:team-drive" -e TZ="Asia/Taipei" -e CRON="0 0 * * *" -e CRON_ABORT="0 6 * * *" -e FORCE_SYNC=1 -e CHECK_URL=Your check url bcardiff/rclone
```
### build image
- 切換到下載的目錄的檔案
```
sudo docker build --rm -t image_name .
```
- 執行最初的爬網站
```
sudo docker run --rm -dit -v /path/to/Dockershare:/Dockershare -e EXE="main.py" image_name
```
- 檢查每日更新
```
sudo docker run -dit -v /path/to/Dockershare:/Dockershare -e CRON="0 0 * * *" -e EXE="check.py" image_name
```
- 每日爬資源
  - /path/to/dowland-directory/create.sh
  - 修改 path : to download-directory
  - 修改 image_name
 
```
(crontab -e) 30 0 * * * /path/to/dowland-directory/create.sh
```

## 成果展示

## 注意事項

## 參考
- [LSA-1072 Docker](https://docs.google.com/presentation/d/1wYhJkBQkx0jS-oyJG-2imdI7p93wti4XZqR9Jc49PxE/edit?usp=sharing)　

## 分工


