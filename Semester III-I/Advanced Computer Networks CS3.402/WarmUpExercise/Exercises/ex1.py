#!/usr/bin/python

"""
To run this script copy it to home folder -> open terminal -> write "sudo python ex1.py" -> enter your password of your machine.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
 
class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
            #Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h + 1), cpu=.5/n)
            #10 Mbps, 5ms delay, 0% Loss, 1000 packet queue
            self.addLink(host, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000, use_htb=True)
 
def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo=topo,host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    # To Do 1: Dump hosts connections here
    print "Testing network connectivity"
    # To Do 2: Ping all hosts via single command
    print "Testing bandwidth between h1 and h3"
    # To Do 3: Test bandwidth between host 1 & host 3 
    # HINT: First get the names of hosts from network then iperf them.
    net.stop()
 
if __name__=='__main__':
    setLogLevel('info')
    perfTest()
