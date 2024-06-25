#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet 
from mininet.node import CPULimitedHost 
from mininet.link import TCLink 
from mininet.util import dumpNodeConnections 
from mininet.log import setLogLevel 
from mininet.node import Controller,RemoteController  
from mininet.cli import CLI

import os

class MyTopo(Topo):
  print "\n*** Test Topology\n"
  print "         Host4"
  print "           |"
  print "           |"
  print "Host1---Switch0-----(25%)------Switch1"
  print "           |                      |"
  print "          (0%)                   (0%)"
  print "           |                      |"
  print "        Switch2------(0%)------Switch3---Host2"
  print "                                  |"
  print "                                  |"
  print "                                Host3\n"

  def __init__(self, n=2, **opts):
   Topo.__init__(self, **opts)
   s0 = self.addSwitch('s0')
   s1 = self.addSwitch('s1')
   s2 = self.addSwitch('s2')
   s3 = self.addSwitch('s3')
   h1=self.addHost('h1', cpu=.5/n)
   h2=self.addHost('h2', cpu=.5/n)
   h3=self.addHost('h3', cpu=.5/n)
   h4=self.addHost('h4', cpu=.5/n)
   self.addLink(h1, s0)
   self.addLink(s0, s1, loss=50)
   self.addLink(s0, s2)
   self.addLink(s1, s3)
   self.addLink(s2, s3)
   self.addLink(s3, h2)
   self.addLink(s3, h3)
   self.addLink(h4, s0)

def perfTest(): 
  "Create Network & Run Simple Performance Test"
  topo= MyTopo(n=4)
  net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink, controller=RemoteController)
  net.start()
  h1, h2, h3, h4 = net.get('h1', 'h2', 'h3', 'h4')
  print"\n"
  print "*******************************************************************************************************\n"
  raw_input( "Press Any Key To PINGALL Connections...\n")
  net.pingAll()
  print "*******************************************************************************************************"
  CLI(net)
  net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
