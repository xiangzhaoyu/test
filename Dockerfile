# 从仓库拉取运维Python3.6的基础环境
FROM hub.imgo.tv/library/python:python3.6
# 添加标签说明
LABEL author="xiangzy" email="229893497@qq.com" purpose="控制中心"

# 将当前目录复制到容器的项目目录
WORKDIR /data/apps/test
ADD . /data/apps/test/

ENV LC_ALL="en_US.UTF-8"
ENV LC_CTYPE="en_US.UTF-8"
# 安装 Python等依赖
RUN	apk add --no-cache build-base libffi-dev libxslt-dev openssl-dev mariadb-dev openldap-dev python3-dev

VOLUME /data

CMD ["python", "log1.py"]
