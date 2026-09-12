from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from random import randint
Window.size=(360, 640)

class LoveApp(App):
    def second_screen(self, instance):
        self.layout.clear_widgets()
        background2=Image(
                    source="fon.png",
                    size_hint=(1,1),
                    allow_stretch=True,
                    keep_ratio=False
                    )
        self.layout.add_widget(background2)
        cat2 = Image(
                    source="kotek2.png",
                    size_hint=(None, None),
                    size=(300, 250),
                    pos=(30,300)
                )
        self.layout.add_widget(cat2)
        text=Label(
                    text="я тебя очень сильно люблююю",
                    font_size=22,
                    font_name="podzagolovki.otf",
                    color=(0.8, 0.35, 0.5,1),
                    size_hint=(1, None),
                    height=50,
                    pos=(0, 250)
                )
        self.layout.add_widget(text)
        Clock.schedule_interval(self.create_heart, 0.5)
    def create_heart(self, dt):
        heart = Label(
            text="♥",
            font_name="Arial",
            font_size=30,
            color=(1, 0.3, 0.5, 1),
            size_hint=(None, None),
            size=(40, 40)
        )

        heart.x = randint(0, int(self.layout.width - 40))
        heart.y = 0

        self.layout.add_widget(heart)

        def move_heart(dt):
            heart.y += 5

            if heart.y > self.layout.height:
                self.layout.remove_widget(heart)
                return False

        Clock.schedule_interval(move_heart, 0.01)
    def build(self):
        self.layout=FloatLayout()
        layout=self.layout
        background=Image(
            source="fon.png",
            size_hint=(1,1),
            allow_stretch=True,
            keep_ratio=False
            )
        layout.add_widget(background)
        cat1 = Image(
            source="kotek1.png",
            size_hint=(None, None),
            size=(300, 250),
            pos=(30,300)
        )
        layout.add_widget(cat1)
        text=Label(
            text="для моего сладкого котьки",
            font_size=22,
            font_name="podzagolovki.otf",
            color=(0.8, 0.35, 0.5,1),
            size_hint=(1, None),
            height=50,
            pos=(0, 250)
        )
        layout.add_widget(text)
        button=Button(
            text="продолжить",
            font_size=22,
            font_name="podzagolovki.otf",
            color=(0.8, 0.35, 0.5,1),
            size_hint=(None, None),
            size=(180,50),
            pos=(90,200),
            background_normal="",
            background_color=(1, 0.82, 0.9 ,1),
            
        )
        layout.add_widget(button)
        button.bind(on_press=self.second_screen)
        return layout 
LoveApp().run()