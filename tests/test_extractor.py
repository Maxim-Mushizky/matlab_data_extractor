import pytest
import os

from src.matlab_extractor.extractor import MatlabExtractor

FOLDER_PATH = r"sources\matlab_saved_workspaces"


@pytest.mark.parametrize('matlab_path',
                         [os.path.join(FOLDER_PATH, obj) for obj in os.listdir(FOLDER_PATH) if obj.endswith(".mat")])
def test_extraction(matlab_path, matlab_folder_path, matlab_ws_keys, verification_key):
    assert matlab_path is not None, f"Nothing yielded by search at folder {matlab_folder_path}"
    extracted = MatlabExtractor(matlab_path)
    assert extracted._full_data is not None, "The full data is empty"
    assert extracted.data is not None, "The data is empty"
    for key in extracted.data.keys():
        assert key in matlab_ws_keys, "The key is not part of the test case"

    assert extracted.data[verification_key] == 1, "The flag value must be Matlab true (1)"
