.. _ref_user_guide:

User guide
============

This section explains how to use ``pyansys-tools-report`` and its features.

Using PyAnsys Tools Report
--------------------------

Once the ``pyansys-tools-report`` package is installed in your own personal environment (if not, please proceed
to :ref:`ref_getting_started`), you can start importing the package and using it.

In order to import the package, please run:

.. code:: python

    import ansys.tools.report as pyansys_report

The ``pyansys-tools-report`` contains a main class called ``Report``. This class is basically an extension of the
``scooby.Report``, but customized for showing Ansys libraries and variables in a common format.

The possible arguments that the ``Report`` class accepts can be found in the :ref:`ref_index_api`. PLease, have a look
at it to understand the arguments you may use. A simple example of Ansys variables and libraries is shown below.

.. code:: python

    # After defining my_ansys_libs and my_ansys_vars with the needed format (see API Reference)
    # we can start the instantiation of the report
    #
    # Instantiate a Report object
    rep = report.Report(ansys_libs=my_ansys_libs, ansys_vars=my_ansys_vars)

    # For printing the report
    rep

The typical output of a ``Report`` would look as follows:

.. code-block:: text
    
    >>> -------------------------------------------------------------------------------
    >>> PyAnsys Software and Environment Report
    >>> -------------------------------------------------------------------------------
    >>>   Date: Thu Jun 02 10:16:04 2022 CEST
    >>> 
    >>>                 OS : Linux
    >>>             CPU(s) : 16
    >>>            Machine : x86_64
    >>>       Architecture : 64bit
    >>>        Environment : Python
    >>>        GPU Details : ...
    >>> 
    >>>   Python 3.8.10 (default, Mar 15 2022, 12:22:08)  [GCC 9.4.0]
    >>> 
    >>>         matplotlib : 3.5.1
    >>>              numpy : 1.22.3
    >>>            pyvista : 0.34.1
    >>>            appdirs : 1.4.4
    >>>               tqdm : ...
    >>>             pyiges : ...
    >>>              scipy : ...
    >>>                   ...
    >>>
    >>>
    >>> -------------------------------------------------------------------------------
    >>> Ansys Environment Report
    >>> -------------------------------------------------------------------------------
    >>> 
    >>> 
    >>> Ansys Installation
    >>> ******************
    >>> Version   Location
    >>> ------------------
    >>> MyLib1       v1.2
    >>> MyLib2       v1.3
    >>> 
    >>> 
    >>> Ansys Environment Variables
    >>> ***************************
    >>> MYVAR_1                        VAL_1
    >>> MYVAR_2                        VAL_2


By default, the ``Report`` class would look for a certain set of environment variables. The following
strings are searched for in the available environment variables. If any match is found, they are included
in the report:

* ``AWP_ROOT``
* ``ANS``
* ``MAPDL``
* ``FLUENT``
* ``AEDT``
* ``DPF``

If you want the ``Report`` class to look for some extra environment variables by default, please
`raise an issue <https://github.com/pyansys/pyansys-tools-report/issues>`_.

Enjoy its use. If you have any doubts, please raise a question/issue in the 
`PyAnsys Tools Report Issues <https://github.com/pyansys/pyansys-tools-report/issues>`_ site.