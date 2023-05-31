import turtle

class BTNode:
    data=0
    left=None
    right=None

    def __init__(self, data=0, left=None, right=None):
        """
        初始化二叉树节点
        :param data: 节点数据
        :param left: 左子节点
        :param right: 右子节点
        """
        self.data = data
        self.left = left
        self.right = right

class BTree:
    node=None

    def __init__(self, data):
        """
        初始化二叉树
        :param data: 二叉树节点数据列表
        """
        for i in data:
            self.insert(self.node, i)

    def insert(self, node, val):
        """
        向二叉树中插入节点
        :param node: 当前节点
        :param val: 插入节点的数据
        """
        if not node:
            self.node = BTNode(val)
            return
        p = node
        while True:
            if p.data > val and p.left:
                p = p.left
            elif p.data > val and not p.left:
                q = BTNode(val)
                p.left = q
                return
            elif p.data < val and p.right:
                p = p.right
            elif p.data < val and not p.right:
                q = BTNode(val)
                p.right = q
                return

    def depth(self, node):
        """
        计算二叉树的深度
        :param node: 当前节点
        :return: 二叉树的深度
        """
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        else:
            leftDep = self.depth(node.left)
            rightDep = self.depth(node.right)
            if leftDep > rightDep:
                return leftDep + 1
            else:
                return rightDep + 1

    def draw(self):
        """
        绘制二叉树
        """
        width = turtle.window_width()
        height = turtle.window_height()
        yFar = height / (self.depth(self.node) + 1)
        xFar = width / 4
        x = width / 2
        y = yFar
        t = turtle.Turtle()
        turtle.tracer(0)
        turtle.setworldcoordinates(0, height, width, 0)
        self.drawTree(self.node, x, y, xFar, yFar, t)
        turtle.hideturtle()
        turtle.done()

    def drawTree(self, node, x, y, xFar, yFar, t):
        """
        递归绘制二叉树
        :param node: 当前节点
        :param x: 当前节点的x坐标
        :param y: 当前节点的y坐标
        :param xFar: x方向的距离
        :param yFar: y方向的距离
        :param t: turtle对象
        """
        if node.left:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.goto(x - xFar, y + yFar)
            self.drawTree(node.left, x - xFar, y + yFar, xFar / 2, yFar, t)
        if node.right:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.goto(x + xFar, y + yFar)
            self.drawTree(node.right, x + xFar, y + yFar, xFar / 2, yFar, t)
        if node:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.circle(15)
            t.penup()
            t.goto(x, y + 25)
            t.write(node.data, align="center")

def main():
    with open("./data.txt") as myFile:
        data = myFile.readlines()
        data = list(map(int, data[0].split()))
        myTree = BTree(data)
        myTree.draw()

if __name__ == '__main__':
    main()
