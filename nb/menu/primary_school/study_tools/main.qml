
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "趣味记单词"; icon: "menu/app.png"; cmd_type:"auto"; cmd: "menu/none.qml" }
        ListElement { name: "动漫课堂"; icon: "menu/app.png"; cmd: "data/动漫课堂"}
        ListElement { name: "应用题训练"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "英语学习"; icon: "menu/app.png"; cmd_type: "dir"; cmd: "user/小学/学习工具/英语学习"}
        ListElement { name: "语文学习"; icon: "menu/app.png"; cmd_type: "dir"; cmd: "user/小学/学习工具/语文学习"}
        ListElement { name: "数学学习"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "词典大全"; icon: "menu/app.png"; cmd: "menu/dicts/main.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/primary_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

