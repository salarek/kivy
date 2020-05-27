from kivy.app import App
from plyer import gps
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class StartupPage(GridLayout):
    def __init__(self, **kwargs):
        super(StartupPage, self).__init__(**kwargs)
        self.localizationHistory = Label(size_hint_y=5)
        self.add_widget(self.localizationHistory)
        self.add_widget(Label(text="Podaj IP"))
        gps.configure(on_location=self.on_gps_location)
        gps.start()
    def on_gps_location(self, **kwargs):
        lat = kwargs['lat'] 
        lon = kwargs['lon']
        self.localizationHistory.text = str(lat)

class MainApp(App):
    
    def build(self):
        return StartupPage
        
MainApp().run()