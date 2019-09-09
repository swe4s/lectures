# Sofware Engineering for Scientists Lectures
This is a collection of small Python and Bash scripts used in lecure and course
notes for the Sofware Engineering for Scientists course taught at CU Boulder.

For more information about the course contct Ryan Layer at
ryan.layer@colorado.edu

## Development enviroment
Below is the basic setup for a Linux environment. If you are using a Mac, then
replace the Miniconda3 script with the MacOS version.

```
$ cd $HOME
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh -b
$ . $HOME/miniconda3/etc/profile.d/conda.sh
$ conda update --yes conda
$ conda config --add channels bioconda
$ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc 
$ conda create --yes -n swe4s
$ conda activate swe4s
$ conda install --yes python=3.6
$ conda install -y pycodestyle
```

## Topics

### Unit tests

Based on the Python library `unittest`
