
import QtQuick 1.0

Image { 
         property string path: "menu/tools/"
         source: path + "bg.jpg"; 
         anchors.centerIn: parent 
         ShockIcon{ x:110;y:50; cmd:"menu/plays/main.qml" }
         ShockIcon{ x:20;y:140; cmd:"menu/none.qml" }
         ShockIcon{ x:460;y:15; cmd:"menu/none.qml" }
         ShockIcon{ x:420;y:110; cmd:"menu/none.qml" }
         ShockIcon{ x:430;y:200; cmd:"menu/none.qml" }
         ShockIcon{ x:520;y:280; cmd:path + "curriculum/main.qml" }
         ExitIcon{ x:930;y:600; cmd:path + "../main.qml" }
         QuitIcon{ x:960;y:10; cmd:"menu/main.qml" }
}





