FROM continuumio/miniconda3:4.7.10

LABEL maintainer="Sergio Bugallo <sergiobugalloenjamio@gmail.com>"

RUN bash -c 'mkdir -p /blackjack/envs'
WORKDIR /blackjack

COPY ./envs/prod.yml /blackjack/envs/prod.yml
RUN conda env create -f /blackjack/envs/prod.yml
RUN echo '. activate blackjack' >> ~/.bashrc

COPY . /blackjack
RUN bash -c '/opt/conda/envs/blackjack/bin/python /blackjack/setup.py install'

CMD [ "/bin/bash" ]