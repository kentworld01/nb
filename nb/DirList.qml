
import QtQuick 1.0



Rectangle {

    width: icon_list_bg.width; height: icon_list_bg.height
    color: "white"
    property ListModel listItem:appModel
    property string bg: "menu/bg.jpg"
    property int board_x: 100
    property int board_y: 100
    property int board_width: 500
    property int board_height: 400
    property string dir: "."

    Image{
        id: icon_list_bg
        source: bg
        anchors.centerIn: parent 


/*
        Rectangle{
            width:200
            height:50
            Button{}
            onClicked:{
                doSelect( "up_dir", dir )
            }
        }
*/
        
            Button {
                id: backButton
                action: webView.back; image: "pics/go-previous-view.png"
                anchors { left: parent.left; bottom: parent.bottom }
            }
        Component {
            id: appDelegate
            Item {
                width: 200; height: 30
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { 
                        doSelect( "dir", cmd ) 
                    }
                    onEntered: {
                        grid.currentIndex = index
                        animation1.running = true;
                        animation2.running = true;
                    }
                    //onExited: grid.currentIndex = -1
                }
                Row{
                    spacing:10
                Image {
                    id: myIcon
                    y: 20; 
                    //anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    source: "images/plus-sign.png" 
                    //source: icon ? icon : "images/plus-sign.png" 
                    //source: icon
                }
                Text {
                    //anchors { top: myIcon.bottom; horizontalCenter: parent.horizontalCenter }
                    text: name
                    //font.family: "Simfang"
                    font.pixelSize: 24
                    smooth: true
                }
                }
                SequentialAnimation on x {
                    running:false
                    id:animation1
                    loops:20
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
                    loops:20
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
            Rectangle { width: 200; height: 30; color: "lightsteelblue"; opacity:0.5 }
        }
    
        ListView {
            id: grid
            x:board_x
            y:board_y
            width:board_width
            height:board_height
            //cellWidth: 200; cellHeight: 200
            highlight: appHighlight
            focus: true
            model: listItem
            delegate: appDelegate
        }
        //ScrollBar { scrollArea: list; height: list.height; width: 8; anchors.right: window.right }
    }

}
