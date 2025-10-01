# KoolCenter 插件 - OpenList文件列表 (123解限版)
[![license](https://img.shields.io/github/license/Genius-Society/rogsoft_openlist.svg)](./LICENSE)
[![sf](https://img.shields.io/badge/release-SourceForge-ff6600.svg)](https://sourceforge.net/projects/rogsoft-openlist/files)
[![bili](https://img.shields.io/badge/bilibili-BV18ergYRERP-fc8bab.svg)](https://www.bilibili.com/video/BV18ergYRERP/?p=2)

一个支持多种存储, 支持网页浏览和 WebDAV 的文件列表程序, 由 gin 和 Solidjs 驱动, 当前项目为其解限 pan123 下载 1G 流量限制的 KoolCenter 插件版本

<a href="https://github.com/Genius-Society/rogsoft_openlist" target="_blank">
    <img src="./openlist/res/icon-openlist.png" style="width: 160px;">
</a>

## 官方信息
插件正常启动后的使用问题请查看 [文档](https://www.oplist.org) 或去 [官方TG交流群](https://t.me/OpenListTeam) 寻求帮助

## 依赖项
在 KoolCenter 软件中心安装并挂载如下前置插件, 安装顺序自上而下:
- USB2JFFS
- 虚拟内存

## 机型支持
在 asuswrt 为基础的固件上, OpenList 插件目前仅支持 aarch64 架构的路由器, 具体如下：
- 部分及其未列出, 请根据 CPU 型号和支持软件中心与否自行判断
- 使用 OpenList 建议配置 1G 及以上的虚拟内存, 特别是小内存的路由器

| 机型             | 内存  | CPU/SOC | 架构  | 核心 | 频率    |
| ---------------- | ----- | ------- | ----- | ---- | ------- |
| RT-AC86U         | 512MB | BCM4906 | armv8 | 2    | 1.8 GHz |
| GT-AC2900        | 512MB | BCM4906 | armv8 | 2    | 1.8 GHz |
| RT-AX92U         | 512MB | BCM4906 | armv8 | 2    | 1.8 GHz |
| GT-AC5300        | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| RT-AX88U         | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| GT-AX11000       | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| NetGear RAX80    | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| RT-AX68U         | 512MB | BCM4906 | armv8 | 2    | 1.8 GHz |
| RT-AX86U         | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| GT-AXE11000      | 1GB   | BCM4908 | armv8 | 4    | 1.8 GHz |
| ZenWiFi_Pro_XT12 | 1GB   | BCM4912 | armv8 | 4    | 2.0GHz  |
| GT-AX6000        | 1GB   | BCM4912 | armv8 | 4    | 2.0GHz  |
| GT-AX11000_PRO   | 1GB   | BCM4912 | armv8 | 4    | 2.0GHz  |
| RT-AX86U_PRO     | 1GB   | BCM4912 | armv8 | 4    | 2.0GHz  |
| RAX50            | 512MB | BCM6750 | armv7 | 3    | 1.5 GHz |
| RAX70            | 512MB | BCM6755 | armv7 | 4    | 1.5 GHz |
| RT-AX56U         | 512MB | BCM6755 | armv7 | 4    | 1.5 GHz |
| RT-AX56U_V2      | 256MB | BCM6755 | armv7 | 4    | 1.5 GHz |
| RT-AX58U         | 512MB | BCM6750 | armv7 | 3    | 1.5 GHz |
| RT-AX82U         | 512MB | BCM6750 | armv7 | 3    | 1.5 GHz |
| TUF-AX3000       | 512MB | BCM6750 | armv7 | 3    | 1.5 GHz |
| TUF-AX5400       | 512MB | BCM6750 | armv7 | 3    | 1.5 GHz |
| ZenWiFi_XT8      | 512MB | BCM6755 | armv7 | 4    | 1.5 GHz |
| ZenWiFi_XD4      | 256MB | BCM6755 | armv7 | 4    | 1.5 GHz |
| TUF-AX3000_V2    | 512MB | BCM6756 | armv7 | 4    | 1.7GHz  |
| RT-AX57          | 256MB | BCM6756 | armv7 | 4    | 1.7GHz  |

## 代码下载
```bash
git clone git@github.com:Genius-Society/rogsoft_openlist.git
cd rogsoft_openlist
```

## 环境
```bash
conda create -n py311 python=3.11 -y
conda activate py311
```

## Windows 上打包
```bash
# 要先将 git bash 和 7z 的环境变量配置好重启
python build.py
```

## 致谢
- <https://github.com/Yxiguan/OpenList_123>
- <https://github.com/everstu/Koolcenter_openlist>
