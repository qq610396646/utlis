FROM python:3.6
MAINTAINER xiao/CC

# 开放端口
EXPOSE 8000

# 设置环境变量
ENV pypi https://pypi.tuna.tsinghua.edu.cn/simple
ENV DIR /opt/SHCE_NER
ENV BASE_DIR ${DIR}

# 切换工作目录
COPY ./ ${DIR}
WORKDIR ${DIR}

RUN pip install -r requirements.txt -i ${pypi}
RUN chmod a+x app.sh

ENTRYPOINT ["sh", "app.sh"]