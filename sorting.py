from __future__ import annotations

import argparse
import sys


def sort_numbers(values):
    items = list(values)
    if len(items) < 2:
        return items

    middle = len(items) // 2
    left = sort_numbers(items[:middle])
    right = sort_numbers(items[middle:])
    return _merge(left, right)


def _merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def build_parser():
    parser = argparse.ArgumentParser(
        description="Sort a list of integers with a merge sort implementation."
    )
    parser.add_argument(
        "numbers",
        nargs="*",
        type=int,
        help="Integers to sort. If omitted, a demo list will be used.",
    )
    return parser


def parse_numbers(raw_values):
    return [int(value) for value in raw_values]


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.numbers:
        numbers = args.numbers
    else:
        stdin_text = sys.stdin.read().strip()
        numbers = parse_numbers(stdin_text.split()) if stdin_text else [5, 1, 4, 2, 3]
    print(sort_numbers(numbers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
