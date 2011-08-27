
import QtQuick 1.0

Image { 
         property string path: "menu/tools/curriculum/"
         source: path+"bg.jpg"; 
         anchors.centerIn: parent 
         ExitIcon{ x:730;y:800; cmd:path+"../main.qml" }
}





