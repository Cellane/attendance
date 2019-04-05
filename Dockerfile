FROM selenium/node-chrome

USER root
RUN apt-get -qq update && \
  apt-get install -y python3 python3-pip && \
  pip3 install --upgrade pip && \
  hash -r pip && \
  pip3 install selenium && \
  rm -r /var/lib/apt/lists/*
ADD entrypoint /opt/entrypoint/
USER seluser
