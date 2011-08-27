# -*- coding: utf8 -*-

import os
import sys
import pickle
import pprint
import codecs

def chop( str ):
    if len( str ) <= 0 :
        return str
    while ord( str[-1] ) == 0xd or ord( str[-1] ) == 0xa :
        str = str[:-1]
        if len( str ) <= 0 :
            break;
    return str

def create_dict( name ):
    dict = {}
    name = name.decode('utf8')
    print name
    #f = open( '%s/%s.txt'%(name,name), 'r' )
    f = codecs.open( '%s/%s.txt'%(name,name), 'r', 'utf-8' )
    f.read(2)
    lines = f.read().split('\n')
    f.close()
    count = 0
    for l in lines:
        l = chop(l)
        if( len( l ) <= 2 ):
            continue
        iis = l.split( '\t' )
        if len(iis) > 2:
            print "up two item"
            print l
            print count
            sys.exit(0)
        if len(iis) <= 1:
            print "not enough item"
            print l
            print count
            sys.exit(0)
        key = iis[0]
        value = "\t%s"%iis[1]
        print key
        dict[ key ] = value
        count = count + 1
    f = open( '%s.jpg'%name, 'wb' )
    #pickle.dump( dict, f )
    pickle.dump( dict, f, -1 )
    f.close()
    print count
    return 'ok'

def create_dict_2( name ):
    dict = {}
    name = name.decode('utf8')
    print name
    f = codecs.open( '%s/%s.txt'%(name,name), 'r', 'utf-8' )
    #f = open( '%s/%s.txt'%(name,name), 'r' )
    f.read(2)
    lines = f.read().split('\n')
    f.close()
    count = 0
    for l in lines:
        l = chop(l)
        if( len( l ) <= 2 ):
            continue
        iis = l.split( '\t' )
        if len(iis) > 3:
            print "up three item"
            print l
            print count
            sys.exit(0)
        if len(iis) <= 1:
            print "not enough item"
            print l
            print count
            sys.exit(0)
        key = iis[0]
        print key
        value = "%s\t%s"%(iis[1],iis[2])
        #dict[ iis[0] ] = iis[1]
        dict[ key ] = value
        count = count + 1
    f = open( '%s.jpg'%name, 'wb' )
    #pickle.dump( dict, f )
    pickle.dump( dict, f, -1 )
    f.close()
    print count
    return 'ok'

def create_dict_3( name ):
    dict = {}
    name = name.decode('utf8')
    print name
    f = codecs.open( '%s/%s.txt'%(name,name), 'r', 'utf-8' )
    #f = codecs.open( p, "r", "utf-8" )
    f.read(2)
    lines = f.read().split('\n')
    f.close()
    count = 0
    line_count = 0
    value = ""
    key = ""
    for l in lines:
        l = chop(l)
        if( len( l ) <= 2 ):
            continue
        iis = l.split( '\t' )
        if len(iis) > 2:
            print "up two item"
            print l
            print count
            sys.exit(0)
        if len(iis) <= 1:
            print "not enough item"
            print l
            print count
            sys.exit(0)
        if iis[0] == "":
            value += iis[1]
            value += '\n'
        else:
            if key != "":
                dict[ key ] = value
                print len( key )
                print key[0]
                print key.encode('utf8')
                print "key=%s"%key
                #print "value=%s"%value
                print count
                count = count + 1
            key = iis[0]
            value = "\t%s"%(iis[1])
        print line_count
        line_count = line_count + 1
    f = open( '%s.jpg'%name, 'wb' )
    #pickle.dump( dict, f )
    pickle.dump( dict, f, -1 )
    f.close()
    print count
    return 'ok'

def create_dict_4( name ):
    dict = {}
    name = name.decode('utf8')
    print name
    #f = open( '%s/%s.txt'%(name,name), 'r' )
    f = codecs.open( '%s/%s.txt'%(name,name), 'r', 'utf-8' )
    f.read(2)
    lines = f.read().split('\n')
    f.close()
    count = 0
    for l in lines:
        l = chop(l)
        if( len( l ) <= 2 ):
            continue
        iis = l.split( '#' )
        if len(iis) > 2:
            print "up two item"
            print l
            print count
            sys.exit(0)
        if len(iis) <= 1:
            print "not enough item"
            print l
            print count
            sys.exit(0)
        key = iis[0]
        value = "\t%s"%iis[1]
        print key
        dict[ key ] = value
        count = count + 1
    f = open( '%s.jpg'%name, 'wb' )
    #pickle.dump( dict, f )
    pickle.dump( dict, f, -1 )
    f.close()
    print count
    return 'ok'



if __name__ == '__main__':
    create_dict( '成语词典' )
    create_dict( '汉英词典' )
    create_dict_2( '古代汉语' )
    create_dict_4( '新英汉' )
    create_dict_3( '现代汉语' )

    sys.exit(0)


