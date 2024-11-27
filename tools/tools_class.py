import json
from pathlib import Path
import os
import shutil

class JsonFileEditor:
    def __init__(self, file_path):
        """初始化编辑器，加载 JSON 文件。

        参数:
        file_path (str): JSON 文件的路径。
        """
        self.file_path = Path(file_path)
        self.data = self.load_json()

    def load_json(self):
        """从文件中加载 JSON 数据。"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_json(self):
        """将修改后的 JSON 数据保存回文件。"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def update_parameter(self, id, param, value):
        """根据给定的 ID 更新特定参数的值。

        参数:
        id (int): 需要更新的对象的 ID。
        param (str): 要更新的参数名。
        value (any): 新的参数值。
        """
        for item in self.data:
            if item['id'] == id:
                item[param] = value
                break
        self.save_json()

    def print_json(self):
        """打印当前的 JSON 数据，以便查看。"""
        print(json.dumps(self.data, indent=4))


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


