def ipCheck( netSplit, ipBase ):
    if netSplit == False:
        return None
    for controller, netList in netSplit.items():
        for network in netList:
            if not networkCheck( network, ipBase ):
                return False
    return True

def networkCheck( ipaddr1, ipaddr2 ):
    network1, broadcast1 = broadcastEvaluate( ipaddr1 )
    network2, broadcast2 = broadcastEvaluate( ipaddr2 )
    return compare( network1, broadcast1, network2, broadcast2 )

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

def compare(net1, broad1, net2, broad2):
    if net1 >= net2 and broad1 <= broad2:
        return True
    else:
        return False

def validateCtrl( controllers, inputString ):
    key = inputString.split( ',' )
    if controllers.has_key(key[ 0 ]):
        if key[ 0 ] == 'remote':
            addresses = key[1: ]
            for ip in addresses:
                if not validateIP( ip ):
                    return False
            return True
        return True
    return False

def validateIP( ip ):
    ip = ip.split( '.' )
    if len( ip ) <= 1 and len( ip ) > 4:
        return False
    for i in ip:
        if not i.isdigit() or i == '' or int( i ) > 255 or int ( i ) < 0:
            return False
    return True

def validateMultiCtrl( inputString ):
    if inputString == False:
        return None
    #if inputString.find( ':' ) == -1:
    #    return False
    entries = inputString.split( ':' )
    for entry in entries:
        switch, comma, controller = entry.partition( ',' )
        if not switch.startswith( 's' ):
            return False
        controllers = controller.split( ',' )
        for c in controllers:
            if not c.startswith( 'c' ):
                return False
    return True

def validateNetSplit( inputString ):
    if inputString == False:
        return None
    if inputString.find( ':' ) == -1:
        return False
    entries = inputString.split( ':' )
    for entry in entries:
        controller, comma, ipAddresses = entry.partition( ',' )
        if not controller.startswith( 'c' ):
            return False
        ipAddresses = ipAddresses.split(',')
        for ip in ipAddresses:
            if not validateIPAddr( ip ):
                return False
    return True

def validateIPAddr( ip ):
    if ip.find( '/' ) == -1:
        return False
    network, subnet = ip.split( '/' )
    if subnet == '' or not subnet.isdigit():
        return False
    return validateIP( network )
