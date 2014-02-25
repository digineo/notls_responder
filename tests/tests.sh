#!/bin/bash

basedir=`dirname "$0"`
script=$basedir/../tls_responder.py
status=0

function check {
  echo -n "$1 ... "
  output=`$script < $1`
  if [[ "$output" =~ "$2" ]]; then
    echo "success"
  else
    echo "FAILED"
    status=1
  fi
}

# mails to drop
for file in $basedir/drop/*; do
  check $file "dropped"
done

# mails to reply
for file in $basedir/reply/*; do
  check $file "replied"
done

# everthing done
exit $status
