python src/hash_functions.py words.txt ascii | python src/histogram.py doc/ascii_hash_function_nonrand_histogram.png "Hashed value" "Freq"

python src/hash_functions.py words.txt rolling | python src/histogram.py doc/rolling_hash_function_nonrand_histogram.png "Hashed value" "Freq"

python src/hash_functions.py data/rand_words.txt ascii | python src/scatter.py doc/ascii_hash_function_rand_scatter.png "Hashed word" "Hashed value"

python src/hash_functions.py data/rand_words.txt rolling | python src/scatter.py doc/rolling_hash_function_rand_scatter.png "Hashed word" "Hashed value"

python src/hash_functions.py data/non_rand_words.txt ascii | python src/scatter.py doc/ascii_hash_function_non_rand_scatter.png "Hashed word" "Hashed value"

python src/hash_functions.py data/non_rand_words.txt rolling | python src/scatter.py doc/rolling_hash_function_non_rand_scatter.png "Hashed word" "Hashed value"

for M in $( seq  1000 1000 10000 ); do
    python src/hash_table.py 10000 ascii linear data/rand_words.txt $M >  ascii_linear_rand.$M.txt
done

grep insert ascii_linear_rand.*.txt | cut -d " " -f2,3 | python src/scatter.py doc/linear_insert_time.png "Load factor" "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search ascii_linear_rand.$M.txt | cut -d " " -f2 | python src/mean.py
done) | python src/scatter.py doc/ascii_search_time.png "Load factor" "Search time"

for M in $( seq  1000 1000 10000 ); do
    python src/hash_table.py 10000 rolling linear data/rand_words.txt $M >  rolling_linear_rand.$M.txt
done

grep insert rolling_linear_rand.*.txt | cut -d " " -f2,3 | python src/scatter.py doc/rolling_insert_time.png "Load factor" "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor " 
    grep search rolling_linear_rand.$M.txt | cut -d " " -f2 | python src/mean.py
done) | python src/scatter.py doc/rolling_search_time.png "Load factor" "Search time"
