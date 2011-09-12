
import os
import sys
import socket
import urllib2, urllib



def read_time_out( f, size ) :
    str = ''
    while 1:
        try :
            s = f.read( 1 )
            if len(s) == 0 :
                break;
            if size > 0 :
                size -= 1
            if size == 0 :
                break
        except:
            break
        str += s;
    return str


def get_page( web_add, post_data ):
    socket.setdefaulttimeout( 1 )
    #f = urllib.urlopen( web_add )
    #f = urllib2.urlopen( url = web_add, data = post_data)
    #s = read_time_out( f, -1 )
    #f.close()
    req = urllib2.Request( web_add, post_data )
    f = urllib2.urlopen(req)
    s = f.read()
    f.close()
    return s

def test():
    s = get_page( "https://124.248.35.165/punbb/login.php" )
    print s

def get_value( p, key ):
    ls = p.split( key )
    if len( ls ) < 2:
        return ''
    ls = ls[1].split( '/>' )
    #print ls[0]
    return ls[0][9:-2]

def login_by_wget( u,p ):
    rel = 0
    s = get_page( "https://124.248.35.165/punbb/login.php", '' )
    val = get_value( s, 'csrf_token' )
    str = "\"form_sent=1&save_pass=1&redirect_url=http://124.248.35.165:8080/punbb/login.php&csrf_token=%s&req_username=%s&req_password=%s\"" % (val, u, p)
    os.system( "del tt" )
    cmd = "wget --quiet -O tt -o t -T 10 --no-check-certificate --post-data=%s https://124.248.35.165/punbb/login.php" % str
    #cmd = "wget --quiet -o tt -T 10 --no-check-certificate --post-data=%s https://124.248.35.165/punbb/login.php" % str
    #print cmd
    os.system( cmd )
    f = open( "tt", "r" )
    fl = f.read()
    f.close()
    iis = fl.split( 'Logged in successfully' )
    print len( iis )
    if len( iis ) >= 2 :
        print "login ok"
        return 1
    return 0


def login_by_urllib( u,p ):
    rel = 0
    # get csrf_token
    s = get_page( "https://124.248.35.165/punbb/login.php", '' )
    val = get_value( s, 'redirect_url' )
    #print val
    val = get_value( s, 'csrf_token' )
    #print val
    # try login
    if 0:
        str = {'form_send':'1'}
        data = urllib.urlencode( str )
        str = {'redirect_url':'http://124.248.35.165:8080/punbb/login.php'}
        #str = {'redirect_url':'https://124.248.35.165/punbb/login.php'}
        data += '&' + urllib.urlencode( str )
        str = {'csrf_token':val}
        data += '&' + urllib.urlencode( str )
        str = {'req_username':u}
        data += '&' + urllib.urlencode( str )
        str = {'req_password':p}
        data += '&' + urllib.urlencode( str )
        str = {'save_pass':'1'}
        data += '&' + urllib.urlencode( str )
        str = {'login':'Login'}
        data += '&' + urllib.urlencode( str )
    else:
        str = {'form_send':'1','save_pass':'1','redirect_url':'https://124.248.35.165/punbb/index.php','csrf_token':val,'req_username':u,'req_password':p, 'login':'Login' }
        data = urllib.urlencode( str )
    #print data
    s = get_page( "https://124.248.35.165/punbb/login.php", data )
    #print s
    s = get_page( "https://124.248.35.165/punbb/index.php", '' )
    print s
    return rel

def main():
    #test()
    login_by_wget( 'pig', '123456_' )


if __name__ == '__main__':
    main()


