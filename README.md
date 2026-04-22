# C-Train多彩列车包

为[Minecraft-Transit-Railway](https://github.com/Minecraft-Transit-Railway/Minecraft-Transit-Railway) MOD中的C-Train设计的资源包，增加更多腰线颜色。

![](assets/front-display.png)

## 增添更多颜色：

在原版C-Train红色腰线的贴图为基础，新增了7种颜色：

- 绿色：森林绿`#228B22`

- 深蓝色：深海蓝`#0000FF`

- 浅蓝色：天空蓝`#00a2e1`

- 青色：薄荷青`#00FFFF`

- 粉色：樱花粉`#f8779e`

- 橙色：琥珀橙`#FF8000`

- 紫色：葡萄紫`#800080`

![](assets/color-display.png)

## 支持多种车型：

- 普通车：5门4窗
- 小型车：4门3窗
- 迷你车：2门1窗

## 兼容性：

兼容3.1.0以上的Mod版本与所有支持[Minecraft-Transit-Railway](https://github.com/Minecraft-Transit-Railway/Minecraft-Transit-Railway) 3.1.0以上Minecraft版本

原版支持1.16.5，如果你使用的为其他版本可修改pack.mcmeta文件解决

## 如何安装

### 下载最新Releases

1. 下载最新Releases中与资源包相同名称的的zip文件

2. 复制到Minecraft的`resourcepacks`目录中，请确保Minecraft-Transit-Railway已正常运作

3. 在游戏中启用此资源包

### 本地打包

1. Git Clone本仓库

2. 将`resource_pack`​文件夹的以下内容打包为ZIP文件并复制到Minecraft的`resourcepacks`目录中：
   
   ```language
   resource_pack/
   ├── pack.mcmeta
   ├── pack.png
   └── assets/
      └── mtr/
          ├── mtr_custom_resources.json
          └── custom_directory/...    
   ```

3. 在游戏中启用此资源包

4. 确保已安装MTR模组

### 版本修改

进入资源包文件夹下的pack.mcmeta，你将看到如下内容

```mcmeta
{
    "pack": {
        "pack_format": 6,
        "description": "C-train多彩列车包\n作者：阿晨君"
    }
}
```

将`"pack_format"`​的值更改为你使用的版本号：内容来自[Minecraft WiKi](https://zh.minecraft.wiki/w/%E8%B5%84%E6%BA%90%E5%8C%85#pack.mcmeta)

| 版本               | 数字    |
| ---------------- | ----- |
| 1.6.1 - 1.8.9    | 1     |
| 1.9 - 1.10.2     | 2     |
| 1.11 - 1.12.2    | 3     |
| 1.13 - 1.14.4    | 4     |
| 1.15 - 1.16.1    | 5     |
| 1.16.2 - 1.16.5  | 6     |
| 1.17 - 1.17.1    | 7     |
| 1.18 - 1.18.2    | 8     |
| 1.19 - 1.19.2    | 9     |
| 1.19.3           | 11-12 |
| 1.19.4           | 13    |
| 1.20 - 1.20.1    | 15    |
| 1.20.2           | 16-18 |
| 1.20.3 - 1.20.4  | 22    |
| 1.20.5 - 1.20.6  | 32    |
| 1.21 - 1.21.4    | 47    |
| 1.21.5           | 55    |
| 1.21.6 - 1.21.8  | 64    |
| 1.21.9 - 1.21.10 | 69.0  |
| 1.21.11          | 75.0  |

## 许可证

本项目采用MIT许可证。详见[LICENSE](LICENSE)文件。
