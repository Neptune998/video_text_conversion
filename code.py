# Libraries import
import speech_recognition as sr 
import moviepy.editor as mp

# It will clip the video 
# subclip(starttime, endtime) to clip portion of video
# you can remove the subclip to convert complete video
clip = mp.VideoFileClip(r"sample1.mp4").subclip(10, 100)

# It will write the audio in converted_audio.wav file.
clip.audio.write_audiofile(r"Converted_audio.wav")
print("Finished the convertion into audio...")


# Now from here we convert audio into text

# It will read audio file
audio = sr.AudioFile("Converted_audio.wav")
print("Audio file readed...")

# Here the magic start
# create an instance of recognizer as r 
r = sr.Recognizer()

with audio as source:
    audio_file = r.record(source)

# Here we get our text 
result = r.recognize_google(audio_file)

# Now we will store the text in file
with open('recognized.txt',mode ='w') as file:
    file.write(result)

print("Wooh.. You did it...")
