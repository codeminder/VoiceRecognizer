import speech_recognition  as s_r


def main():
    for index, name in enumerate(s_r.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    
    r = s_r.Recognizer()
    my_mic = s_r.Microphone() # device_index=13
    
    with my_mic as source:
        print("say now!")
        audio = r.listen(source)
        print(r.recognize_google(audio))

if __name__ == "__main__":
    main()
