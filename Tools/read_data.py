import os
import yaml


# 获取单个文件中的参数
def package_param_data(filename: str, key1: str, key2: str) -> list:
    list_data = []  # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
    yaml_data = Read_Data(filename).return_data()  # 返回yaml文件读取数据
    for i in yaml_data.keys():
        # list_data.append((i, yaml_data.get(i).get('input_text')))  # list_data中添加参数值
        list_data.append((i, yaml_data.get(i).get(key1), yaml_data.get(i).get(key2)))
    print(list_data)
    return list_data


class Read_Data:
    def __init__(self, file_name: str) -> None:
        self.file_path = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__))) + os.sep + "Data" + os.sep + file_name

    def return_data(self) -> yaml:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data


if __name__ == '__main__':
    package_param_data("searchData.yml", 'input_text', 'key')
