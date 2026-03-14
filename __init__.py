import io
import xml.etree.ElementTree as ET
from .util.BinaryRBXL import BinaryRBXL
from .util.DataStream import DataStream
from .util.DataStream import DataStream
from .util.InstanceTree import InstanceTree

def parse(filename):
    isBinaryFormat = False
    with open(filename, 'rb') as f:
        isBinaryFormat = f.read(8) == b'<roblox!'
    root = None
    if isBinaryFormat:
        data = None
        with open(filename, 'rb') as f:
            data = f.read()
        rbxl = BinaryRBXL(DataStream(io.BytesIO(data)))
        root = rbxl.root
    else:
        tree = ET.parse(filename)
        xmlRoot = tree.getroot()
        root = InstanceTree.CreateRoot(root)
        InstanceTree.BuildTree(root, placeRoot)
    return root