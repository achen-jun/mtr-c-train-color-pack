"""
Copyright (c) 2026 阿晨君.
Licensed under the MIT License.
Author: zyunchen2025@gmail.com
"""

from sys import exit
import os, json
from shutil import copytree, rmtree
import zipfile
# pack_format字典
pack_format = {
    # 1.16
    "1.16.2":6,
    "1.16.3":6,
    "1.16.4":6,
    "1.16.5":6,
    # 1.17
    "1.17":7,
    "1.17.1":7,
    # 1.18
    "1.18":8,
    "1.18.1":8,
    "1.18.2":8,
    # 1.19
    "1.19":9,
    "1.19.1":9,
    "1.19.2":9,
    "1.19.3":12,
    "1.19.4":13,
    # 1.20
    "1.20":15,
    "1.20.1":15,
    "1.20.2":18,
    "1.20.3":22,
    "1.20.4":22
    }

# 1、检查目录
# 1.1、检查tmp
try:
    os.mkdir("tmp")
except:
    rmdir_tmp = input("检测到工作目录下已有tmp，是否删除并重新创建？(y/n or 任意键)")
    if rmdir_tmp == "y":
        rmtree("tmp")
        os.mkdir("tmp")
    else:
        exit()
# 1.2、检查parkup
try:
    os.mkdir("packup")
except:
    rmdir_packup = input("检测到工作目录下已有packup，是否删除并重新创建？(y/n or 任意键)")
    if rmdir_packup == "y":
        rmtree("packup")
        os.mkdir("packup")
    else:
        exit()
# 2、复制src至tmp
copytree('src', 'tmp', dirs_exist_ok=True) # "dirs_exist_ok=True":允许目标目录已存在。
# 3、转换字典为列表
minecraft_releases = list(pack_format.keys())
minecraft_pack_format = list(pack_format.values())
# 4、确认版本
release = input("请输入版本")
# 5、创建文件
for minecraft_releases,minecraft_pack_format in zip(minecraft_releases,minecraft_pack_format):
    # 5.1、修改park.mcmeta
    with open('tmp/pack.mcmeta', 'w') as f:
        json.dump({
            "pack": {
                "pack_format": minecraft_pack_format,
                "description": f"C-train多彩列车包\n作者：阿晨君。版本:V{release}"
            }
        }, f)
    # 5.2、创建zip文件
    with zipfile.ZipFile(f'packup/MTR_C-Train-Color-Park_{minecraft_releases}_{release}.zip', 'w') as zf:
        for root, dirs, files in os.walk('tmp'):
            for file in files:
                path = os.path.join(root, file)
                zf.write(path, arcname=os.path.relpath(path, 'tmp'))
# 打包完成提示
print("打包完成！可在packup目录中查看")