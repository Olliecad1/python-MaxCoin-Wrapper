# python-MaxCoin-Wrapper
MaxCoin API wrapper for Python 2.7

![python](https://img.shields.io/badge/python-2.7-blue.svg)

```
$ sudo apt-get install python-requests
```

## Use  
```$ sudo pip install requests ``` 
## If you have pip installed


##  On OSX you can also use 
```sudo easy_install -U requests ```
## if you have easy_install installed.

## Windows
This might help: http://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
## Dependencies
- https://pypi.python.org/pypi/requests


## Step 1

### Git clone the github page


![python](https://img.shields.io/badge/python-2.7-blue.svg)

```
sudo git clone https://github.com/Olliecad1/python-MaxCoin-Wrapper
```

## Step 2

### Change Directory into python-tuxexchange-Wrapper

```
cd python-MaxCoin-Wrapper
```

### Step 3

### Building and Installing the setup file

```
sudo python setup.py build
sudo python setup.py install
```

## Step 4

```
sudo mv maxcoin.py /usr/lib/python2.7/dist-packages/
```

```python

import maxcoin

print maxcoin.GetBlockCount()

print maxcoin.GetBlockHash()

print maxcoin.GetBlock()
```
