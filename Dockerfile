FROM ubuntu:latest

COPY entrypoint.sh /entrypoint.sh
RUN  sudo apt update -y && sudo apt install docker.io -y
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
