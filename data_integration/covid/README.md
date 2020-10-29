```
git clone https://github.com/nytimes/covid-19-data.git
```

```
wget https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv
```

OR

```
curl "https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv" -o co-est2019-alldata.csv
```

```
python masks.py Illinois > Illinois.out
cat Illinois.out | python scatter.py Illinois.png "Cases Rate" "Frequency or Always Rate"
```
