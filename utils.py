def lines(file):
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):  # 循环迭代器，取得文档的每一个块
        if line.strip():  # 如果这一行不为空，加入到这个block
            block.append(line)
        elif block:  # 否则就返回这个block ，返回以后重置block
            yield ''.join(block).strip()
            block = []
