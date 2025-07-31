class Light:
    def flash(self):
        pass

class LightImpl(Light):
    def flash(self):
        print("flashing color light")

class Music:
    def play(self):
        pass

class MusicImpl(Music):
    def play(self):
        print("playing music")

class Video:
    def show(self):
        pass
    
class VideoImpl(Video):
    def show(self):
        print("showing video")

class Facade:
    __light = None
    __music = None
    __video = None

    def __init__(self):
        self.__light = LightImpl()
        self.__music = MusicImpl()
        self.__video = VideoImpl()

    def sing(self):
        print("singing...")
        self.__light.flash()
        self.__music.play()
        self.__video.show()

    def dance(self):
        print("dancing...")
        self.__light.flash()
        self.__music.play()
        self.__video.show()

facade = Facade()
facade.sing()
facade.dance()  

