## Development enviroment
Below is the basic setup for a Linux environment. If you are using a Mac, then
replace the Miniconda3 script with the MacOS version.

```
$ cd $HOME
$ cd $HOME
$ curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-x86_64.sh 
$ bash Mambaforge-pypy3-Linux-x86_64.sh.sh
$ mamba update --yes conda
$ mamba config --add channels bioconda
$ mamba create --yes -n swe4s
$ mamba activate swe4s
$ mamba install --yes python=3.6
$ mamba install -y pycodestyle
$ mamba install -y matplotlit
```

## Topics

### Unit tests (`unit_test`)

Based on the Python library `unittest`

### Continuous Integration (`ci`)

Using Travis CI

### Test Driven Developmetn (`tdd`)

Write tests, then write code to satisfy those tests

### Data Visualization (`matplotlib`)

Scatter plot, histogram, and combination plots of random data with matplotlib.

### Data Integration
#### Gene Expression  (`data_integration/gtex`)

Integrate data between files using parallel arrays

### Profiling and benchmarking code (`benchmark_profile`)

Using `cProfile`

### Time Series (`timeseries`)

Importing multiple files from a folder, handling time stamps

### Pandas (`pandas`)
Working with the pandas module to import and analyze data
