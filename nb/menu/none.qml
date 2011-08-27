
import QtQuick 1.0

Image { 
         property string path: "menu/"
         source: path + "none.jpg"; 
         anchors.centerIn: parent 
         ExitIcon{ x:860;y:620; cmd: path+"main.qml" }
}





