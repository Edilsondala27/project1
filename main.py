from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder


KV = """
<ScreenOne>
    name: 's1'
    MDRaisedButton:
        text: 'panzo'
        pos_hint:{'center_x':.5 , 'center_y':.5}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 's2'
            print("amor")

<ScreenTwo>
    name: 's2'
    MDRaisedButton:
        text: 'dala'
        pos_hint:{'center_x':.5 , 'center_y':.5}
        on_release: 
            root.manager.transition.direction = 'right'
            root.manager.current = 's1'
"""

class ScreenOne(MDScreen):
    pass

class ScreenTwo(MDScreen):
    pass



class TestApp(MDApp):

    def build(self):
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(ScreenOne())
        sm.add_widget(ScreenTwo())
    
        return sm

if __name__ == '__main__':
    TestApp().run()
