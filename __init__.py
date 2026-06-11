import io
from .util.RBXLX import RBXLX
from .util.BinaryRBXL import BinaryRBXL
from .util.DataStream import DataStream

def parse(filename):
    isBinaryFormat = False
    with open(filename, 'rb') as f:
        isBinaryFormat = f.read(8) == b'<roblox!'
    rbxl = None
    if isBinaryFormat:
        data = None
        with open(filename, 'rb') as f:
            data = f.read()
        rbxl = BinaryRBXL(DataStream(io.BytesIO(data)))
    else:
        rbxl = RBXLX(filename)
    return rbxl