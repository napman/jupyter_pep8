Jupyter PEP8
==============================

## Install

```
$ pip install jupyter_pep8
```

## Usage

```
$ jupyter_pep8 target.ipynb

$ jupyter_pep8 '*.ipynb'

$ jupyter_pep8 './*/*.ipynb'

```

* It automatically generates destination files (e.g. 'target.ipynb.pep8.ipynb').
* use '' for filename patterns.

## Options

Overwrite option can be used to avoid making destination files. It overwrites the original files instead.

```
$ jupyter_pep8 target.ipynb --overwrite

```

Notebook version (3 or 4) can be specified. We have not validate this carefully.

```
$ jupyter_pep8 target.ipynb --version=3

```

## 

[autopep8 and error codes](https://pypi.python.org/pypi/autopep8)

## License

BSD

## Author

[Kotaro Nakayama / napman](http://github.com/napman)
