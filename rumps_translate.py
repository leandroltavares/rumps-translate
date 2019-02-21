from rumps import App, MenuItem, Window, alert
from googletrans import Translator


class TranslateStatusBarApp(App):
    def __init__(self):
        super().__init__("Translate App",  icon='icon.png', quit_button=MenuItem('Quit', key='q'))
        self.menu = [MenuItem('Translate', callback=self.translate, key='t')]
        self.translator = Translator()

    def translate(self, _):
        window = Window('Type something to translate', 'Translate', cancel=True)
        window.icon = None
        response = window.run()

        if response.clicked == 1:
            try:
                translated = self.translator.translate(response.text, dest='pt')
                # window.default_text = translated.text
                # window.run()
                alert(translated.text)
            except:
                alert('Sorry...')


if __name__ == "__main__":
    TranslateStatusBarApp().run()
