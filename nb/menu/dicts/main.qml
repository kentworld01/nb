
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "新英汉"; icon: "images/工具箱-词典/新英汉.png"; cmd_type: "dict"; cmd: "新英汉"}
        ListElement { name: "英汉有声"; icon: "images/工具箱-词典/英汉有声.png"; cmd: "menu/none.qml"}
        ListElement { name: "动漫词典"; icon: "images/工具箱-词典/动漫词典.png"; cmd: "menu/none.qml"}
        ListElement { name: "现代汉语"; icon: "images/工具箱-词典/现代汉语.png"; cmd_type: "dict"; cmd: "现代汉语"}
        ListElement { name: "成语词典"; icon: "images/工具箱-词典/成语词典.png"; cmd_type: "dict"; cmd: "成语词典"}
        ListElement { name: "汉英词典"; icon: "images/工具箱-词典/汉英词.png"; cmd_type: "dict"; cmd: "汉英词典"}
        ListElement { name: "古代汉语"; icon: "images/工具箱-词典/古代汉语.png"; cmd_type: "dict"; cmd: "古代汉语"}
        ListElement { name: "描红词典"; icon: "images/工具箱-词典/描红词典.png"; cmd_type: "auto"; cmd: "data/动漫字"}
        //ListElement { name: "下载词典"; icon: "images/工具箱-词典/.png"; cmd: "menu/none.qml"}
        //ListElement { name: "生词库"; icon: "images/工具箱-词典/.png"; cmd: "menu/none.qml"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

