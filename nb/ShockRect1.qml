import QtQuick 1.0

Rectangle{
    property string cmd
    property string cmd_type: "show"
    x:0;y:0
    width:100
    height:100
    anchors.centerIn: parent
    color:"green"

    Rectangle{
         id: icon
         //x:0;y:0
         //width:100
         //height:100
         opacity: 0.3
         color:"green"
            anchors.centerIn: parent

         //source: "images/big-sun.png"
         MouseArea{
            anchors.fill: parent
            hoverEnabled: true
            onClicked: {
                doSelect( cmd_type, cmd )
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
            loops:50
            PropertyAnimation{
                easing.type:Easing.InOutElastic; to:8; duration:10
            }
            PropertyAnimation{
                easing.type:Easing.OutInElastic; to:0; duration:10
            }
        }
        SequentialAnimation on y{
            id:animation2
            running:false
            loops:50
            PropertyAnimation{
                easing.type:Easing.InOutBounce; to:8; duration:10
            }
            PropertyAnimation{
                easing.type:Easing.OutInBounce; to:0; duration:10
            }
        }
    }
}

