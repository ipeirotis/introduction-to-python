#!/usr/bin/python3

import sys
import subprocess
import nbformat

from os import listdir
from os.path import isfile, join


def test_notebooks(path):

    notebooks = [
        f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".ipynb")
    ]

    for notebook in sorted(notebooks):
        print(notebook)
        args = [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout=600",
            join(path, notebook),
        ]
        exit_code = subprocess.check_call(args)
        if exit_code != 0:
            raise AssertionError


def main():
    directory = sys.argv[1]
    test_notebooks(directory)


if __name__ == "__main__":
    main()
