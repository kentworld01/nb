
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "作文"; icon: "images/工具箱-语文/作文.png"; cmd_type: "auto"; cmd: "data/作文"}
        ListElement { name: "三字经"; icon: "images/工具箱-语文/三字经.png"; cmd: "data/三字经"}
        ListElement { name: "千字文"; icon: "images/工具箱-语文/千字文.png"; cmd: "data/千字文"}
        ListElement { name: "百家姓"; icon: "images/工具箱-语文/百家姓.png"; cmd: "data/百家姓"}
        ListElement { name: "弟子规"; icon: "images/工具箱-语文/弟子规.png"; cmd: "data/弟子规"}
        ListElement { name: "论语"; icon: "images/工具箱-语文/论语.png"; cmd: "data/论语"}
        ListElement { name: "诗歌欣赏"; icon: "images/工具箱-语文/诗歌欣赏.png"; cmd: "data/诗歌欣赏"}
        ListElement { name: "成语典故"; icon: "images/工具箱-语文/成语典故.png"; cmd: "data/成语典故"}
        ListElement { name: "古文观止"; icon: "images/工具箱-语文/古文观止.png"; cmd: "data/古文观止"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

