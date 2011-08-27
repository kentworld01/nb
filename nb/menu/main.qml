
import QtQuick 1.0

Image { 
        property string path: "menu/"
        source: path + "bg.jpg"; 
        anchors.centerIn: parent 
        ShockIcon{ x:520;y:150; cmd_type: "dir"; cmd: "user/学龄前" }
        ShockIcon{ x:520;y:350; cmd: path+"primary_school/main.qml" }
        ShockIcon{ x:780;y:150; cmd: path+"high_school/main.qml" }
        ShockIcon{ x:720;y:390; cmd: path+"tools/main.qml" }

        //ShockIcon{ x:0;y:0; cmd:"menu/t.qml" }
        //ShockIcon{ x:0;y:0; cmd_type:"test" }
}





