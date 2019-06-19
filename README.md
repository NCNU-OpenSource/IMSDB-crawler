# IMSDB-crawler
---
# Group 1
# Group member
1. 資工四 104321021 劉肇中
2. 資工四 104321024 蔡旻勳

## 功能
- 使用 docker 建立 crawler-image
- 建立多個 container 高效爬下所有IMSDB的劇本之編劇、類型以及腳本
- 使用 rclone 備份至 google drive
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


