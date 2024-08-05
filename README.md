# WhatsApp Chat Analyzer

Try it - https://whatsapp-chat-stats-analyse.streamlit.app

A web application to analyze WhatsApp chat logs for various metrics and insights.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Neerabh/whatsapp-chat-analyzer.git
   
2. Navigate to the project directory:
   cd whatsapp-chat-analyzer

3. Create a virtual environment (optional but recommended):
   python -m venv venv

4. Activate the virtual environment:
   On Windows:
      venv\Scripts\activate
  
   On macOS/Linux:
      source venv/bin/activate

5. Install the dependencies:
   pip install -r requirements.txt

Usage
1. Prepare your WhatsApp chat log and place it in the data directory.
2. Run the application:
      streamlit run app.py


Caution: Regex Pattern for Chat Parsing
Please note that the regex pattern used for parsing chat data in this project has certain limitations and may not handle all edge cases perfectly. While it works for most standard WhatsApp chat exports, the following points should be kept in mind:

Chat Format Variations: WhatsApp chat exports may vary depending on the version of the app and the operating system. Ensure your chat data follows the standard format that the regex pattern expects.

Date and Time Formats: The regex pattern is designed to work with a specific date and time format. If your chat data uses a different format, you might need to adjust the pattern accordingly.

Before running the analysis, it's recommended to review a sample of your chat data to ensure compatibility with the regex pattern. If you encounter issues, you may need to modify the pattern in preprocessor.py to better suit your data.
