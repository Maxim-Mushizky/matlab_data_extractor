import pytest
from typing import (
    Dict,
    Optional,
    List
)


@pytest.fixture(scope='module')
def matlab_folder_path(p: Optional[str] = None) -> str:
    return r"..\sources\matlab_saved_workspaces"


@pytest.fixture(scope='module')
def matlab_ws_keys(keys: Optional[Dict] = None) -> List:
    return ['data', 'storage', 'ans', 'storage_model', 'storage_obj', 'tester']


@pytest.fixture(scope='module')
def verification_key() -> str:
    return 'tester'
