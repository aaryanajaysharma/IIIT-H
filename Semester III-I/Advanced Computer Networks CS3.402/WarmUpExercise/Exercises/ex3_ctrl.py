from pox.core import core 
import pox.openflow.libopenflow_01 as of 
from pox.lib.util import dpidToStr

""" PASTE UNDER /pox/ext/ """

log = core.getLogger() 
s0_dpid=0
s1_dpid=0 
s2_dpid=0 
s3_dpid=0

def _handle_ConnectionUp(event):
 global s0_dpid, s1_dpid, s2_dpid, s3_dpid
 print "ConnectionUp: ", dpidToStr(event.connection.dpid)

#remember the connection dpidfor switch
 for m in event.connection.features.ports:
  if m.name == "s0-eth1":
   s0_dpid = event.connection.dpid
   print "s0_dpid=", s0_dpid
  #To Do 1: Do it for the rest of the switches as well!!! SEE TOPOLOGY FILE FOR DETAILS OF THE SWITCHES.


def _handle_PacketIn (event):
 global s0_dpid, s1_dpid, s2_dpid, s3_dpid 
 print "PacketIn: ", dpidToStr(event.connection.dpid)

 if event.connection.dpid==s0_dpid:
   msg= of.ofp_flow_mod()
   msg.idle_timeout = 0
   msg.hard_timeout = 0 
   # To Do 2: FLOOD THE PACKETS. USE SYNTAX:
   # msg.actions.append(of.ofp_action_output(port = FLOOD_TO_ALL_CMD))
   event.connection.send(msg)

 #To Do 3: Repeat for the rest of the switches as well!!!


def launch():
 core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp) 
 core.openflow.addListenerByName("PacketIn", _handle_PacketIn) 
