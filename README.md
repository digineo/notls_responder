NoTLS Responder
===============

[![Build Status](https://travis-ci.org/digineo/notls_responder.svg?branch=master)](https://travis-ci.org/digineo/notls_responder)

This autoresponder script automatically replies all messages that are sent through an unencrypted connection to your mail server.
The intension for using this script is to raise your communication partners awareness for the risk of using using non-encrypted connections and to propagate the secure transport of emails.

Installation
------------

### Postfix

Download the script and make it executable:

    curl https://raw.github.com/digineo/notls_responder/master/tls_responder.py > /usr/share/postfix/tls_responder.py
    chmod +x /usr/share/postfix/tls_responder.py

Enable TLS and TLS received headers in your `/etc/postfix/main.cf`:

    smtpd_tls_cert_file=/etc/postfix/ssl/<your-certificate>
    smtpd_tls_key_file=/etc/postfix/ssl/<your-private-key>
    smtpd_tls_received_header = yes
    smtpd_tls_security_level = may
    smtp_tls_security_level = may

Update your configuration to send copies of all mails you want to be processed by noTLS responder to a specific alias.
If you use virtual maps, then you may add to your `/etc/postfix/virtual` file:

    your-address@example.com notls-responder

And finally add the following line to your `/etc/aliases` file:

    notls-responder: "|/usr/share/postfix/notls_responder"

Finally you need to rebuild your maps with `postmap` and reload postfix with `postfix reload`.


License
----------

This code is licensed under the the MIT License.
