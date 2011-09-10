import QtQuick 1.0

    Rectangle{
    property string cmd
    property string cmd_type: "text_book_show_pos"
         id: icon
         x:0;y:0
         width:100
         height:100
         opacity: 0.01
         color:"blue"
         radius: 12
         border.color: "Black"; border.width: 2
         //anchors.centerIn: parent

         //source: "images/big-sun.png"
         MouseArea{
            anchors.fill: parent
            hoverEnabled: true
            onClicked: {
                //animation1.running = true;
                //animation2.running = true;
                doSelect( cmd_type, cmd )
                doSelectPoint( icon.x, icon.y+icon.height, icon.x + mouse.x, icon.y + mouse.y, cmd_type, cmd )
            }
            onEntered: {
                //icon.source= "images/big-face-smile.png"
                animation1.running = true;
                animation2.running = true;
            }
            //onExited: icon.source= "images/big-sun.png"
        }
        SequentialAnimation on x {
            running:false
            id:animation1
            loops:0
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
            loops:0
            PropertyAnimation{
                easing.type:Easing.InOutBounce; to:y+8; duration:10
            }
            PropertyAnimation{
                easing.type:Easing.OutInBounce; to:y+0; duration:10
            }
        }
    }

