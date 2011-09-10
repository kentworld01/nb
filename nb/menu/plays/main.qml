
import QtQuick 1.0

Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "博客"; icon: "images/开心一刻/博客.png"; cmd_type:"auto"; cmd: "menu/none.qml"}
        ListElement { name: "相册"; icon: "images/开心一刻/相册.png"; cmd: "menu/none.qml"}
        ListElement { name: "电子书"; icon: "images/开心一刻/电子书.png"; cmd: "menu/none.qml"}
        ListElement { name: "动漫"; icon: "images/开心一刻/动漫.png"; cmd: "menu/none.qml"}
        ListElement { name: "影音"; icon: "images/开心一刻/影音.png"; cmd: "menu/none.qml"}
        ListElement { name: "音乐"; icon: "images/开心一刻/音乐.png"; cmd: "menu/none.qml"}
        ListElement { name: "游戏"; icon: "images/开心一刻/游戏.png"; cmd: "data/游戏"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

