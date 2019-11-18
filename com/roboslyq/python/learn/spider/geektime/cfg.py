# encoding: utf-8
import optparse     # 强大的参数解析模块

# 命令行参数定义(提示用户)
descriptions = {
    # option name: [help msg, type, default value]
    'cell-phone': ['cell phone to login greek time', str, None],
    'password': ['password to login greek time', str, None],
    'save-dir': ['directory to save pdf', str, None],
    'download-interval': ['interval of every request', int, 0]
}
"""
　　1、首先import optparse类 ： import optparse 
    2、然后创建optparse对象parser ： optparse.OptionParser()
    3、再使用add_option()来定义命令行参数： parser.add_option(）
    4、最后使用parse_args()来解析命令行: parser.add_option()
    
    传参Demo： --cell-phone=1588993xxxx --password=xxxx --save-dir=D:\360Downloads
    
"""
# init options
parser = optparse.OptionParser()
for k, v in descriptions.items():
    default = v[2] if v[2] is not None else optparse.NO_DEFAULT
    parser.add_option('--{}'.format(k),
                      dest=k.replace('-', '_'),
                      default=default,
                      help=v[0],
                      type=v[1])
options, _ = parser.parse_args()