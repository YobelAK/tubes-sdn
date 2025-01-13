from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import time


def customTopo():
    
    net = Mininet(link=TCLink, switch=OVSSwitch, controller=RemoteController, autoSetMacs=True)

    info(' Adding remote controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',  
                           port=6633)  
    info(' Adding switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')
    s8 = net.addSwitch('s8')
    s9 = net.addSwitch('s9')
    s10 = net.addSwitch('s10')
    
    info(' Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    h4 = net.addHost('h4', ip='10.0.0.4/24')
    h5 = net.addHost('h5', ip='10.0.0.5/24')
    h6 = net.addHost('h6', ip='10.0.0.6/24')
    h7 = net.addHost('h7', ip='10.0.0.7/24')

    info(' Creating links\n')

    net.addLink(s1, s2)
    net.addLink(s1, s4) 
    net.addLink(s1, h1)

    net.addLink(s2, s3)
    net.addLink(s2, s10)

    net.addLink(s3, s6)
    net.addLink(s3, h4)

    net.addLink(s4, s5)
    net.addLink(s4, s7)

    net.addLink(s5, s10)

    net.addLink(s6, s8)
    net.addLink(s6, s9)
    net.addLink(s6, h7)

    net.addLink(s7, h2)
    net.addLink(s7, s8)
    net.addLink(s7, s8)

    net.addLink(s8, h6)
    net.addLink(s8, s10)
    net.addLink(s8, s9)

    net.addLink(s9, h3)

    net.addLink(s10, h5)

    info(' Starting network\n')
    net.build()

    info(' Starting controller\n')
    c0.start()

    info(' Starting switches\n')
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])
    s5.start([c0])
    s6.start([c0])
    s7.start([c0])
    s8.start([c0])
    s9.start([c0])
    s10.start([c0])

    info(' Pausing for 5 seconds to allow STP to converge\n')
    time.sleep(5) 
    info(' Running CLI\n')
    CLI(net)

    info('* Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    customTopo()


./pox.py openflow.of_01 --port=6633 log.level --DEBUG samples.pretty_log openflow.discovery openflow.spanning_tree --no-flood --hold-down forwarding.l2_learning host_tracker info.packet_dump
