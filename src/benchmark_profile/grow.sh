for i in `seq 1 100000 1000000`; do 
    $HOME/miniconda3/envs/swe4s/bin/time -f '%e\t%M' python grow.py $i
done
