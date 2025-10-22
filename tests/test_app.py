import sys
import os

# 添加项目根目录到 Python 路径，这样就能找到 app 模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import deduplicate, add_numbers

def test_deduplicate():
    """测试去重功能"""
    numbers = [1, 2, 2, 3, 4, 4, 5]
    result = deduplicate(numbers)
    # 因为去重后顺序可能变化，我们检查内容和长度
    assert len(result) == 5
    assert set(result) == {1, 2, 3, 4, 5}

def test_add_numbers():
    """测试加法功能"""
    result = add_numbers(2, 3)
    assert result == 5
    result = add_numbers(-1, 1)
    assert result == 0