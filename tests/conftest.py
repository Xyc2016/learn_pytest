import os
import shutil
import tempfile

import pytest


@pytest.fixture(scope="module")
def fixture_scope_module():
    return "_fixture_scope_module"


@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)
