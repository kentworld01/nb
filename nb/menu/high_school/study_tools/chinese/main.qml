
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "作文"; icon: "menu/app.png"; cmd_type: "auto"; cmd: "user/中学/学习工具/语文/作文/作文"}
        ListElement { name: "三字经"; icon: "menu/app.png"; cmd: "data/三字经"}
        ListElement { name: "千字文"; icon: "menu/app.png"; cmd: "data/千字文"}
        ListElement { name: "百家姓"; icon: "menu/app.png"; cmd: "data/百家姓"}
        ListElement { name: "弟子规"; icon: "menu/app.png"; cmd: "data/弟子规"}
        ListElement { name: "论语"; icon: "menu/app.png"; cmd: "data/论语"}
        ListElement { name: "诗歌欣赏"; icon: "menu/app.png"; cmd: "data/诗歌欣赏"}
        ListElement { name: "成语典故"; icon: "menu/app.png"; cmd: "data/成语典故"}
        ListElement { name: "古文观止"; icon: "menu/app.png"; cmd: "data/古文观止"}
        //ListElement { name: "精品阅读"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "习题全解"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "典故"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "唐诗"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "宋词"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "成语"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "文学常识"; icon: "menu/app.png"; cmd: "menu/none.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
}

