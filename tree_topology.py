from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel

class tree_topology(Topo):
    def build(self, n=2, levels=2):
        self.hostNum = 1
        self.addTree(self, levels, n)

    def addTree(self, parent, depth, fanout):
        if depth > 0:
            switch = self.addSwitch('s%s' % self.hostNum)
            for _ in range(fanout):
                host = self.addHost('h%s' % self.hostNum)
                self.hostNum += 1
                self.addLink(switch, host)
                self.addTree(switch, depth - 1, fanout)

def create_custom_tree(n, levels):
    topo = tree_topology(n=n, levels=levels)
    net = Mininet(topo)
    net.start()
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    n = int(input("Nhập số mức của cây: "))
    levels = int(input("Nhập số nút con trên mỗi mức: "))
    create_custom_tree(n, levels)
