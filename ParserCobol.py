import sys
sys.path.append('/Users/nancy/Downloads')  # 将gen目录添加到环境变量中
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, ParseTreeListener
from CobolLexer import CobolLexer
from CobolParser import CobolParser
import networkx as nx
import matplotlib.pyplot as plt

class TreeListener(ParseTreeListener):
    def __init__(self):
        self.G = nx.DiGraph()
        self.parent = None

    def enterEveryRule(self, ctx):
        if self.parent is not None:
            self.G.add_edge(self.parent, ctx)
        self.parent = ctx

    def exitEveryRule(self, ctx):
        self.parent = None if ctx.parentCtx is None else ctx.parentCtx

def tree_to_graph(tree):
    listener = TreeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.G

def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

# 读取COBOL源代码文件
input_stream = FileStream('/Users/nancy/Downloads/CBL0002.cbl')

# 使用ANTLR生成的解析器解析COBOL源代码
lexer = CobolLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CobolParser(token_stream)

# 生成语法树
tree = parser.startRule()  # 替换为你的语法文件中定义的开始规则

# 打印语法树
print(tree.toStringTree(recog=parser))

G = tree_to_graph(tree)
draw_graph(G)