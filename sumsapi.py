"""sumsapi.py：对外门面（老接口 add 不能改）。"""
from __future__ import annotations

from compensum import Sum


class Accumulator:
    def __init__(self):
        self.sum = Sum()

    def add(self, value: float) -> dict:
        return self.sum.add(value)

    def error_bound(self) -> float:
        return self.sum.error_bound()

    def exact(self) -> float:
        return self.sum.exact()

    def snapshot(self) -> bytes:
        return self.sum.persist()

    def rebuild(self, blob: bytes = None) -> dict:
        return self.sum.restore(blob)
