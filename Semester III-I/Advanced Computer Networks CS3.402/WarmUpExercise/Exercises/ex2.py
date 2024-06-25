#!/usr/bin/python
 
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import TCLink
from mininet.log import  setLogLevel, info
 
def mynetwork():

    info( "\n*** Test Topology\n\n")
    info ("Host0---Switch0---Switch1---Host1\n")
    switch0 = Node( 's0', inNamespace=False )
    switch1 = Node( 's1', inNamespace=False )
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )
    
    info( "\n*** Configuring Nodes & Creating Links\n\n" )
    linkopts0=dict(bw=10)
    linkopts1=dict(bw=10, delay='5ms', loss=10)
    TCLink( h0, switch0, **linkopts0)
    TCLink( h1, switch1,**linkopts0)
    TCLink( switch0, switch1,**linkopts1) 
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )

    info( "\n\n*** Open vSwitch Port Info\n\n" )
    switch0.cmd( 'ovs-vsctl add-br dp0' )
    switch1.cmd( 'ovs-vsctl add-br dp1' )
 
    for intf in switch0.intfs.values():
        print intf
        print switch0.cmd( 'ovs-vsctl add-port dp0 %s' % intf )
 
    for intf in switch1.intfs.values():
        print intf
        print switch1.cmd( 'ovs-vsctl add-port dp1 %s' % intf )

    # To Do 1:
    # add-flow for switch 1 & 2 for both to & fro
    # Use syntax :
    # switch_name.cmd('ovs-ofctl add-flow datapath_id \"in_port=port_X actions=output:port_Y\"' )


    info( "*** Running test\n\n" )
    h0.cmdPrint( 'ping -c10 ' + h1.IP() )
    h1.cmdPrint( 'ping -c10 ' + h0.IP() )  
 
    info( "\n*** Stopping network " )
    switch0.cmd( 'ovs-vsctl del-br dp0' )
    switch0.deleteIntfs()
    switch1.cmd( 'ovs-vsctl del-br dp1' )
    switch1.deleteIntfs()
    info( '\n' )
 
if __name__ == '__main__':
    setLogLevel( 'info' ) 
    Mininet.init()
    mynetwork()
