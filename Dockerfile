# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE

# You can make the Docker image e.g. with the following command:
#   $ docker build -t thesis-docker .
# and then run
#   $ docker run thesis-docker
# to make the compilation of the thesis and then copying to the actual 
# directory.

# use an ubuntu image base
FROM ubuntu:22.04

# config docker env to install packages in non-interactive mode
ENV DEBIAN_FRONTEND noninteractive

# install required packages
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        texlive-base \
        texlive-xetex \
        texlive-fonts-extra \
        texlive-lang-spanish \
        latexmk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# working dir inside the container
WORKDIR /thesis

# copy the TeX files and the Makefile
COPY src/ .

# compile with Makefile and copy the thesis.pdf file here
CMD ["sh", "-c", "make -C /thesis"]
