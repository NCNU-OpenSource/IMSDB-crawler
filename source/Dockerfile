# 使用官方的 ubuntu 執行環境作為基本的 Docker 影像
FROM ubuntu:latest

MAINTAINER kent1201

LABEL name="movie crawler" description="crontab .py with arguments CRON URL FILE" owner="kent1201"

# 建立 image 時, 傳入參數 
ARG PYTHON_VERSION=python3.5
ARG CRAWLER_VERSION=nltk
ARG CRAWLER_VERSION2=BeautifulSoup4

# 建立 container 時, 傳入參數
# CRON : set crontab
ENV CRON=
# EXE = input exe
ENV EXE=
# URL : input url
ENV URL= 

# 創建工作目錄
RUN mkdir /source \
  && mkdir /Dockershare
WORKDIR /source

# 複製目前目錄下的內容，放進 Docker 容器中
ADD . /source
COPY ./sources.list /etc/apt/sources.list
COPY ./entrypoint.sh /

# 為 shell 添加執行權限
RUN chmod 755 /source/entrypoint.sh

# RUN
RUN apt-get update \
 && apt-get -y install cron \
 && apt-get -y install ${PYTHON_VERSION} \
 && apt-get -y install python3-pip \
 && pip3 install --no-cache --upgrade pip setuptools wheel \
 && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
# && apt-get -y install unixodbc-dev
  
#RUN git clone https://github.com/mkleehammer/pyodbc.git \
# && python3 setup.py build

RUN pip3 install ${CRAWLER_VERSION} \
 && pip3 install ${CRAWLER_VERSION2} \
 && pip3 install requests \
 && pip3 install parse \
 && pip3 install lxml \
 && python3.5 -m nltk.downloader punkt \
 && python3.5 -m nltk.downloader wordnet \
 && python3.5 -m nltk.downloader averaged_perceptron_tagger \
 && python3.5 -m nltk.downloader universal_tagset


RUN service cron start

# 讓 80 連接埠可以從 Docker 容器外部存取
EXPOSE 80

# VOLUME
VOLUME ["/Dockershare"]

#ENTRYPOINT
ENTRYPOINT ["/entrypoint.sh"]

#CMD
CMD [""]
