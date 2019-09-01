.. _installation:

============
Installation
============

Prerequisites
=============
Prerequisites:

- `conda` (included in Miniconda 3 and Anaconda 3 distributions)

Clone BlackJack's repository
============================

.. code-block:: bash

    git clone https://github.com/sbugallo/BlackJack-MC.git
    cd BlackJack-MC

The following instructions assume that you are located in the root of `BlackJack-MC`.

Install requirements
====================

`conda` is the recommended way for installing all the requirements. You can install `conda` from
`this link <https://docs.conda.io/en/latest/miniconda.html>`_. The following instructions assume that you have
conda installed on your system.

Predefined conda environments for different use cases are provided under `./envs`. There are 2
available environments:

- **dev.yml**: for simple execution usage.
- **prod.yml**: to generate docs, test and develope new features.

You can create a new conda environment as follows:

.. code-block:: bash

    conda env create -f ./envs/{dev.yml | prod.yml}


Usage examples:

.. code-block:: bash

    conda env create -f ./envs/dev.yml
    conda env create -f ./envs/prod.yml

Once our environment is installed, we have to activate it running the following:

.. code-block:: bash

    source activate blackjack

Assuming that you have the environment activated, we install `blackjack` module running:

.. code-block:: bash

    python setup.py install

If you plan to modify de source code, run some tests or generate documentation you should install the module in
development mode:

.. code-block:: bash

    python setup.py develop

This will also install a script that can be run directly in your terminal:

- `TBD`

To see how it works, please go to :ref:`usage` section

Docker
======

To facilitate the usage, a docker image is available at
`https://hub.docker.com/r/sbugallo/blackjack <https://hub.docker.com/r/sbugallo/blackjack>`_ .

Prerequisites
-------------

Prerequisites:

 - `docker` (see `https://docs.docker.com/install/ <https://docs.docker.com/install/>`_)
