python hash_functions.py rand_words.txt ascii | python scatter.py ascii_hash_function_rand.png "Hashed word" "Hashed value"

python hash_functions.py rand_words.txt rolling | python scatter.py rolling_hash_function_rand.png "Hashed word" "Hashed value"

python hash_functions.py non_rand_words.txt ascii | python scatter.py ascii_hash_function_non_rand.png "Hashed word" "Hashed value"

python hash_functions.py non_rand_words.txt rolling | python scatter.py rolling_hash_function_non_rand.png "Hashed word" "Hashed value"

for M in $( seq  1000 1000 10000 ); do
    python hash_table.py 10000 ascii linear rand_words.txt $M >  ascii_linear_rand.$M.txt
done

grep insert ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py linear_insert_time.png "Load factor" "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search ascii_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py ascii_search_time.png "Load factor" "Search time"

for M in $( seq  1000 1000 10000 ); do
    python hash_table.py 10000 rolling linear rand_words.txt $M >  rolling_linear_rand.$M.txt
done

grep insert rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py rolling_insert_time.png "Load factor" "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search rolling_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py rolling_search_time.png "Load factor" "Search time"
