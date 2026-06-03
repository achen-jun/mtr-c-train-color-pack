import os

# pack_format值
# ----
# minecraft_releases = list(pack_format.keys())
# minecraft_pack_format = list(pack_format.values()) # 1-12:只是方便未来可以简单添加而已
# print(minecraft_pack_format)
# print(minecraft_releases)
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

os.mkdir("tmp")