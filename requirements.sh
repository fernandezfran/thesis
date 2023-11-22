#!/bin/bash
# update and upgrade
apt update && apt upgrade -y

# install build-essential to use the make cmd
apt install build-essential -y

# minimal installation of LaTeX: base version and extra packages required
apt install texlive-base -y
apt install texlive-xetex
apt install texlive-fonts-extra -y
apt install texlive-lang-spanish -y
apt install latexmk -y
