curl -L "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr" -o Agrofood_co2_emission.csv
curl -L "https://docs.google.com/uc?export=download&id=1tuoQ9UTW_XRKgBOBaTLtGXh8h0ytKvFp" -o IMF_GDP.csv  


python get_fire_gdp.py "Brazil" "Brazil" > brazil.data

python scatter.py brazil.data brazil.png "Brazil" "CO2" "GDP"
