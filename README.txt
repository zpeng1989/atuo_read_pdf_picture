脚本解决问题：
(1) 图片上字体识别的分析
(2) 转换为txt文本文件

1. 先说下硬件要求:
例子1: i3+4g内存, 无显卡. 正常运行


2. 需要下载的东西:
(1)python2.7 网址：https://www.python.org/downloads/release/python-2715/
到"Windows x86-64 MSI installer"下直接点击就行, 下载完后直接下一步到安装完就行了;


3. 搭建:
(1) 复制文件夹 Automatic_Identification 到桌面（或者其他目录下，建议C盘）
(2) 开始菜单-->Windows系统-->命令指令符
出现黑窗口然后, 输入以下命令 
cd C:\Users\zhangp\Desktop\Automatic_Identification\workflow（这里需要注意切换到你自己的这个目录下）
输入一行, 回车, 安装完后继续输入下一行, 回车:
pip install urllib2
pip install urllib
pip install tkinter
(3) 全部安装完后，退出；


4. 把玩:
(1) 在cmd(黑色界面)里输入'cd path', 其中path是文件的路径，就是workflow中dai.py文件目录。
(2) 运行dai.py
(3) 弹出交互界面，点击File open 控制键，就会进入选择文件的路径
(4)	再点击hit me 就可以运行，输出问的文本文件和图片存在同一个目录下，文件名一直，之后后缀为txt。


5.注意：
(1) 测试版，很多问题需要修改，所以输出的结果需要麻烦各位手动检查一下；
