from jarvis_functions import jarvis_input, jarvis_output, jarvis_open, data, jarvis_time, weather, alarm_set, jarvis_wiki, jarvis_jokester, clear_terminal
from jarvis_functions import jarvis_youtube, jarvis_youtube_instant, jarvis_stt, jarvis_volume_ctrl, layout, random_song_picker
import pyautogui, os, random


jarvis_output("Hello sir")
i = 0
while i == 0:
    e = jarvis_input()
    if e is None:
        pass
    else:
        print("User:{}".format(e))
        e_s = e.split(" ")
        # Jarvis-Tree
        if e == "jarvis" or e == "hey jarvis" or e == "hello" or e == "hello jarvis" or e == "yo jarvis":
            jarvis_output("Yes sir?")
            j_1 = jarvis_input()
            if j_1 == "how are you" or j_1 == "how are you?":
                jarvis_output("I'm fine sir, thank you. How are you?")
                j_2 = jarvis_input()
                if j_2 == "i'm good" or j_2 == "i'm great" or j_2 == "feeling good" or j_2 == "i'm okay" or j_2 == "i'm fine":
                    jarvis_output("That's good to hear")
            if j_1 == "can you play me a song" or j_1 == "can you play me a song?" or j_1 == "play me a song":
                jarvis_output("Sure thing")
                jarvis_youtube_instant(random_song_picker())
            if j_1 == "what's up":
                response_j001 = ["not much", "nothing"]
                jarvis_output(response_j001[random.randint(1, len(response_j001)-1)])
            if j_1 == "tell me a joke" or j_1 == "can you tell me a joke" or j_1 == "can you tell me a joke?":
                jarvis_jokester()
        # In progress
        if e_s[0] == "layout":
            layout(e_s[1])
        if e == "tell me a joke":
            jarvis_jokester()
        if e == "set alarm" or e == "set an alarm":
            alarm_set()
        # Completed
        if e == "full screen" or e == "fullscreen":
            pyautogui.hotkey("F11")
        if e == "speech to text":
            jarvis_stt()
        if e == "wikipedia":
            jarvis_wiki()
        if e == "pause" or e == "unpause" or e == "stop" or e == "continue":
            pyautogui.hotkey("space")
        # Google Related
        if e_s[0] == "google" and e.split(" ", 1)[1] is not None:
            os.startfile("https://www.google.com/search?q=" + e.split(" ", 1)[1])
        if e == "youtube":
            jarvis_youtube()
        if len(e_s) >= 2:
            if e_s[0] == 'youtube' or e_s[0] == 'play':
                jarvis_youtube_instant(e.split(" ", 1)[1])
        if e == "clear terminal":
            clear_terminal()
        if e == "close" or e == "shut down":
            jarvis_output("Goodbye sir")
            i = 1
        if e == "data" or e == "information" or e == "weather report":
            data()
        if e == "weather report" or e == "what's the weather":
            center_weather_report = weather().center(20)
        # Volume - Down
        if e == "turn down the volume a bit" or e == "turn the volume down a bit" or e == "turn the volume down a lot" or e == "turn the volume down a bit though" or e == "turn down the volume a bit though" or e == "turn down the volume a lot":
            jarvis_volume_ctrl("down", 50)
        if e == "turn the volume down" or e == "turn the volume down though" or e == "turn down the volume" or e == "turn down the volume though":
            jarvis_volume_ctrl("down", 25)
        if e == "turn the volume slightly down" or e == "turn the volume a little bit down" or e == "turn the volume down a little bit" or e == "turn the volume slightly down though":
            jarvis_volume_ctrl("down", 10)
        # Volume - Up
        if e == "turn up the volume a bit" or e == "turn the volume up a bit"  or e == "turn the volume up a bit though" or e == "turn up the volume a bit though" or e == "turn up the volume a lot" or  e == "turn the volume up a lot":
            jarvis_volume_ctrl("up", 50)
        if e == "turn the volume up" or e == "turn up the volume" or e == "turn up the volume though" or e == "turn the volume up though" :
            jarvis_volume_ctrl("up", 25)
        if e == "turn the volume slightly up" or e == "turn the volume up a little bit" or e == "turn the volume a little bit up" or e == "turn the volume slightly up though":
            jarvis_volume_ctrl("up", 10)
        # Volume - Down
        if e == "mute":
            jarvis_volume_ctrl("mute", None)
        # Open
        if e == "open fxp":
            jarvis_open("https://www.fxp.co.il/", "Opening FXP")
        if e == "open google":
            jarvis_open("https://www.google.co.il/?hl=iw", "Opening Google")
        if e == "open desmos":
            jarvis_open("https://www.desmos.com/calculator", "Opening Desmos")
        if e == "open youtube":
            jarvis_open("https://www.youtube.com/", "Opening YouTube")
        if e == "open github":
            jarvis_open("https://www.github.com/", "Opening Git Hub")
        if e == "open reddit":
            jarvis_open("https://www.reddit.com/", "Opening Reddit")
        if e == "open whatsapp":
            jarvis_open("https://web.whatsapp.com/", "Opening Whats App")
        if e == "open telegram":
            jarvis_open("https://web.telegram.org/#/im", "Opening Telegram")
        if e == "open discord":
            jarvis_open("C:\\Users\\97252\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe", "Opening Discord")
        if e == "open visual studio":
            jarvis_open(r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe", "Opening Visual Studio")
