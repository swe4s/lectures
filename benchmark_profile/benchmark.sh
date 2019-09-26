search.py 10000 1000 L

search.py 10000 1000 B


#conda install -c conda-forge time
$HOME/miniconda3/envs/swe4s/bin/time search.py 10000 1000 L

$HOME/miniconda3/envs/swe4s/bin/time search.py 10000 1000 B

for i in `seq 1 100000 1000000`; do 
    $HOME/miniconda3/envs/swe4s/bin/time -f '%e\t%M' python grow.py $i
done
