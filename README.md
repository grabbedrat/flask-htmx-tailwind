# Flask Tailwind HTMX Project Template

This is a Flask web application utilizing Tailwind CSS for styling and HTMX for dynamic content without writing JavaScript.

# Features

**Flask:** A lightweight WSGI web application framework.

**Tailwind CSS:** A utility-first CSS framework for rapidly building custom designs.

**HTMX:** Allows you to access AJAX, CSS Transitions, WebSockets, and Server Sent Events directly in HTML, making it easy to build modern user interfaces.

# Prerequisites

- Python 3
- Flask
- Access to the internet for CDN resources (Tailwind CSS, HTMX)

# Installation

Clone, Navigate, Create a virtual environment:

```
git clone https://github.com/grabbedrat/flask-htmx-tailwind.git
cd flask-tailwind-htmx
python3 -m venv venv
```

On Windows:

```venv\Scripts\activate```

On MacOS/Linux:

```source venv/bin/activate```

Install Flask:

```pip install Flask```

Install Tailwind CSS:

```npm install -D tailwindcss```
```npx tailwindcss init```
```pip install librosa```
```pip install nvidia-cublas-cu11 nvidia-cudnn-cu11```

```export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'```
```pip install faster-whisper```
```pip install opus-fast-mosestokenizer```
# Running the Application

Start the Flask application:
flask run
Open a web browser and navigate to http://localhost:5000
