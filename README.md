# Voice Activity Detection (VAD) System

## Overview

The Voice Activity Detection (VAD) System is a Flask web application designed to monitor audio input and detect excessive speech activity in real time. It raises warnings based on predefined thresholds, making it suitable for applications like online proctoring and monitoring speech levels during events.

## Features

- **Real-time Voice Activity Detection**: Continuously monitors audio input and identifies speech activity.
- **Warning System**: Issues warnings when speech levels exceed a specified threshold.
- **User-friendly Interface**: A simple web interface for interaction.
- **Deployment**: Hosted on PythonAnywhere, accessible via a live link.

## Live Demo

You can access the live application at: [Voice Activity Detection System](https://chiragtiwari6842.pythonanywhere.com/)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
    ```bash
    pip install -r requirements.txt

## Usage

1. Run the Flask application:
    ```bash
    python vad_app.py

2. Open your web browser and navigate to http://127.0.0.1:5000 to access the app.


  # Project Structure
   ```bash
   /mysite
   ├── vad_app.py        # Main Flask application
   ├── templates         # HTML templates
   │   └── index.html    # Main page for the application
   ├── static            # Static files (CSS, JS, images)
   ├── requirements.txt   # Python dependencies
   └── README.md          # Project documentation

# Technologies Used

- **Python**: Programming language for backend development.
- **Flask**: Web framework for creating the web application.
- **NumPy**: Library for numerical computations, used for processing audio data.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Chirag Tiwari**
