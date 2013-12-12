def ipCheck( netSplit, ipBase ):
    for controller, netList in netSplit.items():
        for network in netList:
            if not networkCheck( network, ipBase ):
                return False
    return True

def networkCheck( ipaddr1, ipaddr2 ):
    network1, broadcast1 = broadcastEvaluate( ipaddr1 )
    network2, broadcast2 = broadcastEvaluate( ipaddr2 )
    return compare(network1, network2, broadcast1, broadcast2)

def broadcastEvaluate( ipAddress ):
    bits = 8
    index = 3
    try:
        network, subnet = ipAddress.split( '/' )
    except ValueError:
        print "Could not split the network number"
        return False
    subnet = 32 - int( subnet )
    net = network.split( '.' )

    while subnet >= 0:
        if subnet < bits:
            subnet = subnet % bits
            mask = pow( 2, subnet ) - 1 
        else:
            mask = pow( 2, bits ) - 1
        net[ index ] = str( int( net[ index ] ) | mask )
        subnet = subnet - bits
        index = index - 1
    return network, '.'.join ( net )

def compare(net1, net2, broad1, broad2):
    if net1 > broad2 or net2 > broad1:
        return False
    else:
        return True
