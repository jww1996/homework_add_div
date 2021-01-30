import pytest
import yaml
from homework.calc import Calculator

# 读取文件
with open("./calc.yaml") as f:
    # 用D代表读取的整个yaml文件
    D = yaml.safe_load(f)

    # 读取yaml中加法的测试用例
    """
        加法的测试用例:
            datas：除法的测试用例
            myid1：别名
            
    """
    adddata = D['add']
    add_datas = adddata['datas']
    print(add_datas)
    myid1 = adddata['myid1']
    print(myid1)

    # 读取yaml中除法的测试用例
    """
        除法的测试用例:
            divdatas：除法的测试用例
            myid2：别名
            
    """
    divdata = D['div']
    div_datas = divdata['divdatas']
    print(div_datas)
    myid2 = divdata['myid2']
    print(myid2)


class TestCalc():

    # 在类级别的setup中实例化
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=myid1
    )
    def test_add(self, a, b, expect):
        # 实例化计算器的类
        # calc = Calculator()

        # 调用add方法
        result = self.calc.add(a, b)
        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)

        # 得到结果之后需要写断言
        assert result == expect

    @pytest.mark.parametrize(
        'a, b, expect',
        div_datas, ids=myid2
    )
    # 除法的测试用例
    def test_div(self, a, b, expect):
        # 调用div方法
        result = self.calc.div(a, b)

        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 断言，得到结果后需要写断言
        assert result == expect
