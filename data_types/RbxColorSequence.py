from .BasicSequence import BasicSequence
from .RbxColorSequenceKeypoint import RbxColorSequenceKeypoint
from .Color3 import Color3

class RbxColorSequence(BasicSequence[RbxColorSequenceKeypoint]):
    @staticmethod
    def FromXML(elem):
        values = elem.text.split(' ')[:-1]
        seq = RbxColorSequence([])
        for i in range(0, len(values)//5):
            idx = i * 5
            item = values[idx:idx+5]
            _time = float(item[0])
            color = Color3(float(item[1]), float(item[2]), float(item[3]))
            seq.addKeypoint(RbxColorSequenceKeypoint(_time, color))
        return seq