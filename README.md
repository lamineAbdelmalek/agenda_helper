#  Agenda-helper

##  Description
Agenda helper is an LLM powered tool allowing you to query your personal google calendar agenda using natural language.

##  Features
- ✅ Check availibilities in your agenda
- ✅ Book events in your agenda

![Screenshot](https://i.imgur.com/gLe2o33.png)

##  Tech Stack
- **Programming Language:** Python
- **Frameworks & Libraries:** LangChain, OpenAI


##  Installation & Setup
1. **Get your google calendar API access**
- Go to https://console.cloud.google.com/
- Create a new project
- Navigate to API & Services > Library and enable the Google Calendar API
- Go to API & Services > Credentials:
    - Click Create Credentials > OAuth client ID.
    - Choose Desktop App as the application type.
    - Download the credentials.json file.
- Add your email as an approved tester in the OAuth Consent screen

2. **Get your OpenAI API key**
- Replace the file .env-example with a .env file and put your OpenAI API key in it   
3.  **Clone the repository**
   ```bash
   git clone https://github.com/lamineAbdelmalek/agenda_helper.git
   cd agenda_helper
```
   To run the project localy:
  ```bash
  poetry install
  streamlit run agenda_helper/app.py --server.port=8580 --server.address=0.0.0.0
```
  To run the project via docker:
  ```bash
    docker build . -t agenda_helper
    docker run --env-file .env -p 8580:8580 agenda_helper
```
  
  
