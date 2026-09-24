"""compensum.py：求和（基线：朴素浮点累加）。"""
from __future__ import annotations


class Sum:
    def __init__(self):
        self.total = 0.0
        self.count = 0
        self.compensated = None

    def add(self, value: float) -> dict:
        """基线：直接累加，不做补偿。"""
        self.total += value
        self.count += 1
        return {"total": self.total}

    def error_bound(self) -> float:
        raise NotImplementedError("误差界还没实现")

    def exact(self) -> float:
        raise NotImplementedError("精确和还没实现")

    def persist(self) -> bytes:
        raise NotImplementedError("快照还没实现")

    def restore(self, blob: bytes = None) -> dict:
        raise NotImplementedError("重启恢复还没实现")

    def stats(self) -> dict:
        return {"total": self.total, "count": self.count, "compensated": self.compensated}
