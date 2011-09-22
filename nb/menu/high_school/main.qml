
import QtQuick 1.0


Rectangle {
    width: 1024
    height: 768
    color: "white"

    ListModel {
        id: appModel
        ListElement { name: "工具箱"; icon: "images/首页/工具箱.png";  cmd_type: "auto"; cmd: "menu/high_school/study_tools/main.qml"}
        ListElement { name: "开心一刻"; icon: "images/首页/开心一刻.png";  cmd_type: "auto"; cmd: "menu/plays/main.qml"}
        ListElement { name: "英语"; icon: "images/首页/英语.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/英语"}
        ListElement { name: "语文"; icon: "images/首页/语文.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/语文" }
        ListElement { name: "数学"; icon: "images/首页/数学.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/数学"}
        ListElement { name: "物理"; icon: "images/首页/物理.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/物理"}
        ListElement { name: "化学"; icon: "images/首页/化学.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/化学"}
        ListElement { name: "历史"; icon: "images/首页/历史.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/历史"}
        ListElement { name: "地理"; icon: "images/首页/地理.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/地理"}
        ListElement { name: "政治"; icon: "images/首页/政治.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/政治"}
        ListElement { name: "生物"; icon: "images/首页/生物.png";  cmd_type: "dir"; cmd: "user/中学/九门功课/生物"}
        ListElement { name: "视频教学"; icon: "images/首页/视频教学.png";  cmd_type: "dir"; cmd: "user/小学/动漫教学"}
    }
    IconList{ board_x:200; board_y:150; board_width:600; board_height:500; bg: "images/中学主界面.jpg"; listItem: appModel }
    ExitIcon{ x:960;y:700; cmd:"menu/main.qml" }
    QuitIcon{ x:960;y:10; cmd:path + "../main.qml" }
}


