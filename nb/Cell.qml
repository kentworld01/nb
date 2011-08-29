import QtQuick 1.0

Item {
    id: page
    //width: 640; height: 480
    //color: "#343434"
    property int nx:0
    property int ny:0
    property string en: "test"
    property string cn: ""

    property color color: "black"
    //property state now_state: ""
    width:300
    height:40

    Rectangle { 
        width:300
        height:40
        x: 0
        y: 0
        opacity: 0.6
        color: parent.color
        border.color: "White"; border.width: 2
        radius: 12
        MouseArea{
            anchors.fill:parent
            onClicked:{
                if( page.cn != "" ){
                    page.parent.nx = page.x
                    page.parent.ny = page.y
                    //page.parent.en = page.en
                    page.parent.cn_object = page
                }
                else{
                    if( page.parent.nx != 0 ){
                        if( page.state == "" ){
                            //page.nx = page.parent.nx - page.x
                            //page.ny = page.parent.ny - page.y
                            page.nx = page.parent.nx
                            page.ny = page.parent.ny
                            page.state = "move"

                            // for answer check
                            if( page.parent.cn_object.en == page.en ){
                                //console.log( "answer ok" )
                                page.parent.cn_object.y = -100
                                page.en = page.en + " --- " + page.parent.cn_object.cn
                                page.parent.nx = 0
                                page.parent.ny = 0
                            }
                        }
                        else{
                            page.state = ""
                        }
                    }
                }
            }
        }
    }
    Text{
        anchors.centerIn: parent
        color: "white"
        font.pixelSize: 24
        text: page.cn != "" ? page.cn : page.en
    }
    states: [
        State {
            name: "move"
            PropertyChanges { target: page; x: nx; y: ny }
        }
    ]
    transitions: [
        Transition {
            NumberAnimation { properties: "x,y"; easing.type: Easing.OutBounce; duration: 1000 }
        }
    ]
}

