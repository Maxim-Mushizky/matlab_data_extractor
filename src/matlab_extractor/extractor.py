import scipy.io as sio
from pathlib import Path
from typing import (
    Union,
    Dict,
    List
)


class MatlabExtractor:
    matlab_meta_data_keys: List = [
        '__header__',
        '__version__',
        '__globals__'
    ]

    def __init__(self, fpath: Union[str, Path]):
        self._full_data = self.load(fpath)
        self.data = self._pop_meta_data()

    def load(self, fpath: Union[str, Path], **kwargs) -> Dict:
        if not kwargs:
            kwargs['squeeze_me'] = True

        return sio.loadmat(fpath, **kwargs)

    def _pop_meta_data(self) -> Dict:
        full_data: Dict = self._full_data.copy()
        for key in self.matlab_meta_data_keys:
            if key in full_data:
                full_data.pop(key,None)
        return full_data


if __name__ == '__main__':
    f = r"..\..\sources\matlab_saved_workspaces\matlab_saved_ws_1.mat"
    c = MatlabExtractor(f)
    print("h")
