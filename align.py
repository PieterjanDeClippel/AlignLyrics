import sys
import json
import subprocess
from aeneas.executetask import ExecuteTask
from aeneas.task import Task

# Replace with your actual YouTube URL
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
audio_file = "audio.mp3"
lyrics_file = "lyrics.txt"
output_file = "timestamps.json"

# 1. Download and extract audio
subprocess.run([
    "yt-dlp", "-x", "--audio-format", "mp3",
    "-o", audio_file,
    youtube_url
], check=True)

# 2. Create and execute Aeneas task
config_string = "task_language=eng|os_task_file_format=json|is_text_type=plain"

task = Task(config_string=config_string)
task.audio_file_path_absolute = audio_file
task.text_file_path_absolute = lyrics_file
task.sync_map_file_path_absolute = output_file

ExecuteTask(task).execute()
task.output_sync_map_file()

print(f"Timestamps written to {output_file}")

# ✅ Print the JSON to the console
with open(output_file, "r", encoding="utf-8") as f:
    print("\n=== TIMESTAMPS ===\n")
    print(f.read())

# docker build -t lyrics-aligner .
# docker run lyrics-aligner