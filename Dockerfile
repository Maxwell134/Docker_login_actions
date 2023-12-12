FROM ubuntu:latest

COPY entrypoint.sh /entrypoint.sh
RUN  sudo apt update -y 
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
