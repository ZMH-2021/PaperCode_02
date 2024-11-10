import json


def instance_to_json(instances, filename=None):
    """
    将类实例列表转换为 JSON 格式的数据，并选择性地写入到指定的文件。

    参数:
    instances (list): 类实例的列表。
    filename (str): 可选参数，如果指定，则将 JSON 数据写入该文件。

    返回:
    str: JSON 格式的字符串，表示所有实例的属性数据。
    """
    data_list = []
    for instance in instances:
        # 将实例的属性转为字典形式
        instance_dict = instance.__dict__
        data_list.append(instance_dict)

    json_data = json.dumps(data_list, indent=4, ensure_ascii=False)

    # 如果指定了文件名，则将 JSON 数据写入文件
    if filename:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(json_data)
            print(f"Data successfully written to {filename}")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    return json_data


def read_json(filename):
    """
    读取指定的 JSON 文件，并返回其中的全部数据。

    参数:
    filename (str): JSON 文件的文件名

    返回:
    dict: JSON 文件中的全部数据
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {filename} could not be decoded.")
        return None


def json_to_instance(data, class_type):
    """
    将 JSON 数据转换为指定类的对象实例列表。

    参数:
    data (dict or list): JSON 文件读取的全部数据，通常是一个包含对象信息的列表。
    class_type (type): 目标类的类型，例如 Node、TrafficLight 等。

    返回:
    list: 包含使用 JSON 数据初始化的类实例的列表。
    """
    ret = []
    if isinstance(data, dict) and "nodes" in data:
        data = data["nodes"]  # 如果 JSON 数据中存在 'nodes' 键，将其解析为节点数据列表

    for item in data:
        try:
            # 通过字典解包的方式，将 JSON 数据映射到指定的类的属性
            instance = class_type(**item)
            ret.append(instance)
        except TypeError as e:
            print(f"Error initializing {class_type.__name__} with data {item}: {e}")

    return ret


