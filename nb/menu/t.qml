
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    property string path: "menu/primary_school/funs/encyclopedic/"
    //property string data_path: "data/百科知识"
    Row{
    ListModel {
        id: appModel
        ListElement { name: "识"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
    }
    Rectangle{
        width:100
        height:100
        Text{
            text: "abcdef"
        }
    }
    }
    DirView{ dir: 's_dir_html_view_temp_dir'; board_x:430; board_y:130; board_width:400; board_height:320; listItem: appModel }
}

