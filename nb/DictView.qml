
import QtQuick 1.0



Rectangle {
    id: dict_view

    width: icon_list_bg.width; height: icon_list_bg.height
    color: "white"
    property ListModel listItem:appModel
    property string bg: "images/dict_bg.jpg"
    property int board_x: 100
    property int board_y: 100
    property int board_width: 500
    property int board_height: 200
    property int currentIndex: 0
    property string dir: "."

    Image{
        id: icon_list_bg
        source: bg
        anchors.centerIn: parent 
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "key_study click" )
            }
        }

        Component {
            id: appDelegate
            Item {
                //x:50
                width: 200; height: 30
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { 
                        console.log( "dict value" )
                        var val = ""
                        val = dict_value.dict("sound", name )
                        sound.text = val
                        val = dict_value.dict("content", name )
                        content.text = val
                        input.text = name
                    }
                    onEntered: {
                        list.currentIndex = index
                        //animation1.running = true;
                        //animation2.running = true;
                    }
                    //onExited: list.currentIndex = -1
                }
                Row{
                    spacing:10
                    Text {
                        //anchors { top: myIcon.bottom; horizontalCenter: parent.horizontalCenter }
                        text: name
                        //font.family: "Simfang"
                        font.pixelSize: 24
                        smooth: true
                    }
                }
                /*
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
                */
            }
        }
    
        Component {
            id: appHighlight
            Rectangle { width: 200; height: 30; color: "lightsteelblue"; opacity:0.5 }
        }
    
        ListView {
            id: list
            //snapMode:ListView.NoSnap
            x:board_x 
            y:board_y + 80
            width: 200
            currentIndex: dict_view.currentIndex
            height:board_height-80
            //cellWidth: 200; cellHeight: 200
            highlight: appHighlight
            //highlightFollowsCurrentItem: tree
            highlightMoveSpeed: 4000000
            //focus: true
            model: listItem
            delegate: appDelegate
            //Rectangle{ x:board_x ; y:board_y + 80; width: 200; height:board_height-80; anchors.fill: parent; color: "blue"; opacity:0.1; }
        }
        ScrollBar { scrollArea: list; width: 8; y: board_y + 80;height: list.height; anchors { right: list.right } }
        FocusScope {
            id:container
            x:200
            y:600
            width: 200
            height: 28
            //BorderImage { source: "images/lineedit.sci"; anchors.fill: parent }
            signal accepted
            property alias text: input.text
            property alias item:input
            //anchors.centerIn: parent
            TextInput{
                id: input
                width: parent.width - 12
                //anchors.centerIn: parent
                maximumLength:21
                font.pixelSize: 32;
                font.bold: true
                color: "blue"; 
                selectionColor: "mediumseagreen"
                focus: true
                //acceptableInput: true
                onAccepted:{
                    var val = dict_value.dict("no", input.text )
                    var tv = parseInt( val )
                    console.log( tv )
                    list.positionViewAtIndex ( tv, ListView.Beginning )
                    user_input( input.text );

                    //var val = ""
                    //val = dict_value.dict("sound", input.text )
                    //sound.text = val
                    //val = dict_value.dict("content", input.text )
                    //content.text = val
                    container.accepted()
                }
                text: "请输入字词"
                selectByMouse: true
            }
        }
    }

}
