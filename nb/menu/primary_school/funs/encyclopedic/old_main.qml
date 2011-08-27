
import QtQuick 1.0

Rectangle {
    width: 1024
    height: 768
    color: "white"
    property string path: "menu/primary_school/funs/encyclopedic/"

    ListModel {
        id: appModel
        ListElement { name: "名言警句"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "对联集锦"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "星座知识"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "歇后语"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "生肖知识"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "笑话大王"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "精品阅读"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "绕口令"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "脑筋急转弯"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "血型知识"; icon: "menu/app.png"; cmd: "menu/none.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: path + "bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/primary_school/main.qml" }
}

