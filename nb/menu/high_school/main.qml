
import QtQuick 1.0

Image { 
         property string path: "menu/high_school/"
         source: path + "bg.jpg"; 
         anchors.centerIn: parent 
         ShockIcon{ x:480;y:230; cmd_type: "auto"; cmd:path + "nine/main.qml" }
         ShockIcon{ x:680;y:260; cmd:path + "study_tools/main.qml" }
         ShockIcon{ x:910;y:250; cmd:"menu/plays/main.qml" }
         ExitIcon{ x:940;y:530; cmd:path + "../main.qml" }
}





