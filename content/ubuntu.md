Title: Ubuntu
Date: 2000-01-01 00:00
Category: Ubuntu

[TOC]

### 安装Shadowsocks

> 翻墙

``` sh
sudo apt install --no-install-recommends \
shadowsocks
```

#### 客户端
- 修改服务文件`/etc/init.d/shadowsocks`，将变量`DAEMON`更改为`/usr/bin/sslocal`
- 修改配置文件`/etc/shadowsocks/config.json`

#### 服务端
- 修改配置文件`/etc/shadowsocks/config.json`，将字段`server`修改为`0.0.0.0`

* * *

### 安装Pelican

> 静态博客

``` sh
sudo apt install --no-install-recommends \
pelican python-bs4 ghp-import
```

- `ghp-import`的参数`-c CNAME`可自动生成`CNAME`文件
