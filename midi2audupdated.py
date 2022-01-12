import io
import numpy as np
import pretty_midi
import streamlit as st
from scipy.io import wavfile

st.title(":musical_note: Convert a MIDI file to WAV")
st.subheader("Developed with 💖 by TechNinja")
uploaded_file = st.file_uploader("Upload Midi File",type=["mid","midi"])
extracte = st.button("Convert Midi to Audio")
output = st.empty()
midi_file = None
if uploaded_file is None:
    output.warning("Please upload a mid or midi file to proceed.")
else:
    if extracte:
       midi_file = uploaded_file
       st.markdown("---")
       with st.spinner(f"Converting.....Please be patient."):
           midi_data = pretty_midi.PrettyMIDI(midi_file)
           audio_data = midi_data.fluidsynth()
           audio_data = np.int16(
               audio_data / np.max(np.abs(audio_data)) * 32767 * 0.9
           )  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py
           virtualfile = io.BytesIO()
           wavfile.write(virtualfile, 44100, audio_data)

       st.audio(virtualfile)
       st.success("Midi file successfully converted to Audio.")
       st.markdown("Download the audio by clicking the 3 dots section on the media player")


