import pytest

#setup method comes from conftest.py
@pytest.mark.usefixtures('setup')
class BaseClass:
    pass