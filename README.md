# RizzBot - Speech-to-Text Webapp with Conversation Enhancement

## Overview

RizzBot is a Python-based web application that leverages various technologies to transcribe speech to text, display it as a web application using Taipy, and engage in interactive conversations with users using Cohere's conversation enhancement capabilities. This README provides an overview of the project, setup instructions, and usage guidelines.

## Features

- Transcribe speech to text using a speech recognition engine.
- Display transcribed text in a web application using Taipy.
- Engage in interactive and enhanced conversations with users using Cohere.

## Prerequisites

1. Python 3.x: Make sure you have Python 3.x installed. You can download it from the official [Python website](https://www.python.org/).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rizzbot.git
   cd rizzbot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Speech Recognition Engine:
   Configure the speech recognition engine of your choice (e.g., Google Web Speech API) in the code.

2. Taipy Web Application:
   Configure the Taipy web application settings, such as the port and host, in the code.

3. Cohere Conversation Enhancement:
   Obtain the necessary credentials and configure Cohere API integration in the code.

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to the specified host and port (default is `http://localhost:5000`) to access the RizzBot web application.

3. Speak into your microphone to transcribe speech to text and engage in conversations with RizzBot.

## Support and Contributions

If you encounter any issues or have suggestions for improvements, please create a new issue on the GitHub repository. Contributions in the form of pull requests are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---
