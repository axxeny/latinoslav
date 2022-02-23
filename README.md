<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# What is this repository?

This repository is for two things:

1. Demostrate a good practice Python work pipeline (with unit testing, isolated virtual environment, src and tests separation).

2. An actual project of transliteration of Russian language to latin script. It provides a CLI. I plan to add an HTTP microservice.

# Getting started

This code has been tested with Python 3.10.

Prepare your terminal or shell by activating the virtual environment and installing the necessary packages. Go to this directory by running `cd In this directory:

<table>
    <tr>
        <th>Operating System</th>
        <th>Execute terminal or shell commands</th>
    </tr>

<tr><td>Linux or macOS</td><td>

```bash
python3 -m venv venv
source venv/bin/activate
pip install --requirement requirements.txt
pip install --editable .
```

</td></tr>

<tr><td>Windows PowerShell</td><td>

```bash
python3 -m venv venv
venv\Scripts\Activate.ps1
pip install --requirement requirements.txt
pip install --editable .
```

</td></tr>

<tr><td>Windows cmd.exe</td><td>

```bash
python3 -m venv venv
venv\Scripts\activate.bat
pip install --requirement requirements.txt
pip install --editable .
```

</td></tr>

</table>

# Run tests

Make sure to run the prepare the environment in [Getting started](#getting-started). And then:

```bash
pip install --editable .
pytest
```

# Run CLI

Make sure to run the prepare the environment in [Getting started](#getting-started). And then:

```bash
pip install --editable .
python -m pyrulatin
```

# Reformat code with Black

Make sure to run the prepare the environment in [Getting started](#getting-started). And then:

```bash
black .
```
