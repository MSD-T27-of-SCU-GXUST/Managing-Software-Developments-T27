from flask import render_template, request, redirect, url_for
from . import final_testing_bp
import unittest

@final_testing_bp.route('/test', methods=['GET'])
def test():
    # 在这里可以运行测试并返回结果
    test_results = run_tests()
    return render_template('test_results.html', results=test_results)

def run_tests():
    # 执行测试并返回结果
    loader = unittest.TestLoader()
    tests = loader.discover('tests')  # 假设测试文件在 tests 文件夹
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(tests)
    return result
