cat 1342-0.txt | tr ' ' '\n' |  sed 's/[^a-zA-Z0-9]//g' | grep . | sort -u  > words.txt
