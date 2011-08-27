
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "元素周期表"; icon: "menu/app.png"; cmd_type: "auto"; cmd: "menu/none.qml"}
        ListElement { name: "单位转换"; icon: "menu/app.png"; cmd: "data/单位转换"}
        ListElement { name: "小学奥数"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "习题全解"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "科学计算"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "计算器"; icon: "menu/app.png"; cmd: "menu/none.qml"}
        ListElement { name: "公式学习"; icon: "menu/app.png"; cmd: "data/公式学习"}
        //ListElement { name: "化学公式"; icon: "menu/app.png"; cmd: "user/中学/学习工具/数理化/t/化学公式"}
        //ListElement { name: "数学公式"; icon: "menu/app.png"; cmd: "user/中学/学习工具/数理化/t/数学公式"}
        //ListElement { name: "物理公式"; icon: "menu/app.png"; cmd: "user/中学/学习工具/数理化/t/物理公式"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
}

