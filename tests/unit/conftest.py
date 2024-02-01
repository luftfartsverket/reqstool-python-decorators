# Copyright © LFV

import os


def get_tests_rootdir() -> str:
    return os.path.dirname(__file__).removesuffix("/unit")
