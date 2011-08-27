
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"
    property string path: "menu/primary_school/funs/"

    ListModel {
        id: appModel
        ListElement { name: "百科知识"; icon: "menu/app.png"; cmd_type: "auto"; cmd: "data/百科知识" }
        ListElement { name: "词典大全"; icon: "menu/app.png"; cmd: "menu/dicts/main.qml"}
        ListElement { name: "乐园"; icon: "menu/app.png"; cmd: "menu/plays/main.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: path + "bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/primary_school/main.qml" }
}

