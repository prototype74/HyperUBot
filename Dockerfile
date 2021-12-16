# Copyright 2021 nunopenim @github
# Copyright 2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

FROM python:3.10
RUN apt-get update
RUN apt-get install -y python3-dev libffi-dev git neofetch ffmpeg flac \
                       iputils-ping net-tools
WORKDIR /root/HyperUBot
COPY ./ ./
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install -r requirements.txt
CMD ["/bin/bash", "./docker_start/start.sh"]
