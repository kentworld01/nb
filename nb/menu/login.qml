import QtQuick 1.0
Rectangle {
    id:dict_page
    width: 1024
    height: 768
    color: "black"
    property int remeber_password_flag: 0
    property int auto_login_flag: 0
    function do_login(){
            console.log( "call login" )
            var str
            str = "do_login" + " " + auto_login_flag + " " + remeber_password_flag + " " + user.text + " " + password.text
            console.log( str )
            doSelect( "do_login", str )
    }

    Image{
        //anchors.fill: parent
        anchors.centerIn: parent
        source: "images/登录1.jpg"
    }
    Rectangle {
        id:remeber_password
        x:588
        y:434
        width:10
        height:10
        opacity: 0.3
        color:"blue"
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "remeber password click" )
                if( remeber_password_flag == 0 ){
                    remeber_password.color = "red"
                    remeber_password_flag = 1;
                }
                else{
                    remeber_password.color = "blue"
                    remeber_password_flag = 0;
                }
            }
        }
    }
    Rectangle {
        id:auto_login
        x:670
        y:434
        width:10
        height:10
        opacity: 0.3
        color:"s_auto_login_color"
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "auto login click" )
                if( auto_login_flag == 0 ){
                    auto_login.color = "red"
                    auto_login_flag = 1;
                }
                else{
                    auto_login.color = "blue"
                    auto_login_flag = 0;
                }
            }
        }
    }
    Rectangle {
        id:login
        x:602
        y:465
        width:46
        height:30
        opacity: 0.3
        color:"blue"
        MouseArea{
            anchors.fill: parent
            onClicked:{
                do_login()
                console.log( "login click" )
            }
        }
    }
    TextInput{
        id: user
        x: 600
        y: 360
        width: parent.width - 12
        //anchors.centerIn: parent
        maximumLength:21
        font.pixelSize: 20;
        font.bold: true
        color: "red"; 
        selectionColor: "mediumseagreen"
        focus: true
        //acceptableInput: true
        onAccepted:{
            do_login()
            container.accepted()
        }
        text: "s_login_user"
        selectByMouse: true
    }
    TextInput{
        id: password
        x: 600
        y: 398
        width: parent.width - 12
        //anchors.centerIn: parent
        maximumLength:21
        font.pixelSize: 20;
        font.bold: true
        color: "red"; 
        selectionColor: "mediumseagreen"
        focus: true
        //acceptableInput: true
        onAccepted:{
            do_login()
            container.accepted()
        }
        text: "s_login_password"
        selectByMouse: true
    }
}




