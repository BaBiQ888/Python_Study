import unittest

# 定义一个测试类，继承自unittest.TestCase
class TestMathFunctions(unittest.TestCase):
    
    # 测试方法1: 测试两个数相加
    def test_addition(self):
        result = 1 + 2
        self.assertEqual(result, 3)  # 使用断言验证结果是否符合预期

    # 测试方法2: 测试两个数相乘
    @unittest.skip
    def test_multiplication(self):
        result = 2 * 3
        self.assertEqual(result, 6)

    # 测试方法3: 测试除法，注意处理浮点数的误差
    def test_division(self):
        result = 7 / 2
        self.assertAlmostEqual(result, 3.5, places=2)  # 使用近似断言

    # 测试方法4: 测试抛出异常
    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            result = 1 / 0
        

# 如果希望以脚本方式运行测试，可以添加以下代码
if __name__ == '__main__':
    unittest.main()
