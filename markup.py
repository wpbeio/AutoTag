# coding=utf-8
import sys
import re
from handlers import *
from utils import *
from rules import *
'''
'''


class Parser():
    """语法分析模块"""

    def __init__(self, handler):
        # super(Parser, self).__init__()
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, patten, name):
        def filter(block, handler):
            return re.sub(patten, handler.sub(name), block)
        self.filters.append(filter)

# 分析传入文件的方法
    def parse(self, file):
        self.handler.start('document')  # 传入文件第一步加入HTML文件的标头
        # 分割块
        for block in blocks(file):
            for filter in self.filters:  # 初始化BasicTextParser的时候就已经将所有的规则和正则加入
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    """docstring for BasicTextParser"""

    def __init__(self, handler):
        # 识点子类初始化函数，需要调用父类初始化，下面也可以使用super调用，super调用可以解决砖石继承的问题（多继承）
        # Parser.__init__(self, handler)
        super(BasicTextParser, self).__init__()
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasi')
        self.addFilter(r'(http://[\.a-z0-9A-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

# 实例化一个HTMLRenderer对象，HTMLRenderer继承于Handler
text = HTMLRenderer()

# 实例化一个BasicTextParser对象，BasicTextParser对象继承于Parser。Parser初始化需要提供Handler类参数，而HTMLRenderer继承于Handler，所以可以直接实例化。
parser = BasicTextParser(text)
# 使用parse方法分析传入的文件
parser.parse(sys.stdin)
