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
- 申請 check url
  - 請去 https://healthchecks.io/ sign up 申請, 個人提供 : https://hc-ping.com/7069af96-66ed-4787-a0b5-518fb55a62ec
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

## 成果展示

## 注意事項

## 參考

## 分工


