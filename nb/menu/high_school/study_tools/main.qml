
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "词典"; icon: "images/工具箱/词典.png"; cmd_type: "auto"; cmd: "menu/dicts/main.qml" }
        ListElement { name: "语文"; icon: "images/工具箱/语文.png"; cmd: "menu/high_school/study_tools/chinese/main.qml" }
        ListElement { name: "英语"; icon: "images/工具箱/英语.png"; cmd: "menu/high_school/study_tools/english/main.qml" }
        ListElement { name: "数理化"; icon: "images/工具箱/数理化.png"; cmd: "menu/high_school/study_tools/math/main.qml" }
        ListElement { name: "史地政生"; icon: "images/工具箱/史地生政.png"; cmd: "menu/high_school/study_tools/history/main.qml" }
        //ListElement { name: "史地政生"; icon: "images/工具箱/史地政生.png"; cmd: "menu/high_school/study_tools/history/main.qml" }
        ListElement { name: "仿真实验"; icon: "images/工具箱/仿真实验.png"; cmd_type: "dir"; cmd: "user/中学/仿真实验" }
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

