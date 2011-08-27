
import QtQuick 1.0



Rectangle {

    width: icon_list_bg.width; height: icon_list_bg.height
    color: "white"
    property ListModel listItem
    property string bg: "menu/bg.jpg"
    property int board_x: x
    property int board_y: y
    property int board_width: width
    property int board_height: height

    Image{
        id: icon_list_bg
        source: bg
        anchors.centerIn: parent 

        Component {
            id: appDelegate
            Item {
                //property string cmd_type: "auto"
                width: 150; height: 150
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { 
                        var type = "auto"
                        if( ""+cmd_type != "undefined")
                            type = cmd_type
                        doSelect( type, cmd ) 
                    }
                    onEntered: {
                        grid.currentIndex = index
                        animation1.running = true;
                        animation2.running = true;
                    }
                    //onExited: grid.currentIndex = -1
                }
                Image {
                    id: myIcon
                    y: 20; anchors.horizontalCenter: parent.horizontalCenter
                    source: icon
                }
                Text {
                    anchors { top: myIcon.bottom; horizontalCenter: parent.horizontalCenter }
                    text: name
                    //font.family: "Simfang"
                    font.pixelSize: 24
                    smooth: true
                }
                SequentialAnimation on x {
                    running:false
                    id:animation1
                    loops:50
                    PropertyAnimation{
                        easing.type:Easing.InOutElastic; to:x+8; duration:10
                    }
                    PropertyAnimation{
                        easing.type:Easing.OutInElastic; to:x+0; duration:10
                    }
                }
                SequentialAnimation on y{
                    id:animation2
                    running:false
                    loops:50
                    PropertyAnimation{
                        easing.type:Easing.InOutBounce; to:y+8; duration:10
                    }
                    PropertyAnimation{
                        easing.type:Easing.OutInBounce; to:y+0; duration:10
                    }
                }
            }
        }
    
        Component {
            id: appHighlight
            Rectangle { width: 80; height: 80; color: "lightsteelblue"; opacity:0.5 }
        }
    
        GridView {
            id: grid
            x:board_x
            y:board_y
            width:board_width
            height:board_height
            cellWidth: 150; cellHeight: 150
            highlight: appHighlight
            focus: true
            model: listItem
            delegate: appDelegate
        }
    }

}
