FROM centos:7
RUN yum update -y
RUN yum install -y python3
RUN yum install -y python3-pip
RUN yum install -y libxslt
RUN yum install -y vim
RUN yum install -y epel-release
RUN yum install -y jq
RUN useradd -ms /bin/bash -d /app appuser
WORKDIR /app
RUN python3 -m venv venv
RUN chown -R appuser:appuser /app
USER appuser
CMD [ "/usr/bin/bash" ]