import pytest


class TestLogin:
    def setup_class(self):
        print("初始化操作开始----->>>>")

    def teardown_class(self):
        print("清理工作开始---->>>>")

    def test_a(self):
        print("执行test_a")
        assert True

    @pytest.mark.usefixtures("login")
    def test_b(self):
        print("执行test_b")

    # 返回值的必需用参数传递
    def test_c(self, orderIm):
        print(orderIm)
        print(type(orderIm))

    # 跳过用例
    @pytest.mark.skipif(True, reason="跳过用例")
    def test_d(self):
        print("skipif跳过测试")

    @pytest.mark.xfail(True, reason="预期失败的用例")
    def test_e(self):
        print("xfail标记预期失败")

    @pytest.mark.parametrize("codes", [3, 6])
    def test_f(self, codes):
        print("当前参数：%s" % codes)

    @pytest.mark.parametrize("name, age", [("李四", "11"), ("张氏", "99")])
    def test_g(self, name, age):
        print("姓名: %s, 年龄: %s" % (name, age))
