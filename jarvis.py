def jarvis():
    import speech_recognition as sr
    import wikipedia
    import os
    import webbrowser
    import urllib.request
    import urllib.parse
    import re
    import random
    import subprocess
    from cryptography.fernet import Fernet
    import datetime
    import pyautogui
    import time
    import pyttsx3

    def say(sentence):
        engine = pyttsx3.init()
        engine.say(sentence)
        engine.runAndWait()

    r = sr.Recognizer()
    print("Hello, I'm J.A.R.V.I.S")
    say("Hello, I'm Jarvis")
    z = "p"
    # Songs-List
    songs = ["טונהמן ג'ונס - איפור", "Jason Mraz - I'm Yours", "Moves Like Jagger - Maroon 5 featuring Christina Aguilera", "Green Day - 21 Guns", "טונה - נשאר בחיים", "imagine dragons - demons", "green day - american idiot", "walk like an egyptian", "maroon 5 - payphone", "another one bites the dust", "airplanes - B.o.B", "Nirvana - Smells Like Teen Spirit (Official Music Video)",
             "Holiday / Boulevard of Broken Dreams", "Red Hot Chili Peppers - Otherside [Official Music Video]", "G-Eazy - Random (Official Audio)", "טונהמן ג'ונס/מאיר אריאל- עברנו את פרעה", "ג'ימבו ג'יי ולהקת ספא (קליפ רשמי) - עשיתי Jimbo J", "טונה - בסיבוב (עם צליל דנין) \\ Tuna - Besivuv ft. Tzlil", "Mark Ronson - Uptown Funk (Official Video) ft. Bruno Mars", "'m Still Here (Jim's Theme) from Treasure Planet",
             "Passanger - Let Her Go", "Owl City - Fireflies", "The Black Eyed Peas - WHere is The Love?", "Phil Colins - Son of Man", "Phil Colins - You'll be in My Heart", "Brave - Touch the Sky", "Mulan - Reflections [HQ]", "Pocahontas | Colors of the Wind", "Hercules | Zero to Hero", "טונה - הכל זה בצוות", "Oasis - Champagne Supernova", "מאיר בנאי - כמה אהבה"]
    # Start
    while z != "d":

        with sr.Microphone() as begin_operation:

            begin_audio = r.listen(begin_operation, timeout=2, phrase_time_limit=2)
            try:

                key = r.recognize_google(begin_audio).lower()
                print("User: {}".format(key))
                if key == "jarvis" or key == "hello jarvis" or key == "hey jarvis" or key == "start":
                    variable_u = 0
                    print("Yes sir?")
                    say("Yes sir?")
                    while variable_u != 5:
                        # Starthello I'm taking advantage of this technology 
                        with sr.Microphone() as speech:
                            audio = r.listen(speech, phrase_time_limit=3)
                            try:

                                text = r.recognize_google(audio).lower()
                                print("User: {}".format(text))
                                w = text.split(' ', 1)[0]
                                w1 = text.partition(' ')[2]
                                wlist = text.split(" ")
                                #Say
                                # Volume
                                if w == "jarvis":
                                    say("Yes sir?")
                                    print("Yes sir?")
                                if w == "volume":
                                    exal = 0
                                    perc = int(wlist[2])
                                    if wlist[1] == "rise" or wlist[1] == "increase" or wlist[1] == "increased" or wlist[1] == "up" or w == "up to":
                                        for i in range(int(perc/2)):
                                            pyautogui.hotkey("volumeup")
                                            exal += 2
                                            if i % 6 == 0:
                                                time.sleep(0.5)
                                        print("Volume increased by {}".format(exal) + "%")
                                        say("Volume increased by {}".format(exal) + "%")
                                    if wlist[1] == "down" or wlist[1] == "decrease" or wlist[1] == "decreased" or wlist[1] == "descend" or w1 == "down to":
                                        for i in range(int(perc/2)):
                                            pyautogui.hotkey("volumedown")
                                            exal += 2
                                            if i % 6 == 0:
                                                time.sleep(0.5)
                                        print("Volumed decreased by {}".format(exal) + "%")
                                        say("Volumed decreased by {}".format(exal) + "%")
                                    if wlist[1] == "mute" or wlist[1] == "unmute":
                                        pyautogui.hotkey("volumemute")

                                # Encrypt
                                if text == "full screen":
                                    pyautogui.hotkey("F11")
                                    say("Changing to full screen")

                                if w == "encrypt":
                                    key = "wUpTRAElFwPFSX3X_UH5b-EwHsGikwtmVGw3-fzfTlM="
                                    encoded = w1.encode()
                                    f = Fernet(key)
                                    encrypted = f.encrypt(encoded)
                                    print(encrypted)
                                    say("Done, check terminal")

                                # Open Division
                                if w == "open":
                                    if w1 == "wikipedia":
                                        os.startfile("https://www.wikipedia.org/")
                                        print("Opening Wikipedia")
                                        say("Opening Wikipedia")
                                    if w1 == "discord":
                                        os.system("C:\\Users\\97252\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
                                        print("Opening Discord")
                                        say("Opening Discord")
                                    if w1 == "visual studio":
                                        os.startfile(r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe")
                                        print("Opening Visual Studio")
                                        say("Opening Visual Studio 2019")
                                    if w1 == "google" or text == "chrome":
                                        webbrowser.open("https://www.google.co.il/?hl=iw")
                                        print("Opening Google")
                                        say("Opening Google")
                                    if w1 == "fxp":
                                        print("Opening FXP")
                                        webbrowser.open_new_tab("https://www.fxp.co.il/")
                                        say("Opening F X P")
                                    if w1 == "dungeons & dragons" or w1 == "dnd" or w1 == "d&d":
                                        webbrowser.open("steam://rungameid/206480")
                                        say("Opening Dungeons and Dragons Online")
                                        print("Opening Dungeons and Dragons")
                                    if w1 == "youtube":
                                        webbrowser.open("https://www.youtube.com/?hl=iw&gl=IL")
                                        print("Opening YouTube")
                                        say("Opening YouTube")
                                    if w1 == "solex":
                                        webbrowser.open("https://solx.co.il/")
                                        print("Opening SolX")
                                        say("Opening Sol X")
                                    if w1 == "whatsapp":
                                        webbrowser.open("https://web.whatsapp.com/")
                                        print("Opening WhatsApp")
                                        say("Opening Whats Up")
                                    if w1 == "brawlhalla":
                                        webbrowser.open("steam://rungameid/291550")
                                        print("Opening Brawlhalla")
                                        say("Opening Brawlhalla")
                                    if w1 == "reddit" or w1 == "ready":
                                        webbrowser.open("https://www.reddit.com/")
                                        print("Opening Reddit")
                                        say("Opening Reddit")
                                    if w1 == "telegram":
                                        webbrowser.open("https://web.telegram.org/#/im")
                                        print("Opening Telegram")
                                        say("Opening Telegram")
                                    if w1 == "euro stream" or w1 == "hdeuropix" or w1 == "europix":
                                        webbrowser.open("https://europixhd.net/")
                                        print("Opening EuroPixHd")
                                        say("Opening HD Euro Pix")
                                    if w1 == "graphing calculator" or w1 == "graphing" or w1 == "desmos":
                                        print("Opening Desmos")
                                        webbrowser.open("https://www.desmos.com/calculator")
                                        say("Opening Desmos")
                                    if w1 == "calculator":
                                        os.startfile("C:\\Windows\\System32\\calc.exe")
                                        print("Open Calculator")
                                        say("Opening Calculator")
                                    if w1 == "gmail":
                                        webbrowser.open("https://www.gmail.com/")
                                        print("Open Gmail")
                                        say("Opening Mail")
                                    if w1 == "google docs" or w1 == "google document" or w1 == "google documents":
                                        print("Opening Google Docs")
                                        webbrowser.open("https://docs.google.com/")
                                        say("Opening Google Docs")
                                    if w1 == "stack overflow":
                                        print("Opening Stack Overflow")
                                        webbrowser.open("https://stackoverflow.com/")
                                        say("Opening Stack Overflow")

                                if w == "date":
                                    print(datetime.datetime.now())

                                if text == "start program" or text == "run the program" or text == "run program" or text == "start the problem":
                                    pyautogui.hotkey("F5", "Fn", "Ctrl")

                                if w == "wikipedia" or w == "wiki":
                                    y = wikipedia.summary(w1)
                                    print(y)
                                    say("Do you want me to read it sir?")
                                
                                # Close Divison
                                if w == "close":
                                    os.system("taskkill /im {}.exe".format(w1))

                                if w == "pause":
                                    variable_u = 5

                                # Shutdown command
                                if text == "end" or text == "shut down" or text == "go to sleep" or text == "do me a favor and go to sleep" or text == "you can go now":
                                    z = "d"
                                    break
                                # Q&A
                                if text == "what jarvis stands for":
                                    print("It stands for Just a Rather Very Intelligent System")

                                # if w == "jarvis":
                                #     if w1 == "say":
                                #         print("Jarvis:" + w2)

                                # Jarvis-Chat Division
                                # Weather
                                # Google-Search
                                if w == "google" or w == "search":
                                    webbrowser.open("https://www.google.com/search?q=" + w1)

                                # YoutubeVids Divison
                                if w == "youtube" or w == "play" or w == "youtube youtube" or w == "play youtube" or w == "play" or w == "youtube":

                                    try:
                                        quick = text.partition(' ')[2]
                                        check = text.split(' ')[1]

                                        if check == "random" or check == "some music":
                                            textmusic = songs[random.randint(0, (len(songs)-1))]
                                            print("Playing " + textmusic)
                                            query_string = urllib.parse.urlencode({"search_query": textmusic})
                                            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                                            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                                            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
                                            say("Playing a random song")

                                        else:
                                            if check == "playlist":
                                                playlist = quick.partition(' ')[2]
                                                if playlist == "vibe":
                                                    webbrowser.open("https://www.youtube.com/watch?v=KI96t1Xi9cI&list=PL0QwLwMzkTujP8BKJTYFU8KHVhNqnw2Qi&index=2&t=0s")
                                                    say("Playing Playlist Vibe")
                                                if playlist == "songs":
                                                    webbrowser.open("https://www.youtube.com/watch?v=rn_YodiJO6k&list=PL0QwLwMzkTugenoHIO2dlpN5nDaeblgQA&index=2&t=0s")
                                                    say("Playing Playlist Songs")
                                            else:
                                                textmusic = quick
                                                query_string = urllib.parse.urlencode({"search_query": textmusic})
                                                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                                                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                                                webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
                                                print("Playing " + quick)
                                                say("Playing" + quick)

                                    except:
                                        print("Sorry, didn't quite understand")
                                        say("Sorry, didn't quite understand")

                                # Clear
                                if text == "clear" or text == "can you clear" or text == "clear screen":
                                    os.system("cls")
                                    say("Clearing")

                                if text == "thank you":
                                    print("You're welcome")
                                    say("You're welcome sir")

                                if text == "good morning":
                                    print("Good morning sir")
                                    say("Good Morning sir")
                                if text == "good afternoon":
                                    print("Good Afternoon sir")
                                    say("Good afternoon sir")
                                if text == "good night":
                                    print("Good Night sir")
                                    say("Good night")

                                if text == "i'm bored":
                                    print("May I offer you something?")
                                    say("May I offer you something?")
                                    with sr.Microphone() as e_speech:
                                        audiohelp = r.listen(e_speech, timeout=4, phrase_time_limit=2)
                                        try:
                                            texte = r.recognize_google(audiohelp).lower()
                                            print(texte)
                                            if texte == "yes" or texte == "sure" or texte == "sure why not":
                                                print("Alright")
                                                e_offer = ["Listen to music", "Read an article on Wikipedia", "Watch something on YouTube"]
                                                e_offer_r = (e_offer[random.randint(0, len(e_offer)-1)])
                                                print(e_offer_r)
                                                say(e_offer_r)
                                                e_offer_check = e_offer_r.lower()
                                                if e_offer_check == "watch something on youtube":
                                                    webbrowser.open("https://www.youtube.com/?hl=iw&gl=IL")
                                                if e_offer_check == "read an article on wikipedia":
                                                    webbrowser.open("https://www.wikipedia.org/")
                                                if e_offer_check == "listen to music":
                                                    textmusic = songs[random.randint(0, (len(songs)-1))]
                                                    print("Playing " + textmusic)
                                                    query_string = urllib.parse.urlencode({"search_query": textmusic})
                                                    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                                                    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                                                    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

                                                if texte == "nah" or texte == "no" or texte == "no thanks":
                                                    print("Okay")
                                                    say("Okay")

                                            else:
                                                pass

                                        except:
                                            pass
                                if text == "write the next" or text == "type the next":
                                    text_u = 0
                                    while text_u == 0:
                                        with sr.Microphone() as stt:
                                            speech_to_text_audio = r.listen(
                                                stt, phrase_time_limit=4)
                                            try:
                                                what_i_have_said = r.recognize_google(
                                                    speech_to_text_audio)
                                                if what_i_have_said == "stop" or what_i_have_said == "Stop":
                                                    text_u = 2
                                                else:
                                                    sttlist = what_i_have_said.split(
                                                        " ")
                                                    for i in range(len(sttlist)):
                                                        typing = sttlist[i]
                                                        for j in range(len(typing)):
                                                                k = typing[j]
                                                                pyautogui.typewrite(
                                                                    [k])
                                                        pyautogui.typewrite(["space"])
                                            except:
                                                pass
                            except:
                                pass

                # Shut down
                if key == "end" or key == "shut down" or key == "shut it down" or key == "shutdown":
                    z = "d"

                if key == "clear" or key == "can you clear" or key == "clear screen":
                    os.system("cls")
                    say("Clearing")

            except:
                pass
    # End

    print("Goodbye sir")
    say("Goodbye sir")
