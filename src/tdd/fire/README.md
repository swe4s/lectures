```
wget -O Agrofood_co2_emission.csv  "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"
wget -O IMF_GDP.csv  "https://docs.google.com/uc?export=download&id=1tuoQ9UTW_XRKgBOBaTLtGXh8h0ytKvFp"

python get_fire.py \
    Agrofood_co2_emission.csv 1 2 3 \
    IMF_GDP.csv \
    Albania \
    Albania_fire_gdp.txt 
    
python scatter.py Albania_fire_gdp.txt Albania_fire_gdp.png Albania Fires GDP
```
