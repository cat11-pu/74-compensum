"""compensum.py：求和（Neumaier 补偿累加）。"""
from __future__ import annotations

import json
from fractions import Fraction


class Sum:
    def __init__(self):
        self.total = 0.0
        self.compensation = 0.0
        self.count = 0
        self._values = []

    def add(self, value: float) -> dict:
        """Neumaier 补偿累加；返回结构保持 {"total": ...} 不变。"""
        advanced = self.total + value
        if abs(self.total) >= abs(value):
            self.compensation += (self.total - advanced) + value
        else:
            self.compensation += (value - advanced) + self.total
        self.total = advanced
        self.count += 1
        self._values.append(value)
        return {"total": self.total}

    def error_bound(self) -> float:
        """补偿和与精确和之差的绝对值。"""
        return abs((self.total + self.compensation) - self.exact())

    def exact(self) -> float:
        """用 Fraction 求精确和并转成浮点。"""
        return float(sum((Fraction(v) for v in self._values), Fraction(0)))

    def persist(self) -> bytes:
        """落盘快照：累加值、补偿项、计数与历史值。"""
        payload = {
            "total": self.total,
            "compensation": self.compensation,
            "count": self.count,
            "values": self._values,
        }
        return json.dumps(payload).encode("utf-8")

    def restore(self, blob: bytes = None) -> dict:
        """从快照恢复，状态与重启前一致。"""
        payload = json.loads(blob.decode("utf-8"))
        self.total = payload["total"]
        self.compensation = payload["compensation"]
        self.count = payload["count"]
        self._values = list(payload["values"])
        return {"total": self.total, "count": self.count}

    def stats(self) -> dict:
        return {
            "total": self.total,
            "count": self.count,
            "compensated": self.total + self.compensation,
        }
