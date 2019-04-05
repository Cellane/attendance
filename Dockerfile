FROM selenium/node-chrome

USER root

RUN apt update -y
RUN apt install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install selenium

# copy cmd
ADD entrypoint /opt/entrypoint/

USER seluser
