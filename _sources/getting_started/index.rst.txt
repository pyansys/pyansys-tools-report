.. _ref_getting_started:

Getting started
===============

To install ``pyansys-tools-report``, carefully read all instructions on this page.

Installation
------------

This package may be installed following two procedures: either the pip package manager installation or
the manual installation. The process to be followed for each of them is shown in the upcoming sections.

The ``pyansys-tools-report`` package currently supports Python >=3.7 on Windows, Mac OS, and Linux.

Install the latest release from `PyPi <https://pypi.org/project/pyansys-tools-report>`_ with:

.. code:: bash

   pip install pyansys-tools-report


Alternatively, install the latest from GitHub via:

.. code:: bash

   pip install git+https://github.com/pyansys/pyansys-tools-report.git


For a local "development" version, install with (requires pip >= 22.0):

.. code:: bash

   git clone https://github.com/pyansys/pyansys-tools-report.git
   cd pyansys-tools-report
   pip install .

Offline installation
--------------------

If you lack an internet connection on your install machine, the recommended way
of installing PyAnsys Tools Report is downloading the wheelhouse archive from the
`Releases Page <https://github.com/pyansys/pyansys-tools-report/releases>`_ for your
corresponding machine architecture.

Each wheelhouse archive contains all the python wheels necessary to install
PyAnsys Tools Report from scratch on Windows and Linux for Python >=3.7. You can install
this on an isolated system with a fresh python or on a virtual environment.

For example, on Linux with Python 3.7, unzip it and install it with the following:

.. code:: bash

   unzip pyansys-tools-report-v0.2.dev0-wheelhouse-Linux-3.7.zip wheelhouse
   pip install pyansys-tools-report -f wheelhouse --no-index --upgrade --ignore-installed


If you're on Windows with Python 3.9, unzip to a ``wheelhouse`` directory and
install using the same command as before.

Consider installing using a `virtual environment <https://docs.python.org/3/library/venv.html>`_.
More information on general PyAnsys development can be found in the
`PyAnsys Developer's Guide <https://dev.docs.pyansys.com/>`_.

How does it work?
-----------------

This repository basically contains a simple Python package which you can import as follows
(once installed):

.. code:: python

    import ansys.tools.report as pyansys_report


Once imported, you can then start playing around with it:

.. code:: python

    # Instantiate a "default" Report
    rep = pyansys_report.Report()

Refer to the :ref:`ref_index_api` to see the details of the module.
