# Voice Transcribe

A high-performance audio transcription service built with Python that implements multiple Voice model strategies for
speech-to-text conversion.

## Overview

Voice Transcribe provides a FastAPI server that exposes endpoints for transcribing audio files and streaming audio
through WebSockets. The project supports multiple Whisper model implementations:

### Currently Implemented
- `whisper` - Original OpenAI Whisper implementation with support for:
  - Multiple model sizes (large-v3, turbo)
  - Real-time transcription via WebSocket
  - WAV file processing (currently using temporary file storage)
  - Language detection

### Future Implementations
- `whisper_cpp` - C++ implementation of OpenAI's Whisper model
- `faster_whisper` - Optimized version of Whisper for improved performance
- `whisperx` - Enhanced Whisper model with additional features
- Enhanced streaming capabilities for lower latency

## Backstory

This project was developed to provide enterprise-grade transcription capabilities in datacenter environments, leveraging
open-source resources rather than relying on proprietary cloud services.

## Features

- FastAPI REST API for audio transcription
- WebSocket support for real-time transcription
- Multiple Whisper model strategies (currently implementing OpenAI Whisper)
- Support for WAV file transcription
- Comprehensive API documentation
- Example code for quick integration
- Language detection and transcription
- Model size selection (large-v3, turbo)

## Requirements

- Python 3.9.6+
- UV package manager
- OpenAI Whisper model files (automatically downloaded on first run)

## Usage

### Development Server

Run the FastAPI development server:

```bash
cd voice_transcribe &&
export PYTHONPATH="$PYTHONPATH:." &&
uvicorn main:create_app --reload
```

### Production Server

Run the FastAPI application with Gunicorn and Uvicorn workers:

```bash
cd voice_transcribe &&
export PYTHONPATH="$PYTHONPATH:." &&
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:create_app
```

### API Endpoints

The API will be available at http://localhost:8000.

- POST `/transcribe` - Transcribe a WAV audio file
- WebSocket `/ws` - Stream audio for real-time transcription
- Swagger `/docs` - Detailed API documentation and examples are available in the `/docs` directory.

## Configuration

The service can be configured using YAML files in the `configs` directory:
- `dev.yaml` - Development environment settings
- `stage.yaml` - Staging environment settings
- `prod.yaml` - Production environment settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0. Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing permissions and limitations under the License.

## Additional Resources

- Medium Blog Post