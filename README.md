# spacy-model-manager

Command line utility to view, install, and upgrade spaCy models

[![Build Status](https://github.com/carascap/spacy-model-manager/actions/workflows/test_suite.yml/badge.svg?branch=main)](https://github.com/carascap/spacy-model-manager/actions/workflows/test_suite.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/carascap/spacy-model-manager/branch/main/graph/badge.svg)](https://codecov.io/gh/carascap/spacy-model-manager)
[![Twitter Follow](https://img.shields.io/twitter/follow/carascap.svg?style=social&label=Follow)](https://twitter.com/carascap)

Python library and supporting utilities to parse and process PST and mbox email sources.

## Installation

The spacy-model-manager package requires Python 3.7 or newer, and can be installed from the Python Package Index. Installing with **pip** will automatically install all required dependencies. A selection of environments we have tested follows:

*   Ubuntu 18.04LTS and 20.04LTS releases require build-essential, python3, python3-pip, and python3-venv packages
*   macOS 10.14 (and newer) releases require Xcode 11 (or newer), Xcode CLI tools, and Python 3 installed using Homebrew (or your preferred method)
*   Windows 10 releases require Visual Studio Code, Build Tools for Visual Studio, and Python 3 installed using Anaconda 3 (or your preferred method)

We **strongly recommend** you create and activate a Python virtual environment prior to installing spacy-model-manager. With your environment configured and a Python virtual environment created and activated, run the following commands.

Make sure pip is upgraded to the latest version:
```shell
pip install --upgrade pip
```

Install libratom:
```shell
pip install spacy-model-manager
```

## CLI introduction

The spacy-model-manager CLI provides a command line interface to determine which spaCy models are currently installed, install additional models, and remove models. To see available commands, type:

```shell
(venv) user@host:~$ spacy-model -h
```

## Model management

New spaCy releases are generally accompanied by newly trained models. Using different versions of models over the same collection may produce different results. Depending on your workflow and needs, you may wish to install earlier versions of models, upgrade models that were previously installed, or install multiple models. The model command assists with these tasks.

To see a list of available models, type:

```shell
(venv) user@host:~$ spacy-model list
```

To install a specific version of an available model:

```shell
(venv) user@host:~$ spacy-model install en_core_web_sm
```

Note that a request to install a specific version will replace any existing version of that model, even if the existing version is newer.

## License(s)

Logos, documentation, and other non-software products of the CARASCAP team are distributed under the terms of Creative Commons 4.0 Attribution. Software items in CARASCAP repositories are distributed under the terms of the MIT License. See the LICENSE file for additional details.

&copy; 2021, The University of North Carolina at Chapel Hill.

## Development Team and Support

Developed by the CARASCAP team at the University of North Carolina at Chapel Hill.
