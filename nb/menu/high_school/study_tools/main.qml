
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "词典"; icon: "menu/app.png"; cmd_type: "auto"; cmd: "menu/dicts/main.qml" }
        ListElement { name: "语文"; icon: "menu/app.png"; cmd: "menu/high_school/study_tools/chinese/main.qml" }
        ListElement { name: "英语"; icon: "menu/app.png"; cmd: "menu/high_school/study_tools/english/main.qml" }
        ListElement { name: "数理化"; icon: "menu/app.png"; cmd: "menu/high_school/study_tools/math/main.qml" }
        ListElement { name: "史地政生"; icon: "menu/app.png"; cmd: "menu/high_school/study_tools/history/main.qml" }
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
}

