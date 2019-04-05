FROM selenium/node-chrome

USER root

RUN apt-get update -y && \
  apt-get install -y python3 python3-pip && \
  pip3 install --upgrade pip && \
  pip3 install selenium && \
  rm -r /var/lib/apt/lists/*

# copy cmd
ADD entrypoint /opt/entrypoint/

USER seluser
