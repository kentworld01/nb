
import QtQuick 1.0
import QtWebKit 1.0



Rectangle {
    id: dir_html_view

    width: icon_list_bg.width; height: icon_list_bg.height
    color: "white"
    property ListModel listItem:appModel
    property string bg: "images/list_bg.png"
    //property string bg: "menu/bg.jpg"
    property int board_x: 100
    property int board_y: 100
    property int board_width: 500
    property int board_height: 400
    property string dir: "."

    Image{
        id: icon_list_bg
        source: bg
        anchors.centerIn: parent 

        Button {
            id:up_button
            x:board_x 
            y:board_y
            width:400
            height:50
            //action: webView.back; 
            image: "images/go-up-view.png"
            //anchors { left: parent.left; bottom: parent.bottom }
            //anchors.fill: parent
            onClicked:{
                doSelect( "up_dir", dir )
            }
            Rectangle{
                anchors.centerIn: parent
                x:parent.x+50
                width:parent.width-100
                color: "green"
                opacity:0.1
            }
        }
        Component {
            id: appDelegate
            Item {
                x:50
                width: 400; height: 30
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { 
                        doSelect( cmd_type, cmd ) 
                        //doSelect( "auto", cmd ) 
                    }
                    onEntered: {
                        list.currentIndex = index
                        animation1.running = true;
                        animation2.running = true;
                    }
                    //onExited: list.currentIndex = -1
                }
                Row{
                    spacing:10
                Image {
                    id: myIcon
                    y: 20; 
                    //anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    source: select_icon()
                    //source: "images/go-next-view.png" 
                    //source: icon ? icon : "images/plus-sign.png" 
                    //source: icon
                    function select_icon(){
                        //console.log( name )
                        var sub_name = name.substr( name.length-5, 5 )
                        //console.log( sub_name )
                        if( sub_name == ".html" ){
                            return "images/go-jump-locationbar.png"
                        }
                        return "images/go-next-view.png"
                    }
                }
                Text {
                    //anchors { top: myIcon.bottom; horizontalCenter: parent.horizontalCenter }
                    text: get_show_name()
                    //font.family: "Simfang"
                    font.pixelSize: 24
                    smooth: true
                    function get_show_name(){
                        var sub_name = name.replace(".html","")
                        sub_name = sub_name.replace("_百度百科","")
                        return sub_name
                    }
                }
                }
                SequentialAnimation on x {
                    running:false
                    id:animation1
                    loops:10
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
                    loops:10
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
            Rectangle { width: 400; height: 30; color: "lightsteelblue"; opacity:0.5 }
        }
    
        ListView {
            id: list
            //snapMode:ListView.NoSnap
            x:board_x 
            y:board_y + 80
            width: 400
            height:board_height-80
            //cellWidth: 400; cellHeight: 200
            highlight: appHighlight
            //focus: true
            model: listItem
            delegate: appDelegate
            //Rectangle{ x:board_x ; y:board_y + 80; width: 400; height:board_height-80; anchors.fill: parent; color: "blue"; opacity:0.1; }
        }
        ScrollBar { scrollArea: list; width: 8; y: board_y + 80;height: list.height; anchors { right: list.right } }
    }

}
