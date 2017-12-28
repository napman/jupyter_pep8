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

* automatically destination file (e.g. 'target.ipynb.pep8.ipynb') will be made
* use '' for filename patterns

## Options

overwrite option can be used to avoid making destination file. It overwrite the original file instead.

```
$ jupyter_pep8 target.ipynb --overwrite

```

Notebook version (3 or 4) can be specified. We have not validate this carefully.

```
$ jupyter_pep8 target.ipynb --version=3

```

## License

BSD

## Author

[Kotaro Nakayama / napman](http://github.com/napman)
