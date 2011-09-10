import QtQuick 1.0
import "."
Rectangle
{
    id: main
    width:1024
    height:768
    anchors.centerIn: parent
    signal cmd( string type, string path )
    function doSelect( cmd_type, cmd_str ){
        console.log( "do Select" )
        console.log( cmd_type )
        console.log( cmd_str )
        cmd( cmd_type, cmd_str )
    }
    focus: true
    //property url qmlFile: 'tmp.qml'
    property url qmlFile: ''
    property string code: ""
    property string page_no: ""
    property bool show: true

    Item{ id:embeddedViewer
        width: parent.width
        height: parent.height
        opacity: 0;
        z: 10
        Loader{
            id: loader
            z: 10
            focus: true //Automatic FocusScope
            clip: true
            source: qmlFile
            anchors.centerIn: parent
            function key_press(event){
                console.log( event.key )
                if (event.key == Qt.Escape ) { 
                    //console.log( "----" )
                    cmd( "quit", "" ) 
                }
                if (event.key == 16777216 ) { 
                    //console.log( "----" )
                    cmd( "quit", "" ) 
                }
                if( event.key >= 48 && event.key <= 57 ){
                    page_no += String.fromCharCode(event.key)
                    console.log( page_no )
                }
                else if( event.key == 16777220 ){
                    console.log( page_no )
                    cmd( "text_book_go_page", page_no )
                    page_no = ""
                }
                else{
                    page_no = ""
                }
            }
            onStatusChanged:{
                if(status == Loader.Null) {
                    loader.focus = false;
                }else if(status == Loader.Ready) {
                    Qt.createQmlObject( main.code, loader )
                    loader.focus= true
                }else{ console.log( "status other" ) }
            }
            Keys.onPressed: { key_press( event ) }

        }
        
        Rectangle{ id: frame
            z: 9
            anchors.fill: loader.status == Loader.Ready ? loader : errorTxt
            anchors.margins: -8
            radius: 4
            smooth: true
            border.color: "#88aaaaaa"
            gradient: Gradient{
                GradientStop{ position: 0.0; color: "#14FFFFFF" }
                GradientStop{ position: 1.0; color: "#5AFFFFFF" }
            }
            MouseArea{
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton | Qt.RightButton | Qt.MiddleButton
                onClicked: loader.focus=true;/* and don't propagate to the 'exit' area*/
            }

            Rectangle{ id: innerFrame
                anchors.margins: 7
                anchors.bottomMargin: 8
                anchors.rightMargin: 8
                color: "black"
                border.color: "#44000000"
                anchors.fill:parent
            }

        }
        /*
        Rectangle{ id: closeButton
            width: 24
            height: 24
            z: 11
            border.color: "#aaaaaaaa"
            gradient: Gradient{
                GradientStop{ position: 0.0; color: "#34FFFFFF" }
                GradientStop{ position: 1.0; color: "#7AFFFFFF" }
            }
            anchors.left: frame.right
            anchors.bottom: frame.top
            anchors.margins: -(2*width/3)
            Text{
                text: 'X'
                font.bold: true
                color: "white"
                font.pixelSize: 12
                anchors.centerIn: parent
            }
            MouseArea{
                anchors.fill: parent
                //onClicked: main.show = false;
                onClicked: main.show = true;
            }
        }
        */
        Text{
            id: errorTxt
            z: 10
            anchors.centerIn: parent
            color: 'white'
            smooth: true
            visible: loader.status == Loader.Error
            textFormat: Text.RichText
            //Note that if loader is Error, it is because the file was found but there was an error creating the component
            //This means either we have a bug in our demos, or the required modules (which ship with Qt) did not deploy correctly
            text: "The example has failed to load.<br />If you installed all Qt's C++ and QML modules then this is a bug!<br />"
                + 'Report it at <a href="http://bugreports.qt.nokia.com">http://bugreports.qt.nokia.com</a>';
            onLinkActivated: Qt.openUrlExternally(link);
        }
    }
    Rectangle{ id: blackout //Maybe use a colorize effect instead?
        z: 8
        anchors.fill: parent
        color: "#000000"
        opacity: 0.3
    }
    states: [
        State {
            name: "show"
            when: show == true
            PropertyChanges {
                target: embeddedViewer
                opacity: 1
            }
            PropertyChanges {
                target: blackout
                opacity: 0.5
            }
        }
    ]
    transitions: [//Should not be too long, because the component has already started running
        Transition { from: ''; to: "show"; reversible: true
            ParallelAnimation{
                NumberAnimation{ properties: "opacity"; easing.type: Easing.InQuad; duration: 500}
                PropertyAction { target: loader; property: "focus"; value: true}//Might be needed to ensure the focus stays with us
            }
        }
    ]
}

