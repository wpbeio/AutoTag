# coding=utf-8

import re


def lines(file):
    for line in file:  # 遍历文档的每一个字符
        yield line
        # print(line)

    yield '\n'  # 遍历完整个文档以后返回一个换行


def blocks(file):
    block = []
    for line in lines(file):  # 循环迭代器，取得文档的每一个块
        if line.strip():  # 如果个字符不为空，加入到这个block，为空就是一个单词结束
            block.append(line)
        elif block:  # 否则就返回这个block ，返回以后重置block
            yield ''.join(block).strip()
            # print(block)
            # print('\n')
            block = []


def addFilter(self, patten, name):
    def filter(block, handler):
        return re.sub(patten, handler.sub(name), block)
    self.filters.append(filter)

if __name__ == '__main__':
    with open('testtxt.txt', 'r') as f:
        for x in blocks(f.read()):
            pass
