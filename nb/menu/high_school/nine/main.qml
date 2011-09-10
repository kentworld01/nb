
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "英语"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/英语"}
        ListElement { name: "语文"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/语文" }
        ListElement { name: "数学"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/数学"}
        ListElement { name: "物理"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/物理"}
        ListElement { name: "化学"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/化学"}
        ListElement { name: "历史"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/历史"}
        ListElement { name: "地理"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/地理"}
        ListElement { name: "政治"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/政治"}
        ListElement { name: "生物"; icon: "menu/app.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/生物"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

