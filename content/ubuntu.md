Title: Ubuntu
Date: 2000-01-01 00:00
Category: Ubuntu

[TOC]

### 显卡驱动

```
sudo apt install --no-install-recommends \
nvidia-384 nvidia-prime
```

如果安装的是Ubuntu Gnome 16.04，需要额外安装 `gdm`

* * *

### Gnome软件

``` sh
sudo apt install --no-install-recommends \
ibus-libpinyin \
gnome-boxes \
gnome-builder flatpak-builder \
gnome-calculator \
gnome-calendar \
gnome-contacts \
gnome-dictionary \
gnome-documents \
gnome-games-app \
gnome-maps \
gnome-music \
gnome-photos \
gnome-todo \
gnome-weather \
polari \
totem \
corebird \
gnome-recipes \
gnome-twitch \
gnome-twitch-player-backend-gstreamer-cairo \
gnome-twitch-player-backend-gstreamer-clutter \
gnome-twitch-player-backend-gstreamer-opengl \
pitivi \
libclutter-1.0-dev \
libclutter-1.0-doc \
libclutter-gst-3.0-dev \
libclutter-gst-3.0-doc \
libclutter-gtk-1.0-dev \
libclutter-gtk-1.0-doc \
libgail-dev libgail-doc \
libgail-3-dev libgail-3-doc \
libgconf2-dev libgconf2-doc \
libgtk-3-dev libgtk-3-doc \
libgtk2.0-dev libgtk2.0-doc \
libgtkdatabox-dev libgtkdatabox-doc \
libgtkdataboxmm-dev libgtkdataboxmm-doc \
libgtkmm-2.4-dev libgtkmm-2.4-doc \
libgtkmm-3.0-dev libgtkmm-3.0-doc \
libgtksourceview-3.0-dev libgtksourceview-3.0-doc \
libwebkit2gtk-4.0-dev libwebkit2gtk-4.0-doc \
```

* * *

### KDE软件

``` sh
sudo apt install --no-install-recommends \
fcitx-googlepinyin \
kdenlive \
kdevelop kdevelop-l10n kdevelop-python kdevelop-python-l10n \
krita krita-l10n \
kwrite kate \
librecad \
qtcreator \
virtualbox virtualbox-guest-additions-iso virtualbox-ext-pack \
telegram-desktop \
kdevelop-dev \
kdevplatform-dev kdevplatform-l10n \
libqt5serialport5-dev \
qt3d5-dev qt3d5-doc qt3d5-doc-html qt3d5-examples \
qtbase5-dev qtbase5-doc qtbase5-doc-html qtbase5-examples \
qtconnectivity5-dev qtconnectivity5-doc qtconnectivity5-doc-html qtconnectivity5-examples \
qtdeclarative5-dev qtdeclarative5-doc qtdeclarative5-doc-html qtdeclarative5-examples \
qtlocation5-dev qtlocation5-doc qtlocation5-doc-html qtlocation5-examples \
qtmultimedia5-dev qtmultimedia5-doc qtmultimedia5-doc-html qtmultimedia5-examples \
qtscript5-dev qtscript5-doc qtscript5-doc-html qtscript5-examples \
qttools5-dev qttools5-doc qttools5-doc-html qttools5-examples \
```

* * *

### 其他软件

``` sh
sudo apt install --no-install-recommends \
ffmpeg ffmpeg-doc \
gstreamer1.0-plugins-bad gstreamer1.0-plugins-bad-doc \
gstreamer1.0-plugins-ugly gstreamer1.0-plugins-ugly-doc \
gstreamer1.0-fluendo-mp3 gstreamer1.0-libav \
vim vim-doc vim-scripts vim-addon-manager exuberant-ctags \
git git-doc repo mercurial subversion \
p7zip-full p7zip-rar zip unzip rar unrar unrar-free unar \
adb fastboot \
minicom picocom openocd \
mtd-utils u-boot-tools \
polipo proxychains squid stunnel4 \
pandoc \
fping hping3 netcat nmap \
samba smbclient samba-dsdb-modules samba-vfs-modules \
vsftpd sqlite3 sqlite3-doc \
qemu qemu-user-static \
build-essential cppcheck glibc-doc gcc-doc libstdc++-6-doc make-doc \
gcc-multilib g++-multilib gcc-arm-none-eabi gdb-arm-none-eabi \
gdb gdb-doc \
texinfo texinfo-doc-nonfree \
autoconf autoconf-doc automake autopoint libtool libtool-doc \
cmake cmake-doc pkg-config \
llvm clang clang-format llvm-4.0-doc clang-4.0-doc \
golang \
openjdk-8-jdk openjdk-8-doc openjdk-8-source openjdk-8-demo \
libappindicator-dev libappindicator-doc \
libatk1.0-dev libatk1.0-doc \
libatkmm-1.6-dev libatkmm-1.6-doc \
libbz2-dev bzip2-doc \
libcairo2-dev libcairo2-doc \
libcairomm-1.0-dev libcairomm-1.0-doc \
libcanberra-dev libcanberra-doc \
libcogl-dev libcogl-doc \
libdee-dev libdee-doc \
libdevil-dev \
libflac-dev libflac-doc \
libgda-5.0-dev libgda-5.0-doc \
libgdamm5.0-dev libgdamm5.0-doc \
libgdk-pixbuf2.0-dev libgdk-pixbuf2.0-doc \
libglib2.0-dev libglib2.0-doc \
libgstreamermm-1.0-dev libgstreamermm-1.0-doc \
libice-dev libice-doc \
libjson-glib-dev libjson-glib-doc \
libltdl-dev libtool-doc \
liblzma-dev liblzma-doc \
libncurses5-dev ncurses-doc \
libnotify-dev libnotify-doc \
libpango1.0-dev libpango1.0-doc \
libsdl-mixer1.2-dev \
libsdl2-dev libsdl2-doc \
libsigc++-2.0-dev libsigc++-2.0-doc \
libsm-dev libsm-doc \
libsoup2.4-dev libsoup2.4-doc \
libssl-dev libssl-doc \
libtelepathy-farstream-dev libtelepathy-farstream-doc \
libtelepathy-glib-dev libtelepathy-glib-doc \
libtelepathy-logger-dev libtelepathy-logger-doc \
libtheora-dev libtheora-doc \
libvdpau-dev libvdpau-doc \
libx11-dev libx11-doc \
libxml++2.6-dev libxml++2.6-doc \
libxml2-dev libxml2-doc \
llvm-dev \
python-dev python-doc \
python3-dev python3-doc \
```

* * *

### 32bit库

``` sh
# Android Studio
sudo apt install --no-install-recommends \
lib32ncurses5 lib32stdc++6 lib32z1
```

* * *

### 安装Shadowsocks

> 翻墙

``` sh
sudo apt install --no-install-recommends \
shadowsocks
# or
pip install --user \
shadowsocks M2Crypto
```

#### 客户端
- 修改服务文件`/etc/init.d/shadowsocks`，将变量`DAEMON`更改为`/usr/bin/sslocal`
- 修改配置文件`/etc/shadowsocks/config.json`

#### 服务端
- 修改配置文件`/etc/shadowsocks/config.json`，将字段`server`修改为`0.0.0.0`

* * *

### polipo设置

> 默认端口 8123

修改文件 `/etc/polipo/config`，增加以下配置

``` txt
proxyAddress = "0.0.0.0"
allowedClients = 127.0.0.1, 192.168.0.0/16
socksParentProxy = "localhost:1080"
socksProxyType = socks5
```

* * *

### proxychains设置

修改文件 `/etc/proxychains.conf`，删除原来的 `socks4` 配置，增加新的配置 `socks5 IP PORT`

* * *

### 安装Pelican

> 静态博客

``` sh
sudo apt install --no-install-recommends \
pelican python-bs4 python-typogrify ghp-import
# or
pip install --user \
pelican Markdown beautifulsoup4 typogrify ghp-import

```

- `ghp-import`的参数`-c CNAME`可自动生成`CNAME`文件

* * *

### 系统配置

#### 主题和字体

- 主题安装目录 `/usr/share/themes` 及 `~/.local/share/themes/`
- 图标安装目录 `/usr/share/icons` 及 `~/.local/share/icons/`
- 壁纸安装目录 `/usr/share/backgrounds` 及 `~/.local/share/backgrounds/`
- 字体安装目录 `/usr/share/fonts` 及 `~/.local/share/fonts/`

下载

``` sh
# Vimix-Gtk-Theme
wget https://dl.opendesktop.org/api/files/downloadfile/id/1513512805/s/3d9d7459c7395278cd8974ab62347951/t/1513669455/Vimix-Dark-Theme.tar.xz
wget https://dl.opendesktop.org/api/files/downloadfile/id/1513512788/s/3d9d7459c7395278cd8974ab62347951/t/1513669455/Vimix-Light-Theme.tar.xz
# Vimix-Icon-Theme
wget https://github.com/vinceliuice/vimix-icon-theme/archive/2017.09.24.tar.gz
# Wallpapers
wget https://dl.opendesktop.org/api/files/downloadfile/id/1506049886/s/f81518fae8c0fbc9ababee59e1893113/t/1513672104/lakeu.zip
```

设置
``` sh
gsettings get org.gnome.desktop.interface gtk-theme
gsettings set org.gnome.desktop.interface gtk-theme 'THEME'

gsettings get org.gnome.desktop.wm.preferences theme
gsettings set org.gnome.desktop.wm.preferences theme  'THEME'

gsettings get org.gnome.desktop.interface icon-theme
gsettings set org.gnome.desktop.interface icon-theme 'THEME'

gsettings get org.gnome.shell.extensions.user-theme name
gsettings set org.gnome.shell.extensions.user-theme name 'THEME'

gsettings get org.gnome.desktop.interface cursor-theme
gsettings set org.gnome.desktop.interface cursor-theme 'THEME'

gsettings get org.gnome.desktop.background picture-uri
gsettings set org.gnome.desktop.background picture-uri 'file://PATH'

gsettings get org.gnome.desktop.interface font-name
gsettings set org.gnome.desktop.interface font-name 'FONT' # 'Ubuntu 11'

gsettings get org.gnome.desktop.interface document-font-name
gsettings set org.gnome.desktop.interface document-font-name 'FONT' # 'Sans 11'

gsettings get org.gnome.desktop.interface monospace-font-name
gsettings set org.gnome.desktop.interface monospace-font-name 'FONT' # 'Ubuntu Mono 13'

gsettings get org.gnome.desktop.wm.preferences titlebar-uses-system-font
gsettings set org.gnome.desktop.wm.preferences titlebar-uses-system-font false

gsettings get org.gnome.desktop.wm.preferences titlebar-font
gsettings set org.gnome.desktop.wm.preferences titlebar-font 'FONT' # 'Ubuntu Bold 11'
```

> 修改 Gnome Shell 的主题还需要执行 `gnome-shell-extension-prefs`，启用其中的 `User Themes`

#### 登录界面背景

[Change Login Screen Background](http://ubuntuhandbook.org/index.php/2017/10/change-login-screen-background-ubuntu-17-10/)

#### 输入法

``` sh
gsettings get org.gnome.desktop.input-sources sources
# [('ibus', 'libpinyin')]
```

#### 代理

``` sh
gsettings list-recursively org.gnome.system.proxy

gsettings get org.gnome.system.proxy use-same-proxy
gsettings set org.gnome.system.proxy use-same-proxy true

gsettings get org.gnome.system.proxy autoconfig-url
gsettings set org.gnome.system.proxy autoconfig-url 'PATH'

gsettings get org.gnome.system.proxy.socks host
gsettings set org.gnome.system.proxy.socks host 'IP'

gsettings get org.gnome.system.proxy.socks port
gsettings set org.gnome.system.proxy.socks port PORT
```

#### 其他

``` sh
gsettings get org.gnome.desktop.default-applications.terminal exec
gsettings get org.gnome.desktop.default-applications.terminal exec-arg

gsettings get org.gnome.desktop.background picture-options
gsettings get org.gnome.desktop.background color-shading-type
gsettings get org.gnome.desktop.background primary-color
gsettings get org.gnome.desktop.background secondary-color
gsettings get org.gnome.desktop.background show-desktop-icons

gsettings get org.gnome.desktop.interface buttons-have-icons
gsettings get org.gnome.desktop.interface menus-have-icons
gsettings get org.gnome.desktop.interface clock-show-date
gsettings get org.gnome.desktop.interface clock-show-seconds
gsettings get org.gnome.desktop.interface menubar-accel

gsettings get org.gnome.desktop.screensaver lock-enabled

gsettings get org.gnome.desktop.session idle-delay

gsettings get org.gnome.desktop.wm.keybindings panel-main-menu
gsettings get org.gnome.desktop.wm.keybindings close
gsettings get org.gnome.desktop.wm.keybindings panel-run-dialog
gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-1
gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-2
gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-3
gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-4
gsettings get org.gnome.desktop.wm.keybindings show-desktop

gsettings get org.gnome.desktop.wm.preferences num-workspaces
gsettings get org.gnome.desktop.wm.preferences visual-bell
gsettings get org.gnome.desktop.wm.preferences visual-bell-type

gsettings get org.gnome.nautilus.desktop home-icon-visible
gsettings get org.gnome.nautilus.desktop network-icon-visible
gsettings get org.gnome.nautilus.desktop trash-icon-visible
gsettings get org.gnome.nautilus.preferences always-use-location-entry
gsettings get org.gnome.nautilus.preferences default-folder-viewer
gsettings get org.gnome.nautilus.preferences show-image-thumbnails
gsettings get org.gnome.nautilus.preferences show-directory-item-counts

gsettings get org.gnome.settings-daemon.plugins.power button-power
```

* * *

### git设置

``` sh
git config --global user.name "Yaty Lee"
git config --global user.email "studi7o@mail.ru"
git config --global core.editor "vim"
git config --global color.ui auto
git config --global http.sslVerify false
git config --global http.postBuffer 524288000
git config --global http.proxy "socks5://IP:PORT"
```

* * *

### Android开发设置

``` sh
sudo wget https://github.com/M0Rf30/android-udev-rules/raw/master/51-android.rules \
-P /etc/udev/rules.d
```

* * *

### python设置

更换国内源

``` sh
mkdir -p $HOME/.config/pip/ $HOME/.pip/

cat << 'EOF' | tee $HOME/.config/pip/pip.conf $HOME/.pip/pip.conf > /dev/null
[global]
index-url = https://pypi.doubanio.com/simple
EOF
```

安装pip

``` sh
sudo apt install python-pip
# or
easy_install --user pip
# or
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
```

* * *

### wget参数

- `--tries=1`：修改下载次数为1，默认是20次
- `-e http_proxy=http://ip:port -e https_proxy=http://ip:port -e ftp_proxy=http://ip:port`：设置代理

* * *

### Box客户端

在 Nautilus 中连接 `davs://dav.box.com/`

* * *

### 编写代理文件

``` txt
var PROXY = "SOCKS5 127.0.0.1:1080; DIRECT";

var blocked = {
    "www.google.com": 1
};

var slowly = {
    "downloads.gradle.org": 1
};

function FindProxyForURL(url, host)
{
    if (Object.hasOwnProperty.call(blocked, host)) {
        return PROXY;
    }
    if (Object.hasOwnProperty.call(slowly, host)) {
        return PROXY;
    }
    return "DIRECT"
}
```

* * *

### 应用图标

> 图标路径 `~/.local/share/applications/`

#### Android Studio (android-studio.desktop)

``` txt
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio
Icon=android-studio
Exec=/opt/android-studio/bin/studio.sh %f
Comment=IDE for Android Development
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-android-studio
```

#### Atom (atom.desktop)

``` txt
[Desktop Entry]
Name=Atom
Comment=A hackable text editor for the 21st Century.
GenericName=Text Editor
Exec=/opt/atom/atom %F
Icon=atom
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Utility;TextEditor;Development;
MimeType=text/plain;
```
