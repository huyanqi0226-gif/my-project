def deduplicate(numbers):
    """去除列表中的重复数字"""
    return list(set(numbers))

def add_numbers(a, b):
    """新增加的加法功能"""
    return a + b

if __name__ == "__main__":
    # 测试去重功能
    numbers = [1, 2, 2, 3, 4, 4, 5]
    result = deduplicate(numbers)
    print(f"去重前: {numbers}")
    print(f"去重后: {result}")
    
    # 测试加法功能
    sum_result = add_numbers(5, 3)
    print(f"5 + 3 = {sum_result}")