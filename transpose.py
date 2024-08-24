import moviepy.editor as mp 
import speech_recognition as sr
import librosa

# Read in video file, save the audio of video file as wav. 
video = mp.VideoFileClip('video.mp4')
audio = video.audio
audio.write_audiofile('audio.wav')

# Determine clip length and calculate number of 30 second segments (recognize_google function only works on audio <30s)
clip_length = librosa.get_duration(path='audio.wav')
num_30_sec_chunks = int(round(clip_length/30, 0))

# Initialize Recognizer, set pause threshold
r = sr.Recognizer()
r.pause_threshold = 5

# For the amount of 30 second segments, take the wav file and make a partial transcript chunk from Google's API. Append that partial transcript to a list.
transcripts = []
with sr.AudioFile('audio.wav') as source:
	for chunk in range(num_30_sec_chunks + 1):
		audio_text = r.record(source, duration=30)
		partial_transcript = r.recognize_google(audio_text, language='en-US', key=None, show_all=False)
		transcripts.append(f'{partial_transcript} ')

# Write the chunks into a text file
with open('transcription.txt', 'w') as file:
	for transcript in transcripts:
		file.write(transcript)