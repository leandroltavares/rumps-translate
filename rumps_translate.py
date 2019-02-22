from rumps import App, MenuItem, Window, alert, separator, quit_application
from googletrans import Translator, constants


class TranslateStatusBarApp(App):
    def __init__(self):
        super().__init__("Translate App",  icon='icon.png', quit_button=None)
        self.dest_lang_title = 'portuguese'
        self.translator = Translator()
        self.update_menu()

    def quit(self, _):
        quit_application()

    def update_menu(self):
        self.menu.clear()
        self.menu = [
            MenuItem(f'Translate to {self.dest_lang_title}', callback=self.translate, key='t'),
            separator,
            [MenuItem('Select target language'), self.list_languages_menu(self.define_target_language)],
            separator,
            MenuItem(f'Quit', callback=self.quit, key='q')
             ]

    def list_languages_menu(self, callback):
        return [MenuItem(lang, callback=callback) for lang in constants.LANGCODES]

    def translate(self, _):
        window = Window(f'Type something to translate to {self.dest_lang_title}', 'Translate', cancel=True)
        window.icon = None
        response = window.run()

        if response.clicked == 1:
            try:
                translated = self.translator.translate(response.text,
                                                       dest=constants.LANGCODES[self.dest_lang_title])
                alert(translated.text)
            except:
                alert('Sorry, something went wrong...')

    def define_target_language(self, sender):
        self.dest_lang_title = sender.title
        self.update_menu()


if __name__ == "__main__":
    TranslateStatusBarApp().run()
