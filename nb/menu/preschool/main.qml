
import QtQuick 1.0

Image { 
         property string path: "menu/preschool/"
         source: path + "bg.jpg"; 
         anchors.centerIn: parent 
         ShockIcon{ x:110;y:320; cmd:"menu/none.qml" }
         ShockIcon{ x:190;y:130; cmd:"menu/none.qml" }
         ShockIcon{ x:370;y:50; cmd:"menu/none.qml" }
         ShockIcon{ x:400;y:180; cmd:"menu/main.qml" }
         ShockIcon{ x:550;y:150; cmd:"menu/none.qml" }
         ShockIcon{ x:790;y:220; cmd:"menu/none.qml" }
         ShockIcon{ x:400;y:500; cmd:"menu/none.qml" }
         ExitIcon{ x:900;y:530; cmd:"menu/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}





