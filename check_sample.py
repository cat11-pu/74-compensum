"""check_sample.py：按 sample/values.json 走一圈，打印验收面。"""
import json
import os
import sys

from compensum import Sum


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("sample", "values.json")
    with open(path, encoding="utf-8") as handle:
        spec = json.load(handle)
    naive = Sum()
    for value in spec["values"]:
        naive.add(value)
    compensated = Sum()
    for value in spec["values"]:
        compensated.add(value)
    exact = compensated.exact()
    blob = compensated.persist()
    reborn = Sum()
    restored = reborn.restore(blob)
    naive_error = abs(naive.stats().get("total") - exact)
    compensated_error = compensated.error_bound()
    print("朴素总和 =", naive.stats().get("total"))
    print("补偿总和 =", compensated.stats().get("compensated"))
    print("精确和 =", exact)
    print("朴素误差 =", naive_error)
    print("补偿误差 =", compensated_error)
    print("误差是否在上界内 =", compensated_error <= spec["bound"])
    print("恢复后的计数 =", restored.get("count"))
    print("不变量（补偿和比朴素和更接近精确值） =", compensated_error <= naive_error)
    print("数据个数 =", len(spec["values"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
