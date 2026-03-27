def slow_sum(n):
    return sum(range(n))

def fast_sum(n):
    return n * (n - 1) // 2

def test_slow(benchmark):
    result = benchmark(slow_sum, 10_000)
    assert result == fast_sum(10_000)

def test_fast(benchmark):
    result = benchmark(fast_sum, 10_000)
    assert result == slow_sum(10_000)
