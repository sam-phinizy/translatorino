# translatorino
A quick tool to use openai to translate text.

## Installation 
1. Clone the repo
2. Create a venv: `python -m venv .venv`
3. Activate the venv: `source .venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Set up an openai api account: https://platform.openai.com/account/api-keys
6. You'll need to pass this and your [organization id](https://platform.openai.com/account/org-settings) as environment variables: `OPENAI_API_KEY` and `OPENAI_ORG_ID`
7. Extract the pdf files to text: `python main.py extract-text 'PATH_TO_PDF' 'PATH_TO_OUTPUT'`
8. Translate the text: `python main.py translate 'PATH_TO_TEXT' 'PATH_TO_OUTPUT' source-language target-lang api-key org-id`

