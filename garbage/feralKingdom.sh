#!/usr/bin/zsh

mail() {
    POP3=pop.gmail.com
    USER=your_email@gmail.com
    PASS=your_password
    LIST=$(openssl s_client -connect $POP3:995 2>/dev/null | sed -n '/^.*OK.*/{s///;s/ //g;p}')
    for i in $LIST; do
        BODY=$(openssl s_client -connect $POP3:995 -quiet -starttls pop3 -crlf -ign_eof | sed -n "/^.[01]00/,/^.[23]00/{/^.[12]00/!{p;q};p}")
        ATTACH=$(echo $BODY | grep -o 'Content-Type:.*name=[^"]*')
        if [ -z "$ATTACH" ]; then
            openssl s_client -connect $POP3:995 -quiet -starttls pop3 -crlf -ign_eof | sed -n "/^.[01]00/,/^.[23]00/{/^.[12]00/!{p;q};p}" | sed 's/^.. //' | grep -v '^\.\.' | grep -v '^\.$' | sed 's/^/DELE /' | openssl s_client -connect $POP3:995 -quiet -starttls pop3 -crlf -ign_eof
        else
            for j in $ATTACH; do
                FILE=$(echo $j | sed 's/.*name=//' | sed 's/".*$//')
                if [ "$FILE" == "mp3" ]; then
                    openssl s_client -connect $POP3:995 -quiet -starttls pop3 -crlf -ign_eof | sed -n "/^.[01]00/,/^.[23]00/{/^.[12]00/!{p;q};p}" | sed 's/^.. //' | grep -v '^\.\.' | grep -v '^\.