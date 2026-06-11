import xml.etree.ElementTree as ET
from .InstanceTree import InstanceTree

class RBXLX:
    def __init__(self, filename):
        tree = ET.parse(filename)
        xmlRoot = tree.getroot()
        self.root = InstanceTree.CreateRoot(xmlRoot)
        self.instances = {}
        InstanceTree.BuildTree(xmlRoot, self.root)
    def getRef(self, refObj):
        if not type(refObj) is list:
            return None
        if len(refObj) != 2:
            return None
        if refObj[0] != "REF":
            return None
        if refObj[1] is None or refObj[1] == self:
            return None
        return self.instances[refObj[1]]