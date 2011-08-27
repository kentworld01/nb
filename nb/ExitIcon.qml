import QtQuick 1.0
Rectangle{
         property string cmd
         property string cmd_type:"show"
         id: shockIcon
         x:0;y:0
         MouseArea{
                opacity: 0.1
                hoverEnabled: true
                onEntered: icon.width = 100
                onExited: icon.width = 0
         }

         Image {
             id: icon
             source: "images/view-refresh.png"
             MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onClicked: {
                    //doSelect( cmd_type, cmd )
                    doSelect( "quit", "" )
                }
                onEntered: {
                    icon.source= "images/view-refresh.png"
                    animation1.running = true;
                    animation2.running = true;
                }
                onExited: icon.source= "images/view-refresh.png"
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

