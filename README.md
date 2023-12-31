# "WrapperPythonChatGPT"

This project is a simple wrapper for working with the chatGPT model via API, which can be useful if you are unable to access the model on other devices. Please note that the installation instructions are approximate, as I do not remember every step and relied on logic. Thank you for your understanding!

## System requirements for GPT chat shell:

- Computer with Windows, macOS or Linux operating system;
- Python version 3.6 or higher installed;
- Access to OpenAI API key for authentication and use of GPT model;

## Installation

1. Download the project from this repository:

  `git clone https://github.com/karandashhome/wrapper.git`

2. Open the command line or terminal and go to the project folder

3. Make sure you have the Python version specified in the project requirements installed.

4. Set all required dependencies specified in the requirements.txt file by running the command in the command line:

  `pip install -r requirements.txt`

5. Run data_processing.py

  `python data_processing.py`

9. Run database_setup.py

  `python database_setup.py`

These files contain the code that is used in main.py, so they must be run before it.

10. Run main.py

  `python main.py`
  
#  Remember 
Remember to replace the 'openai.api_key' in the main.py file with your api_key token value. The token value is given when you register on OpenAI. If you haven't registered yet, try to by an account, it's almost free.

