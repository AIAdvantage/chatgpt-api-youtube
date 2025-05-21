# ChatGPT API Scripts

This repository contains a few small scripts showing how to interact with the OpenAI ChatGPT API.

## Files

- **01 chatgpt simple** – Minimal example for sending a single prompt.
- **02 chatgpt chat assistant copy.py** – Simple command line chat assistant. Now supports optional voice input using the `speech_recognition` package.
- **03 chatgpt chat assistant website.py** – Demonstrates a basic Gradio web interface.

## Voice Input

The chat assistant script (`02 chatgpt chat assistant copy.py`) can accept microphone input if the
`speech_recognition` package and a compatible audio backend such as `pyaudio` are installed.
If the package is not available or voice input is skipped, the script falls back to text input.

```bash
pip install SpeechRecognition pyaudio
python  "02 chatgpt chat assistant copy.py"
```


