import yaml

with open('../Data/searchData.yml', encoding='utf8') as f:
    # 多组数据使用load_all(),此方法返回一个生成器，需要使用for循环迭代读取每一组数据
    context = yaml.safe_load(f)
    print(context)
