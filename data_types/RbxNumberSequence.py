from .BasicSequence import BasicSequence
from .RbxNumberSequenceKeypoint import RbxNumberSequenceKeypoint
from .Color3 import Color3

class RbxNumberSequence(BasicSequence[RbxNumberSequenceKeypoint]):
    @staticmethod
    def FromXML(elem):
        values = elem.text.split(' ')[:-1]
        seq = RbxNumberSequence([])
        for i in range(0, len(values)//3):
            idx = i * 3
            item = values[idx:idx+3]
            _time = float(item[0])
            number = float(item[1])
            seq.addKeypoint(RbxNumberSequenceKeypoint(_time, number))
        return seq