import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的有向图
G = nx.DiGraph()

# 添加节点
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")

# 添加边
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("B", "E")
G.add_edge("C", "F")

# 打印图的节点和边
# 打印图的节点和边
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

# 使用spring布局来绘制图形
pos = nx.spring_layout(G)
#pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
# 绘制图形
nx.draw(G, pos, with_labels=True)

# 显示图形
plt.show()