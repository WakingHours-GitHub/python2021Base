"""
目标:
    列表的应用场景
    列表的格式
    列表的常用操作
    列表的循环遍历
    列表的嵌套应用

列表是一个容器, 用于存放多个数据.
列表是一个可变数据类型, 因此对于列表的操作是可以在原列表上进行操作的.

列表的格式:
    list(): [ele1, ele2, ...]
    列表中可以存放多个数据.
    列表中的数据类型可以不固定, 可以是多种数据类型
    但是在工作中, 一个列表尽可能存取相同的数据类型.

常用操作:
    查找:
        下标:
            在列表中, 下标(索引), 也是从0开始, 定位数据, 存取数据使用.
    查找相关的函数:
        index = list.index(想要查找的数据, 开始位置下标, 结束位置下标)
        返回数据索引, 如果查找的数据不存在则报错

        int = list.count(计数的数据, 开始下标, 结束下标)
        返回列表中, 想要计数的数据个数

        公共操作: 对于: 字符串, 列表, 元组, 集合, 字典, 都可以使用
        len(list): 返回列表, 元组中数据个数.
        in, not in 也是公共操作


    判断元素是否存在:
        关键字:
        in: 如果元素某个序列中, 则返回True, 否则返回False
        not in: 判断元素是否不在序列中, 不在返回True, 在则返回False

    增加:
        将数据添加到数据列表当中
        list.append(数据): 在列表结尾添加数据. 数据如果是一个序列, 则将该序列整体添加到列表当中去.
        list.extend(序列): 列表结尾追加数据, 数据可以是序列, 将该序列一一添加到列表中去. 常用于合并两个列表.
        list.insert(索引, 数据): 指定索引, 插入数据.

    删除:
        将列表中的数据删除
        del: 这是一个关键字
        可以删除列表, 也可以删除列表中某一索引的元素.
            语法:
            del 目标
            del(目标)

        删除的数据 = list.pop(索引): 删除指定索引的数据, 如果不指定下标, 默认删除最后一个数据
            并且返回被删除的数据

        list.remove(数据): 按照内容(数据)删除, 移除列表中某个数据的第一个匹配项

        list.clear(): 清空列表

    修改:
        修改指定索引数据, 直接使用索引, 然后修改即可
        list[index] = new_data

        逆置: reverse()
            list.reverse()
            直接改变原列表, 逆序排列.
        排序: sort() 排序: 升序, 降序
            list.sort(key=None, reverse=False)
            key是字典排序时使用的,

            reverse: 默认为False为升序, reverse为True则降序.


    复制:
        copy()
        new_list = list.copy()
        copy()函数, 使用的是深拷贝. 数据复制.
        new_list = list # 浅拷贝. 地址复制.
"""

name_list = ["tom", "lily", "rose"]
# 通过索引去查找.
print(name_list[0])  # tom

print('tom' in name_list)  # True
print('lipu' not in name_list)  # True.



# 使用append()添加数据
# 可见, 列表是可变数据类型
# append函数追加数据时, 数据是一个序列, 就将该数据作为一个整体添加到列表的结尾.
name_list.append("xiaoming")
print(name_list) # ['tom', 'lily', 'rose', 'xiaoming']

name_list.append(["xiaohong, xq"])
print(name_list) # ['tom', 'lily', 'rose', 'xiaoming', ['xiaohong, xq']]
# 可见, 数据当作一个整体列表, 添加到原列表当中.


# extend(): 列表结尾追加数据, 如果数据是一个序列, 则将该序列逐个添加到原列表中
name_list = ['tom', 'lily', 'rose']
name_list.extend("xiaohong")
print(name_list) # ['tom', 'lily', 'rose', 'x', 'i', 'a', 'o', 'h', 'o', 'n', 'g']
# 可见, extend是逐个追加的. 因此常常用于两个列表的合并.

name_list = ['tom', 'lily', 'rose']
name_list.extend(["xiaohong", "xiaoming"])
print(name_list) # ['tom', 'lily', 'rose', 'xiaohong', 'xiaoming']
# 可见, 数据序列是逐一添加到原列表当中.

# insert(): 指定 索引, 插入数据
name_list.insert(2, "aaa")
print(name_list) # ['tom', 'lily', 'aaa', 'rose', 'xiaohong', 'xiaoming']
# 可见, 在索引2的位置, 插入了数据.



# 删除相关的操作:




