# -*- coding: utf8 -*-

import os
import sys
import shutil
#import tarfile
import codecs
import zipfile
import re
import PySide.QtNetwork
import PySide.QtWebKit
import types
import urllib
import mp3play
import time
import random
import pickle
import pprint
#import deque
from collections import deque

from PySide import QtCore
from PySide import QtGui
from PySide import QtDeclarative
from PySide import QtOpenGL

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtXml import *

from PySide.QtDeclarative import QDeclarativeView
from PySide.QtDeclarative import QDeclarativeEngine
from PySide.QtDeclarative import QDeclarativeComponent

import nb_qrc

#nb_qrc.qInitResources()

g_path = "nb/"
#g_text_book_sub_name = "zip"
g_text_book_sub_name = "p"
#g_text_book_sub_name = ".p"
g_package_data_sub_name = "pd"
g_text_book_now_page = 1
g_qmlRoot = ""
g_view = ""
g_qml_lastest_string_list = []
g_qml_str_lastest_type = ""
g_mp3_play = ""
g_mp3_play_list = deque()
g_key = "#gaBteN!"
g_switch_sound = ""
g_rand_value = 10000000
g_dict = {}
g_text_book_data = ""
g_zf = ""
g_zf_path = ""
g_quit_command = "quit"










s_key_study_action_o = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    Image{
        anchors.centerIn: parent
        source: "s_text_book_page_bg_file"
    }
    Text{
        id:text1
        x:300
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text1"
    }
    Text{
        id:text2
        x:600
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text2"
    }
    Text{
        id:text3
        x:400
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text3"
    }
        Item{
            x:0
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-previous-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "prev page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_prev_page" )
                }
            }
        }
        Item{
            x:1024-48
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-next-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "next page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_next_page" )
                }
            }
        }
}
"""

s_key_study_action_k = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    Text{
        id:text1
        x:300
        y:200
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text1"
    }
    Text{
        id:text2
        x:400
        y:400
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text2"
    }
    Text{
        id:text3
        x:400
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text3"
    }
        Item{
            x:0
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-previous-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "prev page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_prev_page" )
                }
            }
        }
        Item{
            x:1024-48
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-next-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "next page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_next_page" )
                }
            }
        }
}
"""

s_key_study_action_b = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    Image{
        anchors.centerIn: parent
        source: "s_text_book_page_bg_file"
    }
    Text{
        id:text1
        x:300
        y:100
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text1"
    }
    Text{
        id:text2
        x:600
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text2"
    }
    Text{
        id:text3
        x:400
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text3"
    }
        Item{
            x:0
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-previous-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "prev page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_prev_page" )
                }
            }
        }
        Item{
            x:1024-48
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-next-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "next page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_next_page" )
                }
            }
        }
}
"""

s_key_study_action_m = """
import QtQuick 1.0
//import "file:///D:/pro/net_study/net_bag/nb"
Rectangle{
        width:1024
        height:768
        color: "black"
        property int nx: 0
        property int ny: 0
        //property string en: ""
        property variant cn_object
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "hello" )
            }
        }

        //Cell{color:"black";x:300;y:100; cn:"q"}
        //Cell{color:"black";x:300;y:200; cn:"q"}
        //Cell{color:"red";x:100;y:100}
        //Cell{color:"yellow";x:100;y:200}

"""

s_key_study_action_m_old3 = """
import QtQuick 1.0

/*
    This is exactly the same as states.qml, except that we have appended
    a set of transitions to apply animations when the item changes 
    between each state.
*/

Rectangle {
    id: page
    width: 640; height: 480
    color: "#343434"
    property int nx:0
    property int ny:0

    Rectangle { 
        width:50
        height:50
        id: userIcon
        x: topLeftRect.x; y: topLeftRect.y
        //source: "qt-logo.png"
    }
    MouseArea{
        anchors.fill:parent
        onClicked:{
            if( page.state == "" ){
                nx = mouse.x
                ny = mouse.y
                page.state = "move"
            }
            else{
                page.state = ""
            }
        }
    }

    states: [
        State {
            name: "move"
            PropertyChanges { target: userIcon; x: nx; y: ny }
        }
    ]
    transitions: [
        Transition {
            NumberAnimation { properties: "x,y"; easing.type: Easing.OutBounce; duration: 1000 }
        }
    ]
}
"""


s_key_study_action_m_old2 = """
import QtQuick 1.0
import "file:///D:/pro/net_study/net_bag/nb"

Rectangle {
    id:window
    x:250
    y:100
    color: "white" 
    property color select_color: "black"
    Cell{y:100; r1_color:"red" }
    Cell{y:150; r1_color:"yellow" }
}
"""

s_key_study_action_m_old = """
import QtQuick 1.0
Rectangle {
    x:150
    id: window
    width: 600; height: 460; color: "#232323"
    property int common_y: 0
    ListModel {
        id: easingTypes
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.InExpo"; type: Easing.InExpo; ballColor: "SkyBlue" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.OutExpo"; type: Easing.OutExpo; ballColor: "RoyalBlue" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.InOutExpo"; type: Easing.InOutExpo; ballColor: "MediumBlue" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.OutInExpo"; type: Easing.OutInExpo; ballColor: "MidnightBlue" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.InCirc"; type: Easing.InCirc; ballColor: "CornSilk" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.OutCirc"; type: Easing.OutCirc; ballColor: "Bisque" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.InOutCirc"; type: Easing.InOutCirc; ballColor: "RosyBrown" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.OutInCirc"; type: Easing.OutInCirc; ballColor: "SandyBrown" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.InElastic"; type: Easing.InElastic; ballColor: "DarkGoldenRod" }
        ListElement { ny:0; en:"test"; cn:""; name: "Easing.OutElastic"; type: Easing.OutElastic; ballColor: "Chocolate" }

    }
    Component {
        id: delegate
        Item {
            height: 56; width: window.width
            Text { 
                text: name; 
                anchors{right: parent.right}
                color: "White" 
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( mouse.y )
                    //window.common_y = mouse.y / 46 * 46
                    window.common_y = parent.y
                    console.log( window.common_y )
                }
            }
            Rectangle {
                id: rect; x: 30; color: "#454545"
                border.color: "White"; border.width: 2
                height: 46; width: 100; radius: 12
                //anchors.verticalCenter: parent.verticalCenter
                Text{
                    color: "green"
                    font.pixelSize: 32
                    text:en
                }
                MouseArea {
                    onClicked: {
                        console.log( window.common_y )
                        var tval = window.common_y - parent.parent.y
                        if( tval < 0 )  tval = 0
                        easingTypes.setProperty(index, "ny", tval )
                        console.log( ny )
                        var tpos = parseInt( ny / 46 )
                        console.log( tpos )
                        console.log( easingTypes.get(tpos).cn )
                        if( easingTypes.get(tpos).cn == "" ){
                            if (rect.state == '') {
                                rect.state = "right"; 
                                tpos = ny / 46
                                easingTypes.setProperty(tpos, "cn", en )
                            }
                            else{
                                rect.state = ''
                                tpos = ny / 46
                                easingTypes.setProperty(tpos, "cn", "" )
                            }
                        }
                    }
                    anchors.fill: parent
                    anchors.margins: -5 // Make MouseArea bigger than the rectangle, itself
                }
                states : State {
                    name: "right"
                    PropertyChanges { target: rect; x: window.width + 10; y: ny; color: ballColor }
                }
                transitions: Transition {
                    NumberAnimation { properties: "x,y"; easing.type: type; duration: 1000 }
                    ColorAnimation { properties: "color"; easing.type: type; duration: 1000 }
                }
            }
        }
    }
    Flickable {
        anchors.fill: parent
        contentHeight: layout.height+50
        Rectangle {
            id: titlePane
            color: "#444444"
            height: 35
            anchors { top: parent.top; left: parent.left; right: parent.right }
            //QuitButton {
                //id: quitButton
                //anchors.verticalCenter: parent.verticalCenter
                //anchors.right: parent.right
                //anchors.rightMargin: 10
            //}
        }
        Column {
            id: layout
            anchors { top: titlePane.bottom; topMargin: 10; left: parent.left; right: parent.right }
            Repeater { model: easingTypes; delegate: delegate }
        }
    }
}
"""

s_key_study_action_h = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    Text{
        id:text1
        x:300
        y:200
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text1"
    }
    Text{
        id:text2
        x:400
        y:400
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text2"
    }
    Text{
        id:text3
        x:400
        y:150
        color: "black"
        font.pixelSize: 32
        text:"s_key_study_action_o_text3"
    }
        Item{
            x:0
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-previous-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "prev page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_prev_page" )
                }
            }
        }
        Item{
            x:1024-48
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-next-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "next page" )
                    //bg.source= ""
                    cmd( "text_book", "s_key_study_action_o_next_page" )
                }
            }
        }
}
"""





s_dir_html_view_temp = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    property string path: "menu/primary_school/funs/encyclopedic/"
    //property string data_path: "data/百科知识"
    ListModel {
        id: appModel
        s_dir_html_view_temp_ListElement
        //ListElement { name: "乐园"; cmd: "menu/plays/main.qml"}
    }
    DirView{ dir: 's_dir_html_view_temp_dir'; board_x:430; board_y:130; board_width:400; board_height:320; listItem: appModel }
}

"""


s_html_view_temp = """
import QtQuick 1.0
import QtWebKit 1.0

Rectangle{
        width:1024
        height:768
        //color:"green"
        anchors.centerIn: parent
        WebBrowser{
            urlString: 's_dir_html_view_temp_dir'
        }
}
"""
s_run_flash_hint = """
import QtQuick 1.0
import QtWebKit 1.0
Rectangle{
        width:1024
        height:768
        color:"blue"
        anchors.centerIn: parent
}
"""
s_text_book_test = """
import QtQuick 1.0
import QtWebKit 1.0

Rectangle{
        width:1024
        height:768
        color:"red"
        //anchors.centerIn: parent
        Image{
            source: "file:///D:/pro/net_study/net_bag/tmp/bg.jpg"
            anchors.centerIn: parent
        }
        Rectangle{ x:100; y:100; width:150; height:150; opacity: 0.1; color:"blue" }
}
"""







s_text_book_main_base = """
import QtQuick 1.0
Rectangle{
    anchors.fill: parent
    color:"white"
    Image{
        source: "images/text_book_main.png"
        //SmallShockIcon{ x:450;y:300;width:200;height:50; cmd_type:"text_book"; cmd: "key_study" }
        //SmallShockIcon{ x:450;y:500;width:200;height:50; cmd_type:"text_book"; cmd: "study" }
        ShockIcon{ x:300;y:250;cmd_type:"text_book"; cmd: "key_study" }
        ShockIcon{ x:300;y:400;cmd_type:"text_book"; cmd: "study" }
    }
}
"""

s_text_book_base = """
import QtQuick 1.0
import QtWebKit 1.0

Rectangle{
        id: page
        property int mx : 0
        property int my : 0
        property int exercise_no : -1
        property int exercise_try_count : 0
        property string read_string : 's_text_book_read_string'
        property string explain_string : 's_text_book_explain_string'
        property string exercise_string : 's_text_book_exercise_string'
        function doSelect( cmd_type, cmd_str ){
            //console.log( "text book do Select" )
            if( cmd_type == "quit" ){
                page.exercise_no = -1
                cmd( "quit", "" )
            }
            else if( cmd_type == "stop_sound"){
                page.exercise_no = -1
                cmd( "stop_sound", "" )
            }
            else if( cmd_type == "explain"){
                cmd( "sound", explain_string )
            }
            else if( cmd_type == "read"){
                page.exercise_no = -1
                cmd( "sound", read_string )
            }
            else if( cmd_type == "exercise"){
                //cmd( "sound", read_string )
                info_win.y = -100
                var lines = page.exercise_string.split( '|' )
                var items = lines[0].split( '\t' )
                console.log( page.exercise_string )
                console.log( items[1] )
                console.log( 0 )
                cmd( "sound", items[1] )
                page.exercise_no = 0
            }
            else{
                if( cmd_type == "study" ){
                    page.exercise_no = -1
                    cmd( "sound", ":study" )
                }
                else{
                    if( exercise_no >= 0 ){
                    }
                    else{
                        page.exercise_no = -1
                        var lines = cmd_str.split('|')
                        var items = lines[0].split('\t')
                        //console.log( items.length )
                        if( items.length == 1 ){
                            info_en.text = ""
                            info_cn.text = ""
                            cmd( "sound", items[0] )
                        }
                        else if( items.length >= 4 ){
                            info_en.text = items[0]
                            info_cn.text = items[1]
                            var sound_str = items[2] + "," + items[3]
                            cmd( "switch_sound", sound_str )
                            //cmd( "sound", sound_str )
                        }
                    }
                }
            }
        }
        function doSelectPoint( x,y, mx, my, cmd_type, cmd_str ){
            //console.log( "text book do Select point" )
            // for debug value
            my += 16
            if( exercise_no >= 0 ){
                doSelectPoint_exercise( x,y,mx,my,cmd_type, cmd_str )
            }
            else{
                if( x + 400 > 1024 )    x = 1024 - 400
                if( y + 100 > 768 )    y = 768 - 100
                info_win.x = x
                info_win.y = y
                console.log( page.state )
                if( page.state == "move" )
                    page.state = ""
                else 
                    page.state = "move"
            }
        }
        function doSelectPoint_exercise( x,y, mx, my, cmd_type, cmd_str ){
            //console.log( "text book do Select point" )
            // for debug value
            my += 16
            if( exercise_no >= 0 ){
                var next_flag = 0
                var lines = page.exercise_string.split( '|' )
                var count = lines.length
                var items = lines[page.exercise_no].split( '\t' )
                console.log( items[0] )
                var rect = items[0].split( ',' )
                var l = parseInt( rect[0] ) * 1024 / 255
                var t = parseInt( rect[1] ) * 768 / 255
                var r = parseInt( rect[2] ) * 1024 / 255
                var b = parseInt( rect[3] ) * 768 / 255
                var str = " ( " + mx.toString() + " , " + my.toString() + " ) " + l.toString() + " , " + t.toString() + " , " + r.toString() + " , " + b.toString()
                console.log( str )
                if( l <= mx && mx <= r && t <= my && my <= b ){
                    // find it
                    console.log( "find it" )
                    cmd( "sound", ":right" )
                    next_flag = 1
                }
                else{
                    console.log( "can not find it" )
                    // error count
                    page.exercise_try_count ++
                    if( page.exercise_try_count <= 2 ){
                        cmd( "sound", ":wrong" )
                        cmd( "append_sound", items[1] )
                    }
                    if( page.exercise_try_count > 2 ){
                        next_flag = 1
                    }
                }
                if( next_flag == 1 ){
                    page.exercise_no ++
                    page.exercise_try_count = 0
                    if( page.exercise_no < count ){
                        items = lines[page.exercise_no].split( '\t' )
                        cmd( "append_sound", items[1] )
                        console.log( "add one" )
                    }
                    else{
                        page.exercise_no = -1
                        cmd( "append_sound", ":study" )
                        console.log( "end " )
                    }
                }
            }
            else{
            }
        }
        width:1192
        height:818
        color:"red"
        MouseArea{
            anchors.fill: parent
            hoverEnabled: true
            onClicked:{
                info_win.x = 0
                info_win.y = -100
                console.log( "bg click" )
                //console.log( mouse.x )
                //console.log( mouse.y )
                doSelectPoint_exercise( 0,0,mouse.x,mouse.y,"", "" )
            }
            onEntered: { page_command.state = "move" }
        }
        Image{
            id: bg
            x: -72
            y: -46
            source: "s_text_book_page_bg_file"
            //source: "file:///D:/pro/net_study/net_bag/tmp/bg.jpg"
            smooth: true 
            //cache: false
        }
        Item{
            id: info_win
            x:-100
            y:-100
            width:400
            height:100
            Rectangle{
                //x:100
                //y:100
                radius: 12
                border.color: "Black"; border.width: 2
                opacity: 0.6
                color:"yellow"

                anchors.fill: parent
            }
            Text{
                id: info_en
                x:10
                y:10
                color: "black"
                font.pixelSize: 18
                text:"Test text"
            }
            Text{
                id: info_cn
                x:10
                y:40
                color: "black"
                font.pixelSize: 20
                text:"Test text"
            }
        }
        /*
        states : [
            State { name: "move"; PropertyChanges { target: info_win; x: page.mx; y: page.my } }
        ]
        transitions: [
            Transition { NumberAnimation { properties: "x,y"; easing.type: Easing.InOutQuad; duration: 1000 } }
        ]
        */
        
        s_text_book_base_button_text

        // all action in it study, explain, exercise, read
        Image{
            id: page_command
            x: 0
            y:0
            source: "images/tb_page_command.png"
            MouseArea{
                anchors.fill: parent
                hoverEnabled: true
                onClicked: {
                }
                onEntered: { page_command.state = "" }
                //onExited: { page_command.state = "move" }
            }
            states : [
                State { name: "move"; PropertyChanges { target: page_command; x: -150 } }
            ]
            transitions: [
                Transition { NumberAnimation { properties: "x,y"; easing.type: Easing.InOutQuad; duration: 1000 } }
            ]
            SmallShockIcon{ x:20; y:55; cmd_type: "explain"; cmd : "" }
            SmallShockIcon{ x:20; y:100; cmd_type: "study"; cmd : "" }
            SmallShockIcon{ x:20; y:145; cmd_type: "read"; cmd : "" }
            SmallShockIcon{ x:20; y:195; cmd_type: "exercise"; cmd : "" }
            SmallShockIcon{ x:20; y:240; cmd_type: "quit"; cmd: "" }
        }
        Item{
            x:0
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-previous-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "prev page" )
                    bg.source= ""
                    cmd( "text_book_prev_page", "" )
                }
            }
        }
        Item{
            x:1024-48
            y:700
            width:48
            height:48
            Rectangle{
                width:48
                height:48
                //anchors.fill: parent
                opacity: 0.6
                color:"yellow"
                radius: 12
                border.color: "Black"; border.width: 2
            }
            Image{
                x:8
                y:8
                //anchors.fill: parent
                source: "images/go-next-view.png"
            }
            MouseArea{
                anchors.fill: parent
                onClicked:{
                    console.log( "next page" )
                    bg.source= ""
                    cmd( "text_book_next_page", "" )
                }
            }
        }
}
"""



s_qml_dict_string = """
import QtQuick 1.0
Rectangle {
    id:r
    width: 1024
    height: 768
    color: "white"





    ListModel {
        id: appModel
        s_qml_dict_word_list
        //ListElement { name: "乐"; }
    }
    DictView{ dir: 's_dir_html_view_temp_dir'; board_x:670; board_y:170; board_width:200; board_height:280; listItem: appModel }
    Text{
        id:word
        x: 80
        y:140
        width:100
        height:100
        text: ""
        color: "blue"
        font.pixelSize: 24
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "click me" )
                var val = dict_value.dict("ec","hello")
                word.text = val
            }
        }
    }
    Text{
        id:sound
        //x:250
        //y:140
        x:200
        y:550
        width:100
        height:100
        text: ""
        color: "blue"
        font.pixelSize: 24
    }
    /*
    Rectangle{
        x: 80
        y:207
        width:300
        height:300
    TextEdit{
        id:content
        anchors.bottom:parent.bottom
        y:0
        width:300
        height:300
        wrapMode: TextEdit.WordWrap
        text: ""
        color: "blue"
        font.pixelSize: 32
        //onCursorRectangleChanged: flickArea.ensureVisible(cursorRectangle)
        horizontalAlignment: alignment
    }
    }
    */
    


        Flickable {
            id: flick
            x: 80
            y:207
            width:280
            height:200

            //anchors.fill: parent
            contentWidth: content.paintedWidth
            contentHeight: content.paintedHeight
            interactive: true
            clip: true

            function ensureVisible(r) {
                if (contentX >= r.x)
                    contentX = r.x;
                else if (contentX+width <= r.x+r.width)
                    contentX = r.x+r.width-width;
                if (contentY >= r.y)
                    contentY = r.y;
                else if (contentY+height <= r.y+r.height)
                    contentY = r.y+r.height-height;
            }

            TextEdit {
                id: content
                width: flick.width
                height: flick.height
                focus: true
                wrapMode: TextEdit.Wrap
                //wrapMode: TextEdit.WordWrap
                text: ""
                color: "blue"
                font.pixelSize: 29
                readOnly: true

                onCursorRectangleChanged: flick.ensureVisible(cursorRectangle)

            }
        }



    
}
"""

s_qml_test_string = """
import QtQuick 1.0
Rectangle {
    width: 1024
    height: 768
    color: "white"
    property string path: "menu/primary_school/funs/encyclopedic/"
    //property string data_path: "data/百科知识"
    ListModel {
        id: appModel
        ListElement { name: "识"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
        ListElement { name: "乐"; }
    }
    DirView{ dir: 's_dir_html_view_temp_dir'; board_x:430; board_y:130; board_width:400; board_height:320; listItem: appModel }
    Rectangle{
        x:0
        y:0
        width:100
        height:100
        color:"green"
        //anchors.fill: parent
        Text{
            id:content
            text: "123456"
        }
        MouseArea{
            anchors.fill: parent
            onClicked:{
                console.log( "click me" )
                //var val = cmd( "dict", "" )
                //var val = "test"
                var val = dict_value.dict("ec","hello")
                console.log( val )
                content.text = val
            }
        }
    }
}
"""

"""
"""

























































































































































































































































































































































































































def sys_exit():
    try:
        shutil.rmtree( "tmp" )
    except:
        print "del error"
    sys.exit(0)




def _d( val ):
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
        print ("-"*10, f.f_lineno, f.f_code.co_name, val)
    return (f.f_code.co_name, f.f_lineno)



def zf_dir( zf ):
    ls = []
    for n in zf_namelist( zf ):
        iis = n.split( '/' )
        iis.pop()
        nn = "/".join( iis )
        try:
            ls.index( nn ) 
        except:
            ls.append( nn )
    for l in ls:
        print l

def zf_namelist( zf ):
    #return zf.getnames()
    return zf.namelist()

def zf_extractfile( zf, fn ):
    global g_key
    key = g_key
    #print fn
    #print len( fn )
    #print type(fn)
    if "%s"%type(fn) == "<type 'unicode'>":
        tfn = fn.encode( 'gbk' )
    else:
        tfn = fn.decode( 'gbk' ).encode( 'gbk' )
    #print tfn
    #print len( tfn )
    str = tfn[- len(key) :]
    tkey = ""
    #print "================="
    size = min( len(key), len(str) )
    #print size
    #print "================="
    #print tfn
    #print len(tfn)
    for i in range(size):
        val = ord( str[i] )
        if ord('A') <= val and val <= ord('Z'):
            val += ord('a') - ord('A')
        val = ord(key[i])^val
        if( val == 0 ):
            break
        tkey += "%c"%(val)
        #print key[i]
        #print str[i]
        #print ord(tkey[i])
    #print key
    #print str
    #print tkey
    #print "-----------------"
    buf = zf.read( tfn, tkey )
    #buf = zf.read( fn, g_key )
    #buf = zf.read( fn, "1111" )
    #buf = zf.read( fn )
    return buf

def zf_extractfile_for_tar( zf, fn ):
    print fn
    buf = zf.extract( fn )
    print buf
    #buf = zf.extractfile( fn ).read()
    return buf


def get_qml_file_data_by_qt( fn ):
    p = ":/" + g_path + fn
    #p = "qrc:" + g_path + fn
    ff = QFile( p )
    if( ff.open(QIODevice.ReadOnly ) == False ):
        print "open file %s error"%p
        return "error"
    data = ff.readAll()
    return data

def get_qml_file_string_by_qt( fn ):
    p = ":/" + g_path + fn
    #p = "qrc:" + g_path + fn
    ff = QFile( p )
    if( ff.open(QIODevice.ReadOnly | QIODevice.Text) == False ):
        print "open file %s error"%p
        return "error"
    f = QTextStream( ff )
    f.setCodec( "utf-8" )
    l = f.readAll()
    f.setCodec( "gbk" )
    return l

def get_qml_file_string_by_os( fn ):
    p = g_path + fn
    #print p
    f = codecs.open( p, "r", "utf-8" )
    l = f.read()
    f.close()
    return l

def get_qml_file_string( fn ):
    return get_qml_file_string_by_qt(fn)

#fileObj = codecs.open( "someFile", "r", "utf-8" )
#u = fileObj.read()

def get_dir_string( dir ):
    dir = dir.replace( "../", "" )
    try:
        dir_str = dir.decode( 'utf8' )
    except:
        dir_str = dir
    #print  "dir_str=%s"%dir_str
    return dir_str


def get_qml_test_string( str ):
    return s_qml_test_string.decode('utf8')

def file_name_tran( str ):
    str = str.replace( "'", "\\'" )
    return str

def os_listdir( dir ):
    if dir[:5] == "data/":
        # use package
        sub_dir = dir[5:]
        s = len( sub_dir )
        iis = dir.split( '/' )
        package = "data/" + iis[1] + ".pd"
        #print "package name: %s"%package
        zf = zipfile.ZipFile( package )
        f_dir = zf_namelist( zf )

        ls = []
        for d in f_dir:
            d = d.decode('gbk')
            if d[:s] == sub_dir :
                ss = s+1
                dd = d[ss:]
                if len(dd) > 0 :
                    iis = dd.split( '/' )
                    if len(iis) >= 1 and len(iis) <= 2:
                        try:
                            ls.index( iis[0] )
                        except:
                            # not include mp3
                            tis = iis[0].split('.')
                            if len(tis)==1 :
                                ls.append( file_name_tran(iis[0]) )
                            elif len(tis)>=2 :
                                if iis[0].endswith( 'mp3' ) or iis[0].endswith( 'gif' ) or iis[0].endswith('jpg') or iis[0].endswith('png')  :
                                    print "not show %s"%iis[0]
                                else:
                                    ls.append( file_name_tran(iis[0]) )
        return ls
    else:
        return os.listdir( dir )
    return ""

def get_qml_key_study_list_string( dir, ls ):
    global g_text_book_data
    str = s_dir_html_view_temp
    #_d( dir )

    # get the up dir
    rc = g_text_book_data.elementsByTagName(dir).at(0).parentNode().toElement()
    #_d( rc.tagName() )
    if rc.tagName() == 'text book':
        up_dir_str = "key_study %s"%dir.encode('utf8')
    else:
        up_dir_str = "key_study %s"%( rc.attribute('dir').encode('utf8') )
        do_cmd = "up_dir %s"%up_dir_str
        do_cmd = do_cmd.decode( 'utf8' )
        cmd( "set_quit", do_cmd )
    #_d( up_dir_str )

    str = str.replace( "s_dir_html_view_temp_dir", up_dir_str )
    items = str.split( "s_dir_html_view_temp_ListElement" )
    str = items[0].decode('utf8')
    rc = g_text_book_data.elementsByTagName(dir).at(0).toElement()
    rc = rc.nextSibling().toElement()
    tasks = rc.childNodes()
    #_d( tasks.count() )
    for i in range( tasks.count() ):
        task = tasks.at(i).toElement()
        ts = task.attribute( 'text' )
        action = task.attribute( 'action' )
        #tdir = task.attribute( 'dir' )
        trc = task.childNodes().at(1).toElement()
        tdir = trc.attribute( 'dir' )
        #_d( ts )
        #_d( tdir )
        if action == 'l':
            do_cmd = 'key_study %s %d %s'%(tdir,i,action)
        else:
            do_cmd = 'key_study %s %d %s'%( dir,i,action)

        tmp_str = "ListElement { name: '%s'; cmd_type: 'text_book'; cmd: '%s'}\n"%(ts, do_cmd )
        str += tmp_str
    str += items[1].decode('utf8')
    #print str
    return str

def get_qml_dir_string( dir ):
    dir_str = get_dir_string( dir )
    str = s_dir_html_view_temp
    str = str.replace( "s_dir_html_view_temp_dir", dir_str.encode('utf8') )
    items = str.split( "s_dir_html_view_temp_ListElement" )
    str = items[0].decode('utf8')
    #_d( str )
    #print "now path:%s"%( os.getcwd() )
    for filename in os_listdir( dir_str ):
        t_dir_str = "%s/%s"%(dir_str,filename)
        #t_dir_str = t_dir_str.encode( 'utf8' )
        #print t_dir_str
        tmp_str = "ListElement { name: '%s'; cmd_type: 'auto'; cmd: '%s'}\n"%(filename, t_dir_str )
        #print tmp_str
        str += tmp_str
    str += items[1].decode('utf8')
    #print str
    return str

def get_html_view_string( dir ):
    #print "get_html_view_string( str )"
    dir_str = get_dir_string( dir )
    str = s_html_view_temp

    items = os.getcwd().split( "\\" )
    now_path = "/".join( items ) + "/"
    #now_path = now_path.replace( "D:", "d" )

    #str = str.replace( "s_dir_html_view_temp_dir", "http://www.soso.com" )
    str = str.replace( "s_dir_html_view_temp_dir", "file:///" + now_path +dir_str.encode('utf8') )
    #str = str.replace( "s_dir_html_view_temp_dir", "../"+dir_str.encode('utf8') )
    str = str.decode('utf8')
    #nb_qrc.qCleanupResources()
    #print str
    return str




def create_rc_xml_item( doc, rc, l ):
    items = l.split( ' ' )
    #print items[0]
    if len(items[0]) > 0 and items[0][0] >= '0' and items[0][0] <= '9' :
        page_items = l.split( '\t' )
        page_no = int(page_items[0])
        e = rc.childNodes().at(page_no-1).toElement()
        e.setAttribute( 'no', page_items[0] )
        #if page_items[1] == 'text':
            #e.setAttribute( page_items[1], page_items[2] )
        #else:
            #e.setAttribute( page_items[1], page_items[2] )
        i = page_items[2].decode( 'gbk' )
        e.setAttribute( page_items[1], i )
    elif len( items ) > 1:
        rc.setAttribute( items[0], items[1].decode('gbk') )

def create_rc_xml( doc, rc, lines ):
    for l in lines:
        if len(l) <= 0 :
            continue
        if ord(l[-1]) == 0xd :
            l = l[:-1]
        create_rc_xml_item( doc, rc, l )
def create_rc_node_tree( path, zf, root, doc, rc_fn ):
    # create rc node 
    rc = doc.createElement( 'rc' )
    if type(path) != type(u'') :
        _d( type(path) )
        _d( path )
        path = path.decode('gbk')
    rc.setAttribute( 'dir', (path+rc_fn) )
    root.appendChild( doc.createElement( (path+rc_fn) ) )
    root.appendChild( rc )
    # deal task file
    task_fn = rc_fn.replace( ".rc", ".task" )
    #print "task file name : %s"%task_fn
    #lines = zf.read( path + task_fn ).split( "\n" )
    tfn = path + task_fn
    tfn = tfn.lower()
    lines = zf_extractfile( zf, tfn ).split( "\n" )
    for l in lines:
        items = l.split( '\t' )
        if( len( items ) > 1 ):
            if ord( items[1][-1] ) == 0xd :
                items[1] = items[1][:-1]
            items[1] = items[1].replace( "\\", "/" )
            e = doc.createElement( 'task' )
            e.setAttribute( 'action', items[0].decode('gbk') )
            e.setAttribute( 'target', items[1].decode('gbk') )
            #e.setAttribute( 'dir', path + task_fn )
            e.setAttribute( 'dir', path + rc_fn )
            rc.appendChild( e )
    # deal rc file
    #print "rc file name : %s"%rc_fn
    tfn = path + rc_fn
    tfn = tfn.lower()
    lines = zf_extractfile( zf, tfn ).split( "\n" )
    create_rc_xml( doc, rc, lines )
    # deal the page rc file
    task_count = rc.childNodes().count()
    #print ">>>>>>>>>>>>>>>>>>>>>>>"
    # calc path
    #print rc_fn
    items = rc_fn.split('/')
    items.pop()
    if( len( items ) > 0 ):
        path = path + '/'.join( items ) + '/'
    #print "path=%s"%path
    #print "---------------"
    for i in range( task_count ):
        rc_root = rc.childNodes().at(i).toElement()
        if rc_root.attribute( 'action' ) == 'l' :
            rc_fn = rc_root.attribute( 'target' )
            #print rc_fn
            create_rc_node_tree( path, zf, rc_root, doc, rc_fn )
        # here do other action xml data.
        if rc_root.attribute( 'action' ) == 'o' :
            # 课文朗读
            #print( u'课文朗读'.encode('gbk') )
            sfn = u"%s%s"%(path, u'课文朗读cks.txt' )
            #print sfn
            slines = zf_extractfile( zf, sfn ).split( "\n" )
            for l in slines:
                l = chop(l)
                l = l.decode( 'gbk' )
                iis = l.split( '\t' )
                if len( iis ) >= 4 :
                    item = doc.createElement( 'rc' )
                    rc_root.appendChild( item )
                    item.setAttribute( 'pos', iis[0] )
                    item.setAttribute( 'sound', "%s"%(iis[1]) )
                    #item.setAttribute( 'sound', "%smp3/%s.mp3"%(g_zf_path,iis[1]) )
                    item.setAttribute( 'mov', "%smov/%s_1.jpg"%(g_zf_path,iis[2]) )
                    item.setAttribute( 'text', iis[3] )
        if rc_root.attribute( 'action' ) == 'k' :
            # 翻译练习.txt
            #print( u'翻译练习'.encode('gbk') )
            sfn = u"%s%s"%(path, u'翻译练习.txt' )
            #print sfn
            slines = zf_extractfile( zf, sfn ).split( "\n" )
            for l in slines:
                l = chop(l)
                l = l.decode( 'gbk' )
                #print l
                iis = l.split( '\t' )
                if len( iis ) >= 3 :
                    item = doc.createElement( 'rc' )
                    rc_root.appendChild( item )
                    item.setAttribute( 'en', iis[0] )
                    item.setAttribute( 'cn', iis[1] )
                    item.setAttribute( 'sound', iis[2] )
        if rc_root.attribute( 'action' ) == 'b' :
            # 单词学习.txt
            #print( u'单词学习'.encode('gbk') )
            sfn = u"%s%s"%(path, u'单词学习cks.txt' )
            #print sfn
            slines = zf_extractfile( zf, sfn ).split( "\n" )
            for l in slines:
                l = chop(l)
                l = l.decode( 'gbk' )
                #print l
                iis = l.split( '\t' )
                if len( iis ) >= 3 :
                    item = doc.createElement( 'rc' )
                    rc_root.appendChild( item )
                    item.setAttribute( 'sound', iis[0] )
                    #item.setAttribute( 'mov', iis[1] )
                    item.setAttribute( 'mov', "%smov/%s_1.jpg"%(g_zf_path,iis[1]) )
                    item.setAttribute( 'cn', iis[2] )
        if rc_root.attribute( 'action' ) == 'm' :
            # 单词连连看.txt
            #print( u'单词连连看'.encode('gbk') )
            sfn = u"%s%s"%( path, u'单词连连看.txt' )
            #print sfn
            slines = zf_extractfile( zf, sfn ).split( "\n" )
            for l in slines:
                l = chop(l)
                l = l.decode( 'gbk' )
                #print l
                iis = l.split( '\t' )
                if len( iis ) >= 3 :
                    item = doc.createElement( 'rc' )
                    rc_root.appendChild( item )
                    item.setAttribute( 'sound', iis[0] )
                    item.setAttribute( 'en', iis[1] )
                    item.setAttribute( 'cn', iis[2] )
        if rc_root.attribute( 'action' ) == 'h' :
            # 听力填空.txt
            #print( u'听力填空'.encode('gbk') )
            sfn = u"%s%s"%( path, u'听力填空.txt' )
            #print sfn
            slines = zf_extractfile( zf, sfn ).split( "\n" )
            for l in slines:
                l = chop(l)
                l = l.decode( 'gbk' )
                #print l
                iis = l.split( '\t' )
                if len( iis ) >= 3 :
                    item = doc.createElement( 'rc' )
                    rc_root.appendChild( item )
                    item.setAttribute( 'sound', iis[0] )
                    item.setAttribute( 'answer', iis[2] )
                    item.setAttribute( 'title', iis[3] )
    #print "VVVVVVVVVVVVVVVVVVVVV"


def chop( str ):
    if len( str ) <= 0 :
        return str
    while ord( str[-1] ) == 0xd or ord( str[-1] ) == 0xa :
        str = str[:-1]
        if len( str ) <= 0 :
            break;
    return str

def create_book_command_file_xml( zf, doc, page, lines ):
    for l in lines.split('\n'):
        if len( l ) <= 0:
            continue
        if ord(l[-1]) == 0xd:
            l = l[:-1]
        items = l.split( '\t' )
        if( len( items ) > 1 ):
            page.setAttribute( items[0].decode('gbk'), items[1].decode('gbk') )
    path = page.attribute( 'dir' )
    # deal the study exercise explain read dictation
    # deal the study 
    study = doc.createElement( 'study' )
    page.appendChild( study )
    fn = page.attribute( 'study' )
    lines = zf_extractfile( zf, path + fn ).split( '\n' )
    for l in lines:
        l = chop( l )
        iis = l.split( '\t' )
        if( len( iis ) >= 3 ):
            e = doc.createElement( 'items' )
            study.appendChild( e )
            e.setAttribute( 'rect', iis[0].decode('gbk') )
            e.setAttribute( 'type', iis[1].decode('gbk') )
            e.setAttribute( 'value', iis[2].decode('gbk') )
    # deal the exercise 
    exercise = doc.createElement( 'exercise' )
    page.appendChild( exercise )
    fn = page.attribute( 'exercise' )
    lines = zf_extractfile( zf, path + fn ).split( '\n' )
    for l in lines:
        l = chop( l )
        iis = l.split( '\t' )
        if( len( iis ) >= 3 and len(iis[0]) > 1):
            e = doc.createElement( 'items' )
            exercise.appendChild( e )
            e.setAttribute( 'rect', iis[0].decode('gbk') )
            e.setAttribute( 'type', iis[1].decode('gbk') )
            e.setAttribute( 'value', iis[2].decode('gbk') )
    # deal the explain 
    explain = doc.createElement( 'explain' )
    page.appendChild( explain )
    fn = page.attribute( 'explain' )
    lines = zf_extractfile( zf, path + fn ).split( '\n' )
    if( len( lines ) >= 1 ):
        lines[1] = chop( lines[1] )
        iis = lines[1].split('\t')
        if( len( iis ) >= 2 and len(iis[0]) > 1):
            e = doc.createElement( 'items' )
            explain.appendChild( e )
            e.setAttribute( 'type', iis[0].decode('gbk') )
            e.setAttribute( 'value', iis[1].decode('gbk') )
    # deal the read 
    read = doc.createElement( 'read' )
    page.appendChild( read )
    fn = page.attribute( 'read' )
    lines = zf_extractfile( zf, path + fn ).split( '\n' )
    if( len( lines ) >= 1 ):
        lines[1] = chop( lines[1] )
        iis = lines[1].split('\t')
        if( len( iis ) >= 2 and len(iis[0]) > 1):
            e = doc.createElement( 'items' )
            read.appendChild( e )
            e.setAttribute( 'type', iis[0].decode('gbk') )
            e.setAttribute( 'value', iis[1].decode('gbk') )
    # read the data file
    data_list = doc.createElement( 'data_list' )
    page.appendChild( data_list )
    fn = page.attribute( 'data_list' )
    lines = zf_extractfile( zf, path + fn ).split( '\n' )
    if len( lines ) >= 2 :
        lines = lines[2:]
        for l in lines:
            l = chop( l )
            iis = l.split('\t')
            if len(iis) >= 7 :
                e = doc.createElement( 'items' )
                try:
                    e.setAttribute( 'en', iis[0].decode('gbk') )
                    e.setAttribute( 'cn', iis[1].decode('gbk') )
                    e.setAttribute( 'en_mp3', iis[2].decode('gbk') )
                    e.setAttribute( 'cn_mp3', iis[3].decode('gbk') )
                    e.setAttribute( 'pic', iis[4].decode('gbk') )
                    e.setAttribute( 'delay', iis[5].decode('gbk') )
                    e.setAttribute( 'flag', iis[6].decode('gbk') )
                    data_list.appendChild( e )
                except:
                    print "item error"
                    e.setAttribute( 'en', "" )
                    e.setAttribute( 'cn', "" )
                    e.setAttribute( 'en_mp3', "" )
                    e.setAttribute( 'cn_mp3', "" )
                    e.setAttribute( 'pic', "" )
                    e.setAttribute( 'delay', "" )
                    e.setAttribute( 'flag', "" )
                    data_list.appendChild( e )


def create_book_xml( zf, doc, book, lines ):
    page_flag = 0
    for l in lines:
        if len( l ) <= 0:
            continue
        if ord(l[-1]) == 0xd:
            l = l[:-1]
        items = l.split( '\t' )
        if( len( items ) > 1 ):
            book.setAttribute( items[0], items[1].decode('gbk') )
        elif( items[0] == "page_setup_start" ):
            page_flag = 1
        elif( items[0] == "page_setup_end" ):
            page_flag = 0
        elif( page_flag == 1 ):
            e = doc.createElement( 'page' )
            e.setAttribute( 'command_file', items[0].decode('gbk') )
            e.setAttribute( 'dir', book.attribute('dir') )
            book.appendChild( e )
            # read the command file
            #print items[0]
            lines = zf_extractfile( zf, book.attribute('dir') + items[0] )
            create_book_command_file_xml( zf, doc, e, lines )

def create_book_node_tree( path, zf, root, doc, book_fn ):
    # create book node 
    book = doc.createElement( 'book' )
    book.setAttribute( 'dir', path )
    root.appendChild( book )
    # read the page jpg rect info.
    lines = zf_extractfile( zf, path + "cks/rect.txt" ).split( "\n" )
    book.setAttribute( "cks_rect_1", chop(lines[0]) )
    book.setAttribute( "cks_rect_2", chop(lines[1]) )
    book.setAttribute( "cks_rect_3", chop(lines[2]) )

    # deal book node
    #print "book file name : %s"%book_fn
    lines = zf_extractfile( zf, path + book_fn ).split( "\n" )
    create_book_xml( zf, doc, book, lines )

def create_xml_file_from_zip_file( zf ):
    global g_zf_path
    g_zf_path = u""
    list = zf_namelist(zf)
    g_zf_path = list[0].split('/')[0] + "/"
    #print list[0]
    #print "-"*30
    #print list
    doc = QDomDocument("text book xml")
    root = doc.createElement( 'text book' )
    #root.setAttribute( 'name',zf.filename[:-4] )
    root.setAttribute( 'version', '1.0' )
    doc.appendChild( root )
    try:
        #file_data = zf.read('autorun.bas') 
        file_data = zf_extractfile(zf, 'autorun.bas')
    except:
        #g_zf_path = list[0]
        g_zf_path = list[0].split('/')[0] + "/"

    if 1:
    #try:
        file_data = zf_extractfile( zf, g_zf_path + 'autorun.bas')
        m = re.search( ur'"(\S+)"', file_data )
        if not m:
            print "file error"
            return ""

        # rc
        rc_fn = m.group().replace( "\"", "" )
        rc_fn = rc_fn.decode( 'gbk' )
        _d( type(rc_fn) )
        create_rc_node_tree( g_zf_path, zf, root, doc, rc_fn )
    #except:
        #_d( "not create rc data" )

    # reader
    book_fn = 'reader/book.txt'
    create_book_node_tree( g_zf_path, zf, root, doc, book_fn )

    #print doc.toString()
    return doc


def get_text_book_data_from_zip_file_debug():
    global g_text_book_data
    str = "%s"%(type(g_text_book_data))
    #print str
    #print "<type 'PySide.QtXml.QDomDocument'>"
    if str == "<type 'PySide.QtXml.QDomDocument'>" :
        str = g_text_book_data.toString()
        #print str
        f = open( "tmp.xml", 'w' )
        f.write( str.encode('utf8') )
        f.close()

def open_text_book_data_from_zip_file( str ):
    global g_text_book_data
    global g_zf
    try:
        del g_text_book_data
    except:
        print "delete global g_text_book_data error"
    del g_zf

    #try:
    if True:
        g_zf = zipfile.ZipFile( str )
        #zf_extractfile( g_zf, "xbzyy8s308/data/1/单词学习.txt".decode('utf8') )
        #g_zf = tarfile.open( str, "r")
        #g_zf = tarfile.open( str, "r:bz2")
        #print g_zf.getnames()
        #print g_zf
        #print "-" * 20
        g_text_book_data = create_xml_file_from_zip_file( g_zf )
    #except:
        #print "file error"
        #return ""
    get_text_book_data_from_zip_file_debug()
    #return ""






def check_quote( tv ):
    tv = tv.replace( "\"", "\\\"" )
    return tv


def get_text_book_study_page_read_data( page_no ):
    global g_text_book_data
    mp3_str = ""
    book = g_text_book_data.elementsByTagName('book').at(0).toElement()
    page = book.childNodes().at(page_no-1).toElement()
    data_list_cns = page.firstChildElement( 'data_list' ).childNodes()
    study = page.firstChildElement( 'read' )
    cns = study.childNodes()
    for i in range( cns.count() ):
        type = cns.at(i).toElement().attribute( 'type' )
        str = cns.at(i).toElement().attribute( 'value' )
        if( type == "mp3" ):
            mp3_str += str + ","
        else:
            iis = str.split(',')
            for ii in iis:
                #print ii
                item = data_list_cns.at( int(ii)-1 ).toElement()
                mp3_str += item.attribute( 'en_mp3' ) + ','
    if len( mp3_str ) > 1 :
        mp3_str = mp3_str[:-1]
    #print "read mp3_str = %s"%mp3_str
    return mp3_str

def get_text_book_study_page_exercise_data( page_no ):
    global g_text_book_data
    mp3_str = ""
    book = g_text_book_data.elementsByTagName('book').at(0).toElement()
    page = book.childNodes().at(page_no-1).toElement()
    study = page.firstChildElement( 'exercise' )
    cns = study.childNodes()
    for i in range( cns.count() ):
        mp3_str += cns.at(i).toElement().attribute( 'rect' ) + '\t'
        mp3_str += cns.at(i).toElement().attribute( 'value' ) + '|'
    if len( mp3_str ) > 1 :
        mp3_str = mp3_str[:-1]
    #print "exercise mp3_str = %s"%mp3_str
    return mp3_str

def get_text_book_study_page_explain_data( page_no ):
    global g_text_book_data
    mp3_str = ""
    book = g_text_book_data.elementsByTagName('book').at(0).toElement()
    page = book.childNodes().at(page_no-1).toElement()
    study = page.firstChildElement( 'explain' )
    cns = study.childNodes()
    for i in range( cns.count() ):
        mp3_str += cns.at(i).toElement().attribute( 'value' ) + ','
    if len( mp3_str ) > 1 :
        mp3_str = mp3_str[:-1]
    #print "explain mp3_str = %s"%mp3_str
    return mp3_str

def get_text_book_study_page_study_data( page_no ):
    global g_text_book_data
    global g_rand_value
    ls = []
    book = g_text_book_data.elementsByTagName('book').at(0).toElement()
    page = book.childNodes().at(page_no-1).toElement()
    data_list_cns = page.firstChildElement( 'data_list' ).childNodes()
    study = page.firstChildElement( 'study' )
    cns = study.childNodes()
    for i in range( cns.count() ):
        value = ""
        str = cns.at(i).toElement().attribute( 'rect' )
        rs = str.split(',')
        if( len( rs ) > 4 ):
            # ignore not rectangle
            continue
        l = rs[0]; t = rs[1]; r = rs[2]; b = rs[3]
        type = cns.at(i).toElement().attribute( 'type' )
        value = cns.at(i).toElement().attribute( 'value' )
        if type == "pos":
            #print value
            tv = ""
            for v in value.split(','):
                item = data_list_cns.at( int(v)-1 ).toElement()
                str = item.attribute( 'en' ) + '\t'
                str += item.attribute( 'cn' ) + '\t'
                str += item.attribute( 'en_mp3' ) + '\t'
                str += item.attribute( 'cn_mp3' ) 
                tv += str + "|"
            if( len( tv ) > 1 ):
                tv = tv[:-1]
            tv = check_quote( tv );
            value = "%s"%tv
            #print value
        elif type == "mp3":
            value = value
        x = 1.0*int(l) * (1192) / 255  - 72
        y = 1.0*int(t) * (818) / 255  - 46
        w = 1.0*(int(r)-int(l)) * (1192) / 255
        h = 1.0*(int(b)-int(t)) * (818) / 255
        #print value
        ls.append( [ x, y, w, h, value ] )


    # copy the file
    fn = g_zf_path + "cks/pic/r%d.jpg"%page_no
    #print "ready %s file from package"%fn
    buf = zf_extractfile( g_zf, fn )
    try:
        os.remove( "tmp/tmp%d.jpg"%g_rand_value )
    except:
        print "del error"
    g_rand_value = random.randint( 10000000, 99999999 )
    f = open( "tmp/tmp%d.jpg"%g_rand_value, "wb" )
    #print "========================"
    #print f
    #print "========================"
    f.write( buf )
    f.close()

    return ls

def get_mp3_file( sn ):
    global g_mp3_play
    global g_mp3_play_list
    if( len( sn ) <= 0 ):
        return ""
    if( sn[0] == ':' ):
        # read the file from qt
        sn = "mp3/%s.mp3"% sn[1:]
        #print "read %s from qt" % sn
        buf = get_qml_file_data_by_qt( sn )
        #print len( buf )
    else:
        fn = g_zf_path + "mp3/%s.mp3"%sn
        buf = zf_extractfile( g_zf, fn )
    if( g_mp3_play != "" ):
        g_mp3_play_close()
    f = open( "tmp/tmp.mp3", "wb" )
    f.write( buf )
    f.close()
    sn = "tmp/tmp.mp3"
    #sn = "file:///%s/tmp/tmp.mp3"% os.getcwd()
    sn = sn.replace( "\\", "/" )
    return sn


def get_text_book_string_test( str ):
    get_text_book_page_data( 2 )
    return s_text_book_test 

def get_text_book_string_main( str ):
    global g_text_book_now_page
    global g_rand_value
    text_book_base = s_text_book_main_base
    str = text_book_base
    return str

def get_text_book_string_key_study_o( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    item = task.childNodes().at( item_pos ).toElement()
    sound = item.attribute( 'sound' ) 
    pos = item.attribute( 'pos' ) 
    mov = item.attribute( 'mov' )
    text = item.attribute( 'text' )

    qml_str = s_key_study_action_o 
    qml_str = qml_str.replace( "s_key_study_action_o_dir", dir )
    pos = int(pos)
    qml_str = qml_str.replace( "s_key_study_action_o_text%d"%pos, text )
    qml_str = qml_str.replace( "s_key_study_action_o_text1", "" )
    qml_str = qml_str.replace( "s_key_study_action_o_text2", "" )
    qml_str = qml_str.replace( "s_key_study_action_o_text3", "" )

    if item_pos > 1:
        prev_page = item_pos - 1
    else:
        prev_page = 0
    if item_pos < item_count-1:
        next_page = item_pos + 1
    else:
        next_page = item_count - 1
    qml_str = qml_str.replace( "s_key_study_action_o_prev_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], prev_page ) )
    qml_str = qml_str.replace( "s_key_study_action_o_next_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], next_page ) )

    fn = mov
    buf = zf_extractfile( g_zf, fn )
    try:
        os.remove( "tmp/tmp%d.jpg"%g_rand_value )
    except:
        print "del error"
    g_rand_value = random.randint( 10000000, 99999999 )
    f = open( "tmp/tmp%d.jpg"%g_rand_value, "wb" )
    #print "========================"
    #print f
    #print "========================"
    f.write( buf )
    f.close()
    bg = "file:///%s/tmp/tmp%d.jpg"%(os.getcwd(), g_rand_value)
    bg = bg.replace( "\\", "/" )
    _d( bg )
    qml_str = qml_str.replace( "s_text_book_page_bg_file", bg )
    cmd( "sound", sound )

    cmd( "set_quit", "up_dir key_study %s"%dir )
    #print qml_str
    return qml_str

def get_text_book_string_key_study_k( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    item = task.childNodes().at( item_pos ).toElement()
    sound = item.attribute( 'sound' ) 
    en = item.attribute( 'en' ) 
    cn = item.attribute( 'cn' )

    qml_str = s_key_study_action_k
    qml_str = qml_str.replace( "s_key_study_action_o_dir", dir )
    #pos = int(pos)
    #qml_str = qml_str.replace( "s_key_study_action_o_text%d"%pos, text )
    qml_str = qml_str.replace( "s_key_study_action_o_text1", en )
    qml_str = qml_str.replace( "s_key_study_action_o_text2", cn )
    qml_str = qml_str.replace( "s_key_study_action_o_text3", "" )

    if item_pos > 1:
        prev_page = item_pos - 1
    else:
        prev_page = 0
    if item_pos < item_count-1:
        next_page = item_pos + 1
    else:
        next_page = item_count - 1
    qml_str = qml_str.replace( "s_key_study_action_o_prev_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], prev_page ) )
    qml_str = qml_str.replace( "s_key_study_action_o_next_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], next_page ) )

    cmd( "sound", sound )

    cmd( "set_quit", "up_dir key_study %s"%dir )
    #print qml_str
    return qml_str
def get_text_book_string_key_study_b( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    item = task.childNodes().at( item_pos ).toElement()
    sound = item.attribute( 'sound' ) 
    mov = item.attribute( 'mov' )
    cn = item.attribute( 'cn' )
    en = sound

    qml_str = s_key_study_action_b 
    qml_str = qml_str.replace( "s_key_study_action_o_dir", dir )
    qml_str = qml_str.replace( "s_key_study_action_o_text1", en )
    qml_str = qml_str.replace( "s_key_study_action_o_text2", cn )
    qml_str = qml_str.replace( "s_key_study_action_o_text3", "" )

    if item_pos > 1:
        prev_page = item_pos - 1
    else:
        prev_page = 0
    if item_pos < item_count-1:
        next_page = item_pos + 1
    else:
        next_page = item_count - 1
    qml_str = qml_str.replace( "s_key_study_action_o_prev_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], prev_page ) )
    qml_str = qml_str.replace( "s_key_study_action_o_next_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], next_page ) )

    fn = mov
    buf = zf_extractfile( g_zf, fn )
    try:
        os.remove( "tmp/tmp%d.jpg"%g_rand_value )
    except:
        print "del error"
    g_rand_value = random.randint( 10000000, 99999999 )
    f = open( "tmp/tmp%d.jpg"%g_rand_value, "wb" )
    #print "========================"
    #print f
    #print "========================"
    f.write( buf )
    f.close()
    bg = "file:///%s/tmp/tmp%d.jpg"%(os.getcwd(), g_rand_value)
    bg = bg.replace( "\\", "/" )
    _d( bg )
    qml_str = qml_str.replace( "s_text_book_page_bg_file", bg )
    cmd( "sound", sound )

    cmd( "set_quit", "up_dir key_study %s"%dir )
    #print qml_str
    return qml_str

def get_text_book_string_key_study_m( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    qml_str = s_key_study_action_m
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    en_cn_list = []
    for i in range( item_count ):
        item = task.childNodes().at( i ).toElement()
        sound = item.attribute( 'sound' ) 
        cn = item.attribute( 'cn' )
        en = item.attribute( 'en' )
        en_cn_list.append( [en,cn] )
    #Cell{color:"black";x:300;y:200; cn:"q"}
    #Cell{color:"red";x:100;y:100}
    cell_color = ['gainsboro', 'goldenrod', 'greenyellow', 'khaki', 'lightblue', 'lightseagreen', 'lightsteelblue', 'lime', 'magenta', 'mediumorchid', 'olivedrab', 'orchid', 'papayawhip', 'skyblue', 'springgreen', 'tomato', 'violet', 'yellowgreen']
    y = 100
    for c in en_cn_list:
        tstr = "Cell{color:'black';x:500;y:%d; en:'%s'; cn:'%s' }\n"%( y, file_name_tran(c[0]), c[1] )
        qml_str += tstr
        y += 50
    y = 100
    for i in range( 4 ):
        pos = random.randint( 0, len(en_cn_list)-1 )
        c = en_cn_list[ pos ]
        del en_cn_list[ pos ]
        en_cn_list.append( c )
    for i in range( len(en_cn_list) ):
        #pos = random.randint( 0, len(en_cn_list)-1 )
        pos = i
        tstr = "Cell{color:'%s';x:100;y:%d; en:'%s';  }\n"%( cell_color[i], y,  file_name_tran( en_cn_list[pos][0] ) )
        qml_str += tstr
        y += 50
    qml_str += "\n}\n"
    #print qml_str
    return qml_str

def get_text_book_string_key_study_h( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    item = task.childNodes().at( item_pos ).toElement()
    sound = item.attribute( 'sound' ) 
    title = item.attribute( 'title' ) 
    answer = item.attribute( 'answer' )

    qml_str = s_key_study_action_h
    qml_str = qml_str.replace( "s_key_study_action_o_dir", dir )
    #pos = int(pos)
    #qml_str = qml_str.replace( "s_key_study_action_o_text%d"%pos, text )
    qml_str = qml_str.replace( "s_key_study_action_o_text1", title )
    qml_str = qml_str.replace( "s_key_study_action_o_text2", answer )
    qml_str = qml_str.replace( "s_key_study_action_o_text3", "" )

    if item_pos > 1:
        prev_page = item_pos - 1
    else:
        prev_page = 0
    if item_pos < item_count-1:
        next_page = item_pos + 1
    else:
        next_page = item_count - 1
    qml_str = qml_str.replace( "s_key_study_action_o_prev_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], prev_page ) )
    qml_str = qml_str.replace( "s_key_study_action_o_next_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], next_page ) )

    cmd( "sound", sound )

    cmd( "set_quit", "up_dir key_study %s"%dir )
    #print qml_str
    return qml_str
def get_text_book_string_key_study_b( str ):
    global g_zf
    global g_rand_value
    global g_text_book_now_page
    item_pos = 0
    cmds = str.split(' ')
    if len( cmds ) >= 5:
        item_pos = int( cmds[4] )
    #_d( cmds[1] )
    #_d( cmds[2] )
    #_d( cmds[3] )
    rc = g_text_book_data.elementsByTagName( cmds[1] ).at(0).toElement()
    rc = rc.nextSibling().toElement()
    task = rc.childNodes().at( int(cmds[2]) ).toElement()
    dir = task.attribute( 'dir' )
    item_count = task.childNodes().count()
    _d( item_count )
    item = task.childNodes().at( item_pos ).toElement()
    sound = item.attribute( 'sound' ) 
    mov = item.attribute( 'mov' )
    cn = item.attribute( 'cn' )
    en = sound

    qml_str = s_key_study_action_b 
    qml_str = qml_str.replace( "s_key_study_action_o_dir", dir )
    qml_str = qml_str.replace( "s_key_study_action_o_text1", en )
    qml_str = qml_str.replace( "s_key_study_action_o_text2", cn )
    qml_str = qml_str.replace( "s_key_study_action_o_text3", "" )

    if item_pos > 1:
        prev_page = item_pos - 1
    else:
        prev_page = 0
    if item_pos < item_count-1:
        next_page = item_pos + 1
    else:
        next_page = item_count - 1
    qml_str = qml_str.replace( "s_key_study_action_o_prev_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], prev_page ) )
    qml_str = qml_str.replace( "s_key_study_action_o_next_page", 'key_study %s %s %s %d'%( cmds[1],cmds[2],cmds[3], next_page ) )

    fn = mov
    buf = zf_extractfile( g_zf, fn )
    try:
        os.remove( "tmp/tmp%d.jpg"%g_rand_value )
    except:
        print "del error"
    g_rand_value = random.randint( 10000000, 99999999 )
    f = open( "tmp/tmp%d.jpg"%g_rand_value, "wb" )
    #print "========================"
    #print f
    #print "========================"
    f.write( buf )
    f.close()
    bg = "file:///%s/tmp/tmp%d.jpg"%(os.getcwd(), g_rand_value)
    bg = bg.replace( "\\", "/" )
    _d( bg )
    qml_str = qml_str.replace( "s_text_book_page_bg_file", bg )
    cmd( "sound", sound )

    cmd( "set_quit", "up_dir key_study %s"%dir )
    #print qml_str
    return qml_str

def get_text_book_string_key_study( str ):
    global g_text_book_now_page
    global g_rand_value
    ls = []
    rc = g_text_book_data.elementsByTagName('rc').at(0).toElement()
    cmds = str.split( ' ' )
    up_dir = rc.attribute( 'dir' )
    #_d( up_dir )
    if len(cmds) <= 1 :
        dir = up_dir
    else:
        dir = cmds[1]
        rc = g_text_book_data.elementsByTagName(dir).at(0).toElement()
        rc = rc.nextSibling().toElement()
    #tasks = book.childNodes().at(page_no-1).toElement()
    #_d( rc.attribute( 'dir' ) )
    tasks = rc.childNodes()
    for i in range( tasks.count() ):
        task = rc.childNodes().at(i).toElement()
        no = task.attribute( 'no' )
        #_d( no )
        ls.append( no )

    str = get_qml_key_study_list_string(dir, ls)
    return str

def get_text_book_string_study( str ):
    global g_text_book_now_page
    global g_rand_value
    text_book_base = s_text_book_base
    text_book_base = text_book_base.replace( "s_text_book_read_string", get_text_book_study_page_read_data( g_text_book_now_page ) )
    text_book_base = text_book_base.replace( "s_text_book_explain_string", get_text_book_study_page_explain_data( g_text_book_now_page ) )
    text_book_base = text_book_base.replace( "s_text_book_exercise_string", get_text_book_study_page_exercise_data( g_text_book_now_page ) )
    ls = get_text_book_study_page_study_data( g_text_book_now_page )
    #bg = "file:///%s/tmp/bg_%d.jpg"%(os.getcwd(),g_text_book_now_page)
    bg = "file:///%s/tmp/tmp%d.jpg"%(os.getcwd(), g_rand_value)
    bg = bg.replace( "\\", "/" )
    text_book_base = text_book_base.replace( "s_text_book_page_bg_file", bg )
    #print "scale x=%f y=%f"%(xscale,yscale)

    #code = """ShockRect{ x:0;y:0;width:100;height:50; cmd: "" }
    #"""
    code = ""
    item = """ShockRect{ x:%d;y:%d;width:%d;height:%d; cmd: "%s" }
    """
    for l in ls:
        #code += item%( xscale*l[0],yscale*l[1],xscale*l[2],yscale*l[3],l[4] )
        code += item%( l[0],l[1],l[2],l[3],l[4] )
    #print code
    str = text_book_base.replace( "s_text_book_base_button_text", code )
    #print str
    return str 

def get_text_book_string( str ):
    cmds = str.split( ' ' )
    if str == "test" :
        return get_text_book_string_test( str )
    if str == "study":
        g_mp3_play_list.append( ":study" )
        g_mp3_play_close()
        g_mp3_play_start()
        return get_text_book_string_study( str )
    if str == "main":
        return get_text_book_string_main( str )
    if cmds[0] == "key_study":
        _d( str )
        if len(cmds) >= 4 :
            _d( cmds[3] )
            if cmds[3] == 'l':
                return get_text_book_string_key_study( str )
            elif cmds[3] == 'o':
                return get_text_book_string_key_study_o( str )
            elif cmds[3] == 'k':
                return get_text_book_string_key_study_k( str )
            elif cmds[3] == 'b':
                return get_text_book_string_key_study_b( str )
            elif cmds[3] == 'm':
                return get_text_book_string_key_study_m( str )
            elif cmds[3] == 'h':
                return get_text_book_string_key_study_h( str )
        else:
            return get_text_book_string_key_study( str )
    return ""


def get_g_dict_data( str ):
    global g_dict
    fn = 'data/词典大全.pd'.decode('utf8')
    zf = zipfile.ZipFile( fn )
    fn = "%s/%s.jpg"%( '词典大全', str)

    fn = fn.decode('utf8').encode('gbk')
    buf = zf_extractfile( zf, fn )
    g_dict = pickle.loads( buf )

def get_qml_dict_string( str ):
    global g_dict
    str = str.encode('utf8')
    get_g_dict_data( str )

    qml_str = s_qml_dict_string
    item = """ListElement{name:"%s"}\n"""
    tstr = ""
    key_list = g_dict.keys()
    key_list.sort()
    for k in key_list:
        tstr += item % k.encode('utf8')
    qml_str = qml_str.replace( "s_qml_dict_word_list", tstr )
    return qml_str.decode('utf8')

def package_file_deal( str ):
    try:
        str.index('.')
    except:
        return str
    c = len( str.split('/') )
    #print c
    if str[:5] == 'data/' and c >= 3:
        # this file point into package
        iis = str.split( '/' )
        package = "data/" + iis[1] + ".pd"
        #print "="*50
        #print str
        #print "package name: %s"%package
        zf = zipfile.ZipFile( package )
        fn = str[5:]
        #print fn
        #print len( fn )
        #fn = fn.encode( 'ascii', 'replace' )
        #fn = fn.encode( 'gbk' )
        #print len( fn )
        buf = zf_extractfile( zf, fn.encode('gbk') )
        fn = "tmp/" + iis.pop()
        #print "write file : %s"%fn
        f = open( fn, "wb" )
        f.write( buf )
        f.close()
        return fn
    return str

def get_qml( type_str, str ):
    global g_qml_lastest_string_list
    global g_qml_str_lastest_type 
    global g_text_book_now_page
    global g_text_book_data
    global g_quit_command
    #print "type_str=%s,str=%s."%(type_str,str)

    g_mp3_play_list.clear()
    g_mp3_play_close()
    #g_mp3_play_list.append( ":info" )
    g_mp3_play_list.append( ":ti" )
    g_mp3_play_start()
    #time.sleep( 2 )

    if( type_str == "auto" ):
        str = package_file_deal( str )
        items = str.split(".")

        if( len(items) < 2):
            type_str = "dir"
        elif str.endswith("swf") :
            system_cmd = "flash.exe \"%s%s\""%( "", str )
            os.system( system_cmd.encode('gbk') )
            type_str = "up_dir"
        elif str.endswith( "htm" ):
            type_str = "html_view"
        elif str.endswith( "html" ):
            type_str = "html_view"
        elif str.endswith( "TXT" ):
            type_str = "html_view"
        elif str.endswith( "txt" ):
            type_str = "html_view"
        elif str.endswith( "qml" ):
            type_str = "show"
        elif str.endswith( g_text_book_sub_name ):
            # open the text book 
            # and send the new command show the book first page.
            open_text_book_data_from_zip_file( str )
            type_str = "text_book"
            # show study page
            #str = "study"
            str = "main"
        elif str.endswith( g_package_data_sub_name ):
            # use dir
            type_str = "dir"


    if( type_str == "quit" ):
        #_d( len(g_qml_lastest_string_list) )
        if g_quit_command[:6] == "up_dir":
            type_str = 'up_dir'
            str = g_quit_command[7:]
            _d( str )
            g_quit_command = 'quit'
        elif g_quit_command == "quit":
            if( len(g_qml_lastest_string_list) < 1 ):
                print "cmd quit"
                sys_exit()
            else:
                type_str = "show"
                if g_qml_str_lastest_type == "show" :
                    if( len(g_qml_lastest_string_list) <= 1 ):
                        print "cmd quit"
                        sys_exit()
                    str = g_qml_lastest_string_list.pop()
                    str = g_qml_lastest_string_list.pop()
                else :
                    str = g_qml_lastest_string_list.pop()

    if( type_str == "up_dir" ):
        #print str
        cmds = str.split(' ')
        if( cmds[0] == "key_study" ):
            type_str = "text_book"
        else:
            str = str.replace( "../", "" )
            items = str.split( "/" )
            # need two level directory.
            if( len(items) > 2 and str != "data" ):
                items = str.split( "/" )
                del items[-1]
                str = "/".join(items)
                #print str
            type_str = "dir"


    g_qml_str_lastest_type = type_str
    if( type_str == "show" ):
        #print "append %s"%str 
        g_qml_lastest_string_list.append( str )
        qml_str = get_qml_file_string( str )
    elif( type_str == "dir" ):
        qml_str = get_qml_dir_string( str )
    elif( type_str == "test" ):
        qml_str = get_qml_test_string( str )
    elif( type_str == "html_view" ):
        qml_str = get_html_view_string( str )
    elif( type_str == "text_book" ):
        qml_str = get_text_book_string( str )
    elif type_str == "text_book_prev_page":
        if( g_text_book_now_page >= 2 ):
            g_text_book_now_page -= 1
        #print "g_text_book_now_page = %d"% g_text_book_now_page
        str = "study"
        qml_str = get_text_book_string( str )
    elif type_str == "text_book_next_page":
        book = g_text_book_data.elementsByTagName('book').at(0).toElement()
        page_count = book.childNodes().count()
        if( g_text_book_now_page < page_count ):
            g_text_book_now_page += 1
        #print "g_text_book_now_page = %d"% g_text_book_now_page
        #print "g_text_book_now_page = %d"%g_text_book_now_page
        str = "study"
        qml_str = get_text_book_string( str )
    elif type_str == "dict":
        qml_str = get_qml_dict_string( str )
    else:
        qml_str = ""
    return qml_str

def cmd( type, str ):
    global g_view
    global g_qmlRoot
    global g_mp3_play
    global g_mp3_play_list
    global g_switch_sound
    global g_quit_command
    #print "type = %s"%type
    #print "str = %s"%str
    str = str.replace( "\\", "/" )
    if type == "text_book_show_pos" :
        print str
    elif type == "set_quit":
        _d( type )
        _d( str )
        g_quit_command = str
    elif type == "sound":
        g_mp3_play_list.clear()
        iis = str.split(',')
        for ii in iis:
            g_mp3_play_list.append( ii )
        g_mp3_play_close()
        g_mp3_play_start()
    elif type == "switch_sound":
        g_mp3_play_list.clear()
        iis = str.split(',')
        if( g_switch_sound == iis[0] ):
            g_switch_sound = iis[1]
        else:
            g_switch_sound = iis[0]
        g_mp3_play_list.append( g_switch_sound )
        g_mp3_play_close()
        g_mp3_play_start()
    elif type == "append_sound":
        iis = str.split(',')
        for ii in iis:
            g_mp3_play_list.append( ii )
        if( g_mp3_play == "" ):
            g_mp3_play_start()
    elif type == "wait_sound":
        g_mp3_play_list.clear()
        g_mp3_play_close()
        g_mp3_play_list.append( str )
        g_mp3_play_start()
        g_mp3_play_wait()
    elif type == "stop_sound":
        g_mp3_play_close()
        g_mp3_play_list.clear()
    else:
        g_qmlRoot.setProperty( "qmlFile", "" )
        qml_str = get_qml( type, str )
        g_qmlRoot.setProperty( "code", qml_str )
        g_qmlRoot.setProperty( "qmlFile", "tmp.qml" )

def g_mp3_play_wait():
    global g_mp3_play
    global g_mp3_play_list
    while g_mp3_play != "":
        #print "wait sound end"
        if not g_mp3_play.isplaying() :
            #print "close"
            g_mp3_play_close()
        time.sleep( 1 )

def g_mp3_play_start():
    global g_mp3_play
    global g_mp3_play_list
    #print "next file"
    sn = g_mp3_play_list.popleft()
    sn = get_mp3_file( sn )
    #print sn
    try:
        g_mp3_play = mp3play.load( sn )
        g_mp3_play.play()
    except:
        print "sound device error"

def g_mp3_play_close():
    global g_mp3_play
    global g_mp3_play_list
    if g_mp3_play != "" :
        g_mp3_play.stop()
        del g_mp3_play
        g_mp3_play = ""

def timerProcess():
    global g_mp3_play
    global g_mp3_play_list
    #print "timer..."
    #g_mp3_play.seconds()
    #print len( g_mp3_play_list )
    if g_mp3_play != "":
        #print g_mp3_play.isplaying()
        if not g_mp3_play.isplaying() :
            #print "close"
            g_mp3_play_close()
    elif g_mp3_play == "" and len( g_mp3_play_list ) > 0:
        g_mp3_play_start()



class DictValue(QtCore.QObject):
    def __init__(self):
        super(DictValue,self).__init__()
        self.r = 0
    # if a slot returns a value the return value type must be explicitly
    # defined in the decorator
    @QtCore.Slot(str,str,result=str)
    def dict(self,type,word):
        global g_dict
        #print type
        #print word
        #return "abcdef"
        if type == "word":
            return word
        elif type == "sound":
            iis = g_dict[ word ].split( '\t' )
            return iis[0]
        elif type == "content":
            iis = g_dict[ word ].split( '\t' )
            return iis[1]
            #return g_dict[ word ]
        elif type == "no":
            #pos = g_dict.keys().sort().index( "hello" )
            key_list = g_dict.keys()
            key_list.sort()
            #print word
            try:
                pos = key_list.index( word )
            except:
                pos = 0
            #print pos
            return "%d"%pos
        return ""





if __name__ == '__main__':


    try:
        shutil.rmtree( "tmp" )
    except:
        print "oh,oh"
    os.mkdir( "tmp" )

    dict_value = DictValue()

    app = QApplication(sys.argv)
    d = app.desktop()
    w = d.width()
    h = d.height()
    #print "w=%d,h=%d"%(w,h)
    x = (w-1024)/2
    y = (h-768)/2
    #g_view.move( (w-1024)/2, (h-768)/2 )
    g_view = QtDeclarative.QDeclarativeView()
    g_view.setRenderHints(QtGui.QPainter.SmoothPixmapTransform)
    #component = QDeclarativeComponent( g_view.engine(), QUrl( "nb/qs.qml" ) )
    component = QDeclarativeComponent( g_view.engine(), QUrl( "qrc:nb/qs.qml" ) )
    #component = QDeclarativeComponent( g_view.engine() )
    #component.setData( s_qs_qml, QUrl( g_path + "qs.qml" ) )
    if component.isReady() == False :
        print "component error"
        print component.errorSting()
        exit(0)
    g_qmlRoot = component.create()


    context = g_view.rootContext()
    context.setContextProperty("dict_value", dict_value)



    scene = QGraphicsScene()
    g_view.setScene( scene )
    scene.addItem( g_qmlRoot )

    #cmd( "show", "menu/t.qml" )
    #cmd( "show", "menu/main.qml" )
    #cmd( "show", "menu/dicts/main.qml" )
    #cmd( "dict", "新英汉" )
    #cmd( "show", "menu/primary_school/funs/encyclopedic/main.qml" )
    #cmd( "dir", "data/百科知识" )
    #cmd( "sound", ":study" )
    cmd( "auto", "user/小学/电子课本/njyy3b10sx.p".decode('utf8') )
    #cmd( "auto", "user/小学/电子课本/xbzyy8s308.p".decode('utf8') )

    g_qmlRoot.cmd.connect( cmd )
    g_view.setMinimumWidth(1024)
    g_view.setMinimumHeight(768)

    # set the timer
    timer = QTimer()
    timer.timeout.connect( timerProcess )
    timer.start(500);


    #g_qmlRoot.setProperty( "x", x )
    #g_qmlRoot.setProperty( "y", y )
    #g_view.showFullScreen()
    g_view.show()

    app.exec_()




tmp = """

"""





























