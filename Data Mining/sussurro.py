import subprocess

filename = "Data Mining\Varys and Littlefinger.wav"
model_name = "base"
subprocess.run(
  [
    "whisper",
    "--language", "en",
    "--word_timestamps", "True",
    "--model", model_name,
    "--output_dir", f"output-{model_name}",
    filename
  ]
)