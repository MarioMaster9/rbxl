import xml.etree.ElementTree as ET
from .InstanceTree import InstanceTree

class RBXLX:
    def __init__(self, filename):
        tree = ET.parse(filename)
        xmlRoot = tree.getroot()
        self.root = InstanceTree.CreateRoot(xmlRoot)
        InstanceTree.BuildTree(xmlRoot, self.root)