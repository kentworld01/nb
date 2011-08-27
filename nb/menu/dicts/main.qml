
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "新英汉"; icon: "menu/app.png"; cmd_type: "dict"; cmd: "新英汉"}
        ListElement { name: "英汉有声"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "动漫词典"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "现代汉语"; icon: "menu/app.png"; cmd_type: "dict"; cmd: "现代汉语"}
        ListElement { name: "成语词典"; icon: "menu/app.png"; cmd_type: "dict"; cmd: "成语词典"}
        ListElement { name: "汉英词典"; icon: "menu/app.png"; cmd_type: "dict"; cmd: "汉英词典"}
        ListElement { name: "古代汉语"; icon: "menu/app.png"; cmd_type: "dict"; cmd: "古代汉语"}
        ListElement { name: "描红词典"; icon: "menu/app.png"; cmd_type: "auto"; cmd: "data/动漫字"}
        //ListElement { name: "下载词典"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        //ListElement { name: "生词库"; icon: "menu/app.png"; cmd: "menu/none.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/main.qml" }
}

