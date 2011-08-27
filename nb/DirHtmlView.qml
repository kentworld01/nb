
import QtQuick 1.0
import QtWebKit 1.0



Rectangle {
    id: dir_html_view

    width: icon_list_bg.width; height: icon_list_bg.height
    color: "white"
    property ListModel listItem:appModel
    property string bg: "images/list_bg.jpg"
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

        Row{
            spacing: 50
        Item{
        Button {
            id:up_button
            x:board_x 
            y:board_y
            width:300
            height:50
            //action: webView.back; 
            image: "images/go-up-view.png"
            //anchors { left: parent.left; bottom: parent.bottom }
            //anchors.fill: parent
            onClicked:{
                console.log( "button click" )
                console.log( dir )
                var items = dir.split( "/" )
                console.log( items.length )
                items.pop()
                console.log( items.length )
                //items[ items.length-1 ] = ""
                dir = items.join("/")
                console.log( dir )
                doSelect( "dir", dir )
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
                width: 300; height: 30
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { 
                        console.log( dir )
                        console.log( cmd )
                        console.log( "ready test" )
                        var items = cmd.split( "." )
                        //console.log( items[0] )
                        console.log( items[1] )
                        if( items[1] == "html" ){
                            webBrowser.urlString = "../" + cmd
                            //webView.url = "../" + cmd
                            //webView.opacity:1
                            //animateOpacity.start()
                        }
                        else{
                            doSelect( "dir", cmd ) 
                        }
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
            Rectangle { width: 300; height: 30; color: "lightsteelblue"; opacity:0.5 }
        }
    
        ListView {
            id: list
            //snapMode:ListView.NoSnap
            x:board_x 
            y:board_y + 80
            width: 300
            height:board_height-80
            //cellWidth: 300; cellHeight: 200
            //highlight: appHighlight
            //focus: true
            model: listItem
            delegate: appDelegate
            //Rectangle{ x:board_x ; y:board_y + 80; width: 300; height:board_height-80; anchors.fill: parent; color: "blue"; opacity:0.1; }
        }
        ScrollBar { scrollArea: list; width: 8; y: board_y + 80;height: list.height; anchors { right: list.right } }
        }
        // webview
        /*
        WebBrowser{
                id: f_webView
                x:board_x + 350
                y:board_y 
                width: get_web_browser_width()
                //width:dir_html_view.board_width - x
                //width:500
                //height:300
                //height:dir_html_view.board_height
                function get_web_browser_width(){
                    console.log( dir_html_view.board_width )
                    console.log( dir_html_view.board_height )
                    return dir_html_view.board_widht - 350
                }
        }
        */
        Rectangle {
            id: webBrowser

            property string urlString : "../data/百科知识/地理/地貌/暗河/暗河.html"
            //property string urlString : "http://www.nokia.com/"

            color: "#343434"
            x:board_x + 350
            y:100 
            //y:board_y 
            width:board_width - x
            //height:board_height
            height:300

            //focus: true
            FlickableWebView {
                id: webView
                height:300
                url: webBrowser.urlString
                onProgressChanged: header.urlChanged = false
                anchors { top: headerSpace.bottom; left: webBrowser.left; right: webBrowser.right; bottom: webBrowser.bottom }
            }

            Item { id: headerSpace; width: webBrowser.width; height: 62 }

            Header {
                id: header
                editUrl: webBrowser.urlString
                width: headerSpace.width; height: headerSpace.height
            }

            ScrollBar {
                scrollArea: webView; width: 8
                //anchors { right: parent.right; top: header.bottom; bottom: parent.bottom }
                anchors { right: webBrowser.right; bottom: webBrowser.bottom }
            }

            ScrollBar {
                scrollArea: webView; height: 8; orientation: Qt.Horizontal
                anchors { right: webBrowser.right; rightMargin: 8; left: webBrowser.left; bottom: webBrowser.bottom }
            }
        }
        /*
        Rectangle{
            id: flashingblob
            //width: 75; height: 75
            //color: "blue"
            opacity: 0
            //focus: true
            WebView {
                id: webView
                //opacity:0
                x:board_x + 350
                y:board_y
                width:board_width - x
                height:board_height
                //url: "t.html"
                url: "../data/百科知识/地理/地貌/暗河/暗河.html"
            }
            ScrollBar { scrollArea: webView; width: 8; y: board_y ;height: webView.height; anchors { right: webView.right } }
            //ScrollBar { scrollArea: webView; y: board_y; height: webView.height; width: 8; anchors.right: webView.right }
            //ScrollBar { scrollArea: webView; width: 8; anchors { right: parent.right; bottom: parent.bottom } }
            

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    //animateColor.start()
                    console.log( "move" )
                    animateOpacity.start()
                }
            }
        
            //PropertyAnimation {id: animateColor; target: flashingblob; properties: "color"; to: "green"; duration: 100}
        
            NumberAnimation {
                id: animateOpacity
                target: flashingblob
                properties: "opacity"
                from: 0
                to: 1
                //loops: Animation.Infinite
                //easing {type: Easing.OutBack; overshoot: 500}
                duration: 1
            }
        
        }
        */

        }
    }

}
