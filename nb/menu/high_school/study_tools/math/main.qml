
import QtQuick 1.0



Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "元素周期表"; icon: "images/工具箱-数理化/元素周期表.png"; cmd_type: "auto"; cmd: "menu/none.qml"}
        ListElement { name: "单位换算"; icon: "images/工具箱-数理化/单位换算.png"; cmd: "data/单位转换"}
        //ListElement { name: "单位转换"; icon: "images/工具箱-数理化/单位转换.png"; cmd: "data/单位转换"}
        ListElement { name: "习题全解"; icon: "images/工具箱-数理化/习题全解.png"; cmd: "menu/none.qml"}
        ListElement { name: "科学计算"; icon: "images/工具箱-数理化/科学计算.png"; cmd: "menu/none.qml"}
        ListElement { name: "计算器"; icon: "images/工具箱-数理化/计算器.png"; cmd: "menu/none.qml"}
        ListElement { name: "公式学习"; icon: "images/工具箱-数理化/公式学习.png"; cmd: "data/公式学习"}
        //ListElement { name: "化学公式"; icon: "images/工具箱-数理化/化学公式.png"; cmd: "user/中学/学习工具/数理化/t/化学公式"}
        //ListElement { name: "数学公式"; icon: "images/工具箱-数理化/数学公式.png"; cmd: "user/中学/学习工具/数理化/t/数学公式"}
        //ListElement { name: "物理公式"; icon: "images/工具箱-数理化/物理公式.png"; cmd: "user/中学/学习工具/数理化/t/物理公式"}
    }
    IconList{ board_x:200; board_y:100; board_width:600; board_height:500; bg: "menu/primary_school/study_tools/bg.jpg"; listItem: appModel }
    ExitIcon{ x:900;y:530; cmd:"menu/high_school/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}

