import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5

print("Loading Whisper model...")
model = WhisperModel("base", device="cpu", compute_type="int8")
print("Whisper is ready!")


def listen():
    print("\n🎙️ Listening...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()
    write("recording.wav", SAMPLE_RATE, recording)

    print("Processing...")

    segments, info = model.transcribe(
        "recording.wav",
        language="en",
        beam_size=5
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()
