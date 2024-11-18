# Chat Interface

A Streamlit-based chat interface for interacting with an AI model through a REST API.

## Features

- Clean and intuitive chat interface
- Session management
- Persistent chat history
- Easy-to-use sidebar controls
- Error handling and user feedback

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chat-interface.git
cd chat-interface
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your settings:
```bash
cp .env.example .env
```

5. Run the application:
```bash
streamlit run app.py
```

## Configuration

Create a `.env` file with the following variables:
```
API_BASE_URL=http://94.141.99.80:8080
```

## Usage

1. The application will automatically create a new chat session when launched
2. Type your message in the input field at the bottom
3. View the chat history in the main window
4. Use the sidebar to start a new chat session
5. Your session ID is displayed in the sidebar

## API Endpoints

The application interacts with the following API endpoints:

- `GET /newchat` - Create a new chat session
- `POST /chat/:id` - Send a message in an existing session
- `GET /session/:id` - Retrieve session history
- `GET /sessions` - List all sessions