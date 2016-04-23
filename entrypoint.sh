#!/usr/bin/bash
function generate_passwd_file() {
  export USER_ID=$(id -u)
  export GROUP_ID=$(id -g)
  #  grep -v ^python /etc/passwd > "/var/lib/extrausers/passwd"

  echo "python:x:${USER_ID}:${GROUP_ID}:Python Server:${HOME}:/bin/bash" >> /var/lib/extrausers/passwd
}

generate_passwd_file


python app.py
