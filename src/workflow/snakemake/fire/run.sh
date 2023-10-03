wget -O Argrofood_co2_emission.csv 'https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr'
python get_data.py Argrofood_co2_emission.csv Afghanistan Afghanistan.txt
python hist.py Afghanistan.txt Afghanistan Afghanistan.png

python get_data.py Argrofood_co2_emission.csv Albania Albania.txt
python hist.py Albania.txt Albania Albania.png
