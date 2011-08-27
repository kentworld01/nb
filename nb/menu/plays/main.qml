
import QtQuick 1.0

Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "我的博客"; icon: "menu/app.png"; cmd_type:"auto"; cmd: "menu/none.qml"}
        ListElement { name: "我的相册"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "电子图书"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "动漫"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "影音"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "音乐"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "游戏"; icon: "menu/app.png"; cmd: "data/游戏"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/main.qml" }
}

