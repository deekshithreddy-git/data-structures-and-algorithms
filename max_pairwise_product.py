# python3

# naive method
def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    product = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])
    return product

# optimized method
def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    sorted_list = sorted(numbers, reverse=True)
    max_product = sorted_list[0] * sorted_list[1]
    return max_product

if __name__ == '__main__':
    n = int(input())
    # input_numbers = list(map(int, input().split()))
    input_numbers = [int(x) for x in input().split()]
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
