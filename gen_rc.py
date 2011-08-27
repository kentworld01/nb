
import os
import sys

#print sys.argv
if( len( sys.argv ) <= 1 ):
    print "%s rc_dir"%sys.argv[0]
    sys.exit(1)


dir = sys.argv[1]
fn = sys.argv[1] + ".qrc"
f = open(fn,"w")
rc_head="""<RCC>
    <qresource prefix="/">
"""
rc_bottom="""\t</qresource>
</RCC> 
"""



f.write( rc_head )
#f.write( "\t\t<file>qml/nb/m1.qml</file>\n" )
for root, dirs, files in os.walk( dir ):
        #print root
        #print dirs
        #print files
        for ff in files:
            fn = "%s\%s"%(root,ff)
            #print fn
            f.write( "\t\t<file>%s</file>\n"%fn )

f.write( rc_bottom )


