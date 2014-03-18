#!/bin/bash

basedir=`dirname "$0"`
script=$basedir/../tls_responder.py

function check {
  echo -n "$1 ... "
  output=$(DRY=1 $script < $1)
  retval=$?

  if [ "$retval" != "0" ]; then
    echo
    echo -en "\e[00;31mInvalid return status ($retval):\e[00m"
    echo $output
  elif [[ "$output" = "$2" ]]; then
    echo "success"
  else
    echo -e "\e[00;31mUnexpected output:\e[00m"
    diff <(echo "$2") <(echo "$output")
    status=1
  fi
}

# mails to drop
check $basedir/drop/adwords.eml           "dropped, disallowed address"
check $basedir/drop/facebook.eml          "dropped, disallowed header: X-Auto-Response-Suppress"
check $basedir/drop/locally_delivered.eml "dropped, locally delivered"
check $basedir/drop/mailer_daemon2.eml    "dropped, disallowed address"
check $basedir/drop/mailer_daemon.eml     "dropped, disallowed header: Auto-Submitted"
check $basedir/drop/mediawiki.eml         "dropped, disallowed header: X-Mailer"
check $basedir/drop/no_subject.eml        "dropped, subject missing"
check $basedir/drop/with_tls.eml          "dropped, sent with tls"
check $basedir/drop/same_adress.eml       "dropped, same mail adress as sender"


# mails to reply
mail=$(cat $basedir/email/reply.eml)
check $basedir/reply/no_tls.eml          "$mail"

# everthing done
exit $status
