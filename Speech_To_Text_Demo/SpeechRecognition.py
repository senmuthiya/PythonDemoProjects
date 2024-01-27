from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile('mother_teresa.wav') as audio_file:
   audio = recognizer.record(audio_file)
   text = recognizer.recognize_google(audio)
print(text)



# import speech_recognition as sr

# def transcribe_audio(file_path):
#     recognizer = sr.Recognizer()

#     with sr.AudioFile(file_path) as audio_file:
#         audio_data = recognizer.record(audio_file)

#         try:
#             text = recognizer.recognize_google(audio_data)
#             return text
#         except sr.UnknownValueError:
#             return "Speech Recognition could not understand the audio"
#         except sr.RequestError as e:
#             return f"Could not request results from Google Speech Recognition service; {e}"

# # Replace 'your_audio_file.wav' with the path to your .wav file
# file_path = 'mother_teresa.wav'
# result = transcribe_audio(file_path)

# print("Transcription:")
# print(result)
