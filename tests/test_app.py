from app.app import deduplicate, add_numbers

def test_deduplicate():
    """测试去重功能"""
    numbers = [1, 2, 2, 3, 4, 4, 5]
    result = deduplicate(numbers)
    assert result == [1, 2, 3, 4, 5]

def test_add_numbers():
    """测试加法功能"""
    result = add_numbers(2, 3)
    assert result == 5
    result = add_numbers(-1, 1)
    assert result == 0