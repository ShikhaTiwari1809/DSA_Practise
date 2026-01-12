from typing import List
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7

        packages.sort()
        n = len(packages)

        # prefix sums of packages for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i, x in enumerate(packages, 1):
            prefix[i] = prefix[i - 1] + x

        max_package = packages[-1]
        best = float("inf")

        for vendor_boxes in boxes:
            # quick reject if this vendor can't fit the largest package
            if max(vendor_boxes) < max_package:
                continue

            vendor_boxes.sort()

            waste = 0
            prev = 0  # how many packages already assigned

            for b in vendor_boxes:
                # find rightmost index of packages that can fit in box size b
                idx = bisect.bisect_right(packages, b)
                if idx <= prev:
                    continue  # this box size doesn't cover any new packages

                # packages[prev:idx] will be packed into box size b
                count = idx - prev
                sum_packages = prefix[idx] - prefix[prev]
                waste += b * count - sum_packages

                prev = idx
                if prev == n:
                    break

            if prev == n:
                best = min(best, waste)

        return -1 if best == float("inf") else best % MOD
