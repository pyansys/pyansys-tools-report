"""
PyAnsys Tools Report

Module containing the standardized Report class for PyAnsys projects.
"""
import os
import sys

import scooby

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version("pyansys-tools-report")

def version():
    """Method to return the version of the PyAnsys Report Tool.

    Returns
    -------
    str
        The version of the tool being used.
    """
    return __version__

class Report(scooby.Report):
    """A class for custom scooby.Report."""

    def __init__(
        self,
        additional=None,
        ncol=3,
        text_width=80,
        sort=False,
        gpu=True,
        ansys_vars=None,
        ansys_libs=None,
    ):
        """Generate a :class:`scooby.Report` instance.

        Parameters
        ----------
        additional : list(ModuleType), list(str)
            List of packages or package names to add to output information.
        ncol : int, optional
            Number of package-columns in html table; only has effect if
            ``mode='HTML'`` or ``mode='html'``. Defaults to 3.
        text_width : int, optional
            The text width for non-HTML display modes. Defaults to 80.
        sort : bool, optional
            Alphabetically sort the packages. Defaults to ``False``.
        gpu : bool, optional
            Gather information about the GPU. Defaults to ``True`` but if
            experiencing renderinng issues, pass ``False`` to safely generate
            a report.
        ansys_vars : list of str, optional
            List containing the Ansys environment variables to be reported.
            (e.g. ["MYVAR_1", "MYVAR_2" ...]). Defaults to None.
        ansys_libs : dict {str : str}, optional
            Dictionary containing the Ansys libraries and versions to be reported.
            (e.g. {"MyLib" : "v1.2", ...}). Defaults to None.
        """
        # Mandatory packages
        core = [
            "matplotlib",
            "numpy",
            "pyvista",
            "appdirs",
            "tqdm",
            "pyiges",
            "scipy",
            "grpc",  # grpcio
            "google.protobuf",  # protobuf library
        ]

        if os.name == "linux":
            core.extend(["pexpect"])

        # Optional packages
        optional = ["matplotlib"]
        if sys.version_info[1] < 9:
            optional.append("ansys_corba")

        # Information about the GPU - bare except in case there is a rendering
        # bug that the user is trying to report.
        if gpu:
            from pyvista.utilities.errors import GPUInfo

            try:
                extra_meta = [(t[0], t[1]) for t in GPUInfo().get_info()]
            except:
                extra_meta = ("GPU Details", "error")
        else:
            extra_meta = ("GPU Details", "None")

        # Store the ANSYS vars and libs
        self._ansys_vars = ansys_vars
        self._ansys_libs = ansys_libs

        scooby.Report.__init__(
            self,
            additional=additional,
            core=core,
            optional=optional,
            ncol=ncol,
            text_width=text_width,
            sort=sort,
            extra_meta=extra_meta,
        )

    def project_info(self):
        """Return information regarding the ansys environment and installation.

        Returns
        -------
        str
            The project information (env variables and installation)
        """

        # List installed Ansys
        lines = ["", "Ansys Environment Report", "-" * 79]
        lines = ["\n", "Ansys Installation", "******************"]
        if not self._ansys_libs:
            lines.append("No Ansys installations provided")
        else:
            lines.append("Version   Location")
            lines.append("------------------")
            for key in sorted(self._ansys_libs.keys()):
                lines.append(f"{key}       {self._ansys_libs[key]}")
        install_info = "\n".join(lines)

        env_info_lines = [
            "\n\n\nAnsys Environment Variables",
            "***************************",
        ]
        n_var = 0
        if self._ansys_libs:
            for key, value in os.environ.items():
                if key in self._ansys_vars:
                    env_info_lines.append(f"{key:<30} {value}")
                    n_var += 1
        if not n_var:
            env_info_lines.append("None")
        env_info = "\n".join(env_info_lines)

        return install_info + env_info

    def __repr__(self):
        add_text = "-" * 79 + "\nPyAnsys Software and Environment Report"

        report = add_text + super().__repr__() + self.project_info()
        return report.replace("-" * 80, "-" * 79)  # hotfix for scooby