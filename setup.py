from setuptools import setup

setup(name='jupyter_pep8',
    version='0.1.2',
    description='Apply PEP8 for Jupyter Notebooks',
    url='http://github.com/napman/jupyter_pep8',
    author='Kotaro Nakayama',
    author_email='kotaro.nakayama@gmail.com',
    license='BSD',
    scripts=['bin/jupyter_pep8'],
    install_requires=[
        "click",
        "autopep8",
    ],
    zip_safe=False)
