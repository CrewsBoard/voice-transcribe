# Contributing to Voice Transcribe

Thank you for your interest in contributing to Voice Transcribe! This document provides guidelines and instructions to
help you contribute effectively.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/voice-transcribe.git`
3. Create a branch for your changes: `git checkout -b feature/your-feature-name`

## Development Environment

Set up your development environment:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -e .
```

## Project Structure

The project follows a modular structure:

```
voice_transcribe/
├── configs/           # Configuration files for different environments
├── controllers/       # FastAPI route handlers
├── dtos/             # Data Transfer Objects
├── services/         # Business logic and core functionality
│   ├── core/         # Core services and utilities
│   ├── model/        # Model management and loading
│   ├── transcriber/  # Transcription services
│   └── ws/           # WebSocket services
└── shared/           # Shared utilities and constants
```

## Making Changes

1. Make your changes in your feature branch
2. Follow the project's code style:
   - Use Black for code formatting (line length: 88)
   - Use isort for import sorting
   - Follow PEP 8 guidelines
   - Use type hints for all function parameters and return values
3. Update documentation as needed:
   - Add docstrings for new functions/classes
   - Update README.md if necessary
   - Update CONTRIBUTING.md if you add new guidelines

## Testing

1. Write tests for new functionality
2. Ensure all tests pass:
   ```bash
   pytest
   ```
3. Run type checking:
   ```bash
   mypy .
   ```

## Pull Request Process

1. Update your fork to include the latest changes from the main repo
2. Push your changes to your fork
3. Submit a pull request to the main repository
4. In your PR description, clearly explain:
   - What changes you've made
   - Why you've made them
   - Any issues these changes address
   - How to test the changes

## Model Implementation Guidelines

When implementing new model strategies:

1. Create a new model class in `services/model/`
2. Implement the required interface methods
3. Add the model to `ModelNames` enum in `dtos/models/model_names.py`
4. Update the model service to handle the new model type
5. Add appropriate configuration options in the config files

## WebSocket Implementation Guidelines

When working with WebSocket features:

1. Follow the existing pattern in `services/ws/`
2. Implement proper error handling and connection management
3. Ensure thread safety for concurrent connections
4. Add appropriate logging for debugging

## Code Review

After submitting your PR:

1. Maintainers will review your code
2. Address any requested changes
3. Ensure all CI checks pass
4. Once approved, your changes will be merged

## License

By contributing, you agree that your contributions will be licensed under the project's Apache License 2.0.