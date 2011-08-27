
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "历史今天"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "习题全解"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "趣味百科"; icon: "menu/app.png"; cmd: "menu/none.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
}

