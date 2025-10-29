def sum_negative_between_min_max(arr):
    if not arr:
        return 0
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    start, end = sorted([min_idx, max_idx])
    return sum(x for x in arr[start+1:end] if x < 0)


if __name__ == "__main__":
    A = [3, -1, -2, 5, -4, 6, -2]
    result = sum_negative_between_min_max(A)
    print(f"Сумма отрицательных между min и max: {result}")
