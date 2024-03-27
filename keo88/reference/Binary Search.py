from typing import List

testArr = [1, 2, 3, 5, 5, 7, 8, 9]


def binarySearchLeft(arr: List[int], target: int, left=0, right: int = None):
    if not right:
        right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def binarySearchRight(arr: List[int], target: int, left=0, right: int = None):
    if not right:
        right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def binarySearchAltLeft(arr: List[int], target: int, left=-1, right: int = None):
    if not right:
        right = len(arr) - 1

    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid
    return left


def binarySearchAltRight(arr: List[int], target: int, left=-1, right: int = None):
    if not right:
        right = len(arr) - 1

    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left


print(binarySearchLeft(testArr, 5), binarySearchRight(testArr, 5))
print(binarySearchLeft(testArr, 0), binarySearchRight(testArr, 0))
print(binarySearchLeft(testArr, 1), binarySearchRight(testArr, 1))
print(binarySearchLeft(testArr, 9), binarySearchRight(testArr, 9))
print()
print(binarySearchAltLeft(testArr, 5), binarySearchAltRight(testArr, 5))
print(binarySearchAltLeft(testArr, 0), binarySearchAltRight(testArr, 0))
print(binarySearchAltLeft(testArr, 1), binarySearchAltRight(testArr, 1))
print(binarySearchAltLeft(testArr, 9), binarySearchAltRight(testArr, 9))
