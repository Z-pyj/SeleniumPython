import os
import yaml


class Read_Data:
    def __init__(self, file_name):
        self.file_path = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__))) + os.sep + "Data" + os.sep + file_name
        print(self.file_path)

    def return_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            print(data)
            return data

    def return_datas(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            context = yaml.load_all(f, Loader=yaml.FullLoader)
            for i in context:
                print(i)


    def package_param_data(self, funcCase, case):
        list_data = []  # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
        yaml_data = Read_Data(self.file_path).return_data()[funcCase]  # 返回yaml文件读取数据
        for i in yaml_data.keys():
            list_data.append((i, yaml_data.get(i).get(case)))  # list_data中添加参数值
        print(list_data)
        return list_data



if __name__ == '__main__':
    Read_Data("searchData.yml").return_data()
    # package_param_data("searchData.yml", "search_text", "input_text")
