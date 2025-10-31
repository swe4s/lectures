
for hash_size in 100 500 1000 5000 10000; do
    for hash_type in simple polynomial; do
        python h.py rand_words.txt $hash_size $hash_type > rand_${hash_size}_${hash_type}.txt
    done
done
