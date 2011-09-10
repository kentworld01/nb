
import QtQuick 1.0

Image { 
         property string path: "menu/primary_school/"
         source: path + "bg.jpg"; 
         anchors.centerIn: parent 
         ShockIcon{ x:120;y:330; cmd_type: "dir"; cmd: "user/小学/电子课本" }
         ShockIcon{ x:330;y:280; cmd:path + "study_tools/main.qml" }
         ShockIcon{ x:530;y:290; cmd:path + "funs/main.qml" }
         ShockIcon{ x:720;y:300; cmd_type: "dir"; cmd:'user/小学/动漫教学' }
         ExitIcon{ x:960;y:580; cmd:path + "../main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}





