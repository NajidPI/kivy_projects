username_helper = """
MDTextField:
    hint_text: "Enter Username"

    helper_text: "or click on forgot username"
    helper_text_mode: 'on_focus'

    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color

    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["clock",lambda x: app.navigation_draw()]]
            elevation: 10
        MDLabel:
            text: 'Hello World'
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["coffee",lambda x: app.navigation_draw()]]
                mode: 'free-end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()

"""

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Navigation Drawer'
                        left_action_items: [["menu",lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 10
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'baby-yoda.jpg'

                MDLabel:
                    text: '   NajidPI'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: '   najid.0311@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
"""

screen_nav = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:


<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5,'center_y': 0.6}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Najid'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Lets upload some files'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: root.manager.current = 'menu'

"""