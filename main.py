from tools.json_to_class import *
from tools.base_env import *
import os
import shutil

def copy_json_files(src_folder, dest_folder):
    """
    将源文件夹中的所有 JSON 文件复制到目标文件夹。

    参数:
    src_folder (str): 源文件夹路径。
    dest_folder (str): 目标文件夹路径。11111
    """
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(src_folder):
        # 检查文件是否为 JSON 文件
        if filename.endswith('.json'):
            # 复制文件到目标文件夹
            src_file = os.path.join(src_folder, filename)
            dest_file = os.path.join(dest_folder, filename)
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {filename} to {dest_folder}")
def data_init():
    copy_json_files("data_init", "data")

if __name__ == '__main__':
    # data_init()

    # 假设 JSON 文件的路径为 "data/node.json"，并且 Node 类已经定义
    data = read_json("data/node.json")
    node_instances = json_to_instance(data, Node)
    print(node_instances)
    # 检查转换结果
    for node in node_instances:
        print(node.get_attribute("id"))  # 输出每个 Node 对象的 id 属性
        print(node.get_attribute("node_type"))  # 输出每个 Node 对象的 id 属性
        print(node.get_attribute("has_traffic_light"))  # 输出每个 Node 对象的 id 属性
        print(node.get_attribute("rsu_ids"))  # 输出每个 Node 对象的 id 属性
        print(node.get_attribute("drone_ids"))  # 输出每个 Node 对象的 id 属性
    # 假设 node_instances 是一个包含 Node 类实例的列表
    node_instances[0].set_attribute("node_type", 2)

    json_data = instance_to_json(node_instances, "data/node.json")
    print(json_data)  # 打印 JSON 数据


    print("z" * 32)
    print("m" * 32)
    print("h" * 32)