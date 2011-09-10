
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "三步互动"; icon: "images/工具箱-英语/三步互动.png"; cmd_type: "auto"; cmd: "menu/none.qml"}
        ListElement { name: "中学语法"; icon: "images/工具箱-英语/中学语法.png"; cmd: "data/中学语法"}
        ListElement { name: "动词变化"; icon: "images/工具箱-英语/动词变化.png"; cmd: "menu/none.qml"}
        ListElement { name: "单词听写"; icon: "images/工具箱-英语/单词听写.png"; cmd: "menu/none.qml"}
        ListElement { name: "国际音标"; icon: "images/工具箱-英语/国际音标.png"; cmd: "menu/none.qml"}
        ListElement { name: "情景会话"; icon: "images/工具箱-英语/情景会话.png"; cmd: "menu/none.qml"}
        ListElement { name: "模拟考场"; icon: "images/工具箱-英语/模拟考场.png"; cmd: "menu/none.qml"}
        ListElement { name: "习题全解"; icon: "images/工具箱-英语/习题全解.png"; cmd: "menu/none.qml"}
        ListElement { name: "英语写作"; icon: "images/工具箱-英语/英语写作.png"; cmd: "data/英语写作"}
        ListElement { name: "英语谚语"; icon: "images/工具箱-英语/英语谚语.png"; cmd: "data/英语谚语"}
        ListElement { name: "幽默英语"; icon: "images/工具箱-英语/幽默英语.png"; cmd: "data/幽默英语"}
        ListElement { name: "英语考试简介"; icon: "images/工具箱-英语/英语考试简介.png"; cmd: "data/英语考试简介"}
        //ListElement { name: "魔法英语"; icon: "images/工具箱-英语/魔法英语.png"; cmd: "data/英语游戏75/SWF"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

