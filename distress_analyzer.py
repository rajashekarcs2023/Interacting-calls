


# Add your Hume API key here
HUME_API_KEY = ""
 # Ensure you set this


import asyncio
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
from hume import AsyncHumeClient
from hume.expression_measurement.stream import Config
from hume.expression_measurement.stream.socket_client import StreamConnectOptions

import pyaudio
import wave
import time  # Import time for adding delay
import pprint  # For better logging of the response

 # Replace with your actual API key

class DistressAnalysisRequest(Model):
    duration: int  # Duration of recording in seconds

class DistressAnalysisResponse(Model):
    distress_level: str
    interpretation: str

# Define the distress analyzer agent
distress_analyzer = Agent(
    name="distress_analyzer",
    port=8000,
    seed="distress_analyzer_secret_seed",
    endpoint=["http://127.0.0.1:8000/submit"],
)

# Function to record audio from the microphone
async def record_audio(duration):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    # Let the user know to start speaking
    print("Preparing to record. Please speak into the microphone when prompted.")
    time.sleep(2)  # Give the user 2 seconds to prepare

    # Start recording
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording started. Please speak into the microphone now...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Recording done.")

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME

# Function to analyze the recorded audio using Hume API
async def analyze_audio(file_path):
    client = AsyncHumeClient(api_key=HUME_API_KEY)
    
    # Configure prosody model for analyzing audio files
    model_config = Config(prosody={})
    
    # Set up WebSocket streaming options
    stream_options = StreamConnectOptions(config=model_config)
    
    # Connect to Hume WebSocket and analyze the file
    async with client.expression_measurement.stream.connect(options=stream_options) as socket:
        result = await socket.send_file(file_path)  # Sending the audio file for analysis
        # Log the full response for inspection using pprint
        pprint.pprint(vars(result))
        return result

# Function to interpret the prosody result and calculate distress level
def interpret_distress(prosody_result):
    distress_emotions = ['Stress', 'Anxiety', 'Fear', 'Sadness']
    
    # Check if prosody and predictions exist
    if not hasattr(prosody_result, 'prosody') or not hasattr(prosody_result.prosody, 'predictions'):
        return "Error", "Invalid response structure from Hume API."
    
    if not prosody_result.prosody.predictions:
        return "Error", "No predictions returned from the model."
    
    # Access emotions from the first prediction
    first_prediction = prosody_result.prosody.predictions[0]
    
    if not hasattr(first_prediction, 'emotions'):
        return "Error", "No emotions data found in the prediction."
    
    emotion_scores = first_prediction.emotions
    
    # Calculate distress level based on emotions
    distress_level = sum(emotion.score for emotion in emotion_scores if emotion.name in distress_emotions)
    
    if distress_level < 0.3:
        return "Low distress", "Low levels of distress detected in speech."
    elif distress_level < 0.6:
        return "Moderate distress", "Moderate levels of distress detected in speech."
    else:
        return "High distress", "High levels of distress detected in speech."

# Event handler when the agent starts up
@distress_analyzer.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"Distress Analyzer started, address: {ctx.address}")
    await fund_agent_if_low(ctx.wallet.address())
    

# Event handler to process the distress analysis request
@distress_analyzer.on_message(model=DistressAnalysisRequest)
async def handle_distress_analysis(ctx: Context, sender: str, msg: DistressAnalysisRequest):
    ctx.logger.info(f"Received distress analysis request from {sender}")

    try:
        # Record audio based on the request duration
        audio_file = await record_audio(msg.duration)
        
        # Analyze the recorded audio
        analysis_result = await analyze_audio(audio_file)
        ctx.logger.info(f"Raw analysis result: {analysis_result}")
        
        # Interpret the analysis results
        distress_level, interpretation = interpret_distress(analysis_result)
        
        ctx.logger.info(f"Analysis complete. Distress level: {distress_level}, Interpretation: {interpretation}")
        
        # Send the response back to the sender
        await ctx.send(sender, DistressAnalysisResponse(distress_level=distress_level, interpretation=interpretation))
    except Exception as e:
        ctx.logger.error(f"Error during distress analysis: {str(e)}")
        await ctx.send(sender, DistressAnalysisResponse(distress_level="Error", interpretation=f"Error: {str(e)}"))

# Run the agent
if __name__ == "__main__":
    distress_analyzer.run()



# Function to interpret the prosody result and calculate distress level
def interpret_distress(prosody_result):
    distress_emotions = ['Stress', 'Anxiety', 'Fear', 'Sadness']
    emotion_scores = prosody_result['predictions'][0]['emotions']  # Ensure this path matches Hume's response
    
    distress_level = sum(emotion['score'] for emotion in emotion_scores if emotion['name'] in distress_emotions)
    
    if distress_level < 0.3:
        return "Low distress", "Low levels of distress detected in speech."
    elif distress_level < 0.6:
        return "Moderate distress", "Moderate levels of distress detected in speech."
    else:
        return "High distress", "High levels of distress detected in speech."

# Event handler when the agent starts up
@distress_analyzer.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info(f"distress's address: {ctx.address}")
    await fund_agent_if_low(ctx.wallet.address())
    

# Event handler to process the distress analysis request
@distress_analyzer.on_message(model=DistressAnalysisRequest)
async def handle_distress_analysis(ctx: Context, sender: str, msg: DistressAnalysisRequest):
    ctx.logger.info(f"Received distress analysis request from {sender}")

    try:
        # Record audio based on the request duration
        audio_file = await record_audio(msg.duration)
        
        # Analyze the recorded audio
        analysis_result = await analyze_audio(audio_file)
        ctx.logger.info(f"Raw analysis result: {analysis_result}")
        
        # Interpret the analysis results
        distress_level, interpretation = interpret_distress(analysis_result)
        
        ctx.logger.info(f"Analysis complete. Distress level: {distress_level}, Interpretation: {interpretation}")
        
        # Send the response back to the sender
        await ctx.send(sender, DistressAnalysisResponse(distress_level=distress_level, interpretation=interpretation))
    except Exception as e:
        ctx.logger.error(f"Error during distress analysis: {str(e)}")
        await ctx.send(sender, DistressAnalysisResponse(distress_level="Error", interpretation=f"Error: {str(e)}"))

# Run the agent
if __name__ == "__main__":
    distress_analyzer.run()
