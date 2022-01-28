# Session-1
## Introduction
In this session will be configure a Python environment using Poetry and Pyenv in a AWS Linux Server, also will also be reviewed how to debug, profile and use design patterns in a Pythonic way.

## Server Configuration
1. First install the OS updates:
> sudo yum update
2. Then install Git:
> sudo yum install git
3. List Amazon extra packages and search the numbers of Python, EPEL and Java packages:
> sudo amazon-linux-extras list
4. In my case the numbers were 24, 33 and 44. Then we need to install all of them:
> sudo amazon-linux-extras install 24 33 44

## Pyenv and Poetry Configuration
### Pyenv
1. First install the dependencies:
> sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
2. Download and install Pyenv:
> curl https://pyenv.run | bash
3. Export to the Path variables:
```
echo 'export PATH="$PATH:$HOME/.pyenv/bin"' >> ~/.bashrc && \
echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```
4. Reload bash:
> source ~/.bashrc

### Poetry
1. Install poetry:
> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
2. Configure poetry:
> poetry config virtualenvs.in-project true
3. Export to the Path variables:
> echo 'export PATH="$PATH:$HOME/.poetry/bin"' >> ~/.bashrc
4. Reload bash:
> source ~/.bashrc

## Pyenv + Poetry Usage
1. First list the python versions available for Pyenv with the following command:
> pyenv install --list | grep " 3\.[8]"
2. Then install it, in my case I chose the 3.8.5 version:
> pyenv install 3.8.5
3. Set globally:
> pyenv global 3.8.5
4. Make a directory, enter inside and set pyenv locally:
> mkdir new_project && cd new_project & pyenv local 3.8.5
5. Initialize a new poetry project:
> poetry init
6. Open the pyproject.toml file and overwrite the following line:
```
[tool.poetry.dependencies]
python = "^3.8"
```
7. Use the pyenv environment with Poetry:
> poetry env use 3.8.5
8. Install the dependencies:
> poetry install
9. Use poetry shell:
> poetry shell

## PDB commands
```
h: help
w: where
n: next
s: step (steps into function)
c: continue
p: print
l: list
q: quit
```
