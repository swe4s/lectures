cat Pride_and_Prejudice.txt | tr ' ' '\n' |  sed 's/[^a-zA-Z0-9]//g' | grep . | sort -u  > Pride_and_Prejudice.words.txt
