from mininet.topo import Topo
class customtopology(Topo):
    "Simple topology example."
    def __init__(self):
        "Create custom topo."
        # Initialize topology
        Topo.__init__(self)

        core = self.addSwitch('c1')
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        #aggregation
        leftAggeration = self.addSwitch('a1')
        rightAggregation = self.addSwitch('a2')
        #edge
        leftEdge1 = self.addSwitch('e1')
        leftEdge2 = self.addSwitch('e2')
        rightEdge3 = self.addSwitch('e3')
        rightEdge4 = self.addSwitch('e4')

        # Add links
        self.addLink(core, leftAggeration)
        self.addLink(core, rightAggregation)
        self.addLink(leftAggeration, leftEdge1 )
        self.addLink(leftAggeration, leftEdge2)
        self.addLink(rightAggregation, rightEdge3)
        self.addLink(rightAggregation, rightEdge4)
        self.addLink(leftEdge1, h1)
        self.addLink(leftEdge1, h2)
        self.addLink(leftEdge2, h3)
        self.addLink(leftEdge2, h4)
        self.addLink(rightEdge3, h5)
        self.addLink(rightEdge3, h6)
        self.addLink(rightEdge4, h7)
        self.addLink(rightEdge4, h8)

topos = {'customtopology': (lambda: customtopology())}