from sys import exit


class Idiom:
    def __init__(self, identifier, parent):
        self.__identifier = identifier
        self.__children = []
        self.__parent = parent

    def get_name(self):
        return self.__identifier

    def get_children(self):
        return self.__children

    def get_parent(self):
        return self.__parent

    def add_child(self, idiom):
        self.__children.append(idiom)

    def traversal(self):
        print(self.get_name())
        if self.get_parent() is None:
            return
        else:
            self.get_parent().traversal()


class IdiomTree:
    def __init__(self):
        self.__head = Idiom("为所欲为", None)
        self.__all_idiom = [self.__head]

    def print_tree(self):
        print(self.__head.get_name())
        queue = self.__head.get_children()
        while queue:
            print(queue[0].get_name())
            queue = queue[1:] + queue[0].get_children()

    def span_idiom_tree(self, file):
        file = open(file, encoding="utf-8")
        line = file.readlines()
        queue = [self.__head]

        while queue:
            for item in line:
                if item[3] == queue[0].get_name()[0]:
                    temp = Idiom(item[:4], queue[0])
                    queue[0].add_child(temp)
                    self.__all_idiom.append(temp)
                    queue.append(temp)
                    line.remove(item)
            queue = queue[1:]

    def search(self, start, file):
        with open(file, 'r+', encoding="utf-8") as f:
            words = f.read()
            if start not in words:
                inpt = input("%s这个词似乎不在词库里，是否加入？(y/n)" % start)
                if inpt == 'y':
                    f.write("\n%s" % start)
                exit(0)

        for i in self.__all_idiom:
            if start == i.get_name():
                i.traversal()
                return True
        print("%s这个词似乎不能连到为所欲为" % start)
        return False

if __name__ == "__main__":
    a = IdiomTree()
    print("加载词库中...")
    filename = 'idiom_bank.txt'
    a.span_idiom_tree(filename)
    while True:
        inp = input("给我一个四字成语：")
        success = a.search(inp, filename)
#        if success:
#           print("为所欲为\n为所欲为 。。。。。。")
        ans = input("还想继续玩？(y/n)")
        if ans == "n":
            break
