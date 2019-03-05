#!/usr/bin/env python3

"""requirements2setup.py

    Convert requirements.txt into a list that can be pasted into "install_requires" found in setup.py

    MIT License

    Copyright (c) 2019 Jacek Artymiak

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import argparse
import os.path
import sys


def convert_requirements(path: str):
    with open(path, "r") as requirements_fd:
        requirements = requirements_fd.read()
        rl = "\n".join(["\"{}\",".format(line) for line in requirements.split("\n") if line != ""])
        sys.stdout.write("{}".format(rl))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="convert requirements.txt into a list that can be used with setup.py")
    parser.add_argument("-r",
                        help="path to requirement.txt, will look for it in the present working directory, if omitted",
                        type=str, required=False)

    args = parser.parse_args()

    requirements_txt_path = args.r
    if not requirements_txt_path:
        requirements_txt_path = "./requirements.txt"

    convert_requirements(os.path.expanduser(requirements_txt_path))

    sys.exit(0)
