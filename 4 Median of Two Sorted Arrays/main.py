def solution1(nums1: list[int], nums2: list[int]) -> float:
    merged_list = nums1 + nums2
    merged_list.sort()

    if len(merged_list) % 2 != 0:
        return merged_list[len(merged_list) // 2]

    return (
        merged_list[len(merged_list) // 2 - 1] + merged_list[len(merged_list) // 2]
    ) / 2


def solution2(nums1: list[int], nums2: list[int]) -> float:
    merged_list = nums1 + nums2
    merged_list.sort()

    n_item = len(merged_list)
    mid_point = n_item // 2

    if n_item % 2 != 0:
        return merged_list[mid_point]
    return (merged_list[mid_point - 1] + merged_list[mid_point]) / 2


test_cases = [
    ([1, 3], [2]),
    ([1, 2], [3, 4]),
]

for n1, n2 in test_cases:
    print(solution1(n1, n2))
    print(solution2(n1, n2))
