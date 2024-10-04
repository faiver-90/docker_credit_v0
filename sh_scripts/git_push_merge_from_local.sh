#!/bin/bash

# Проверка, что передан аргумент
if [ -z "$1" ]; then
  echo "Необходимо указать комментарий для коммита"
  exit 1
fi

# Выполнить commit.sh с комментарием
bash  sh_scripts/commit.sh "$1"

# Выполнить merge.sh
bash sh_scripts/merge.sh