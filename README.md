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

## Help text

```text
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  extract-text  Extract text from a PDF file
  translate
```

```text
Usage: main.py extract-text [OPTIONS] SOURCE_FILE DESTINATION_FOLDER

  Extract text from a PDF file

Arguments:
  SOURCE_FILE         [required]
  DESTINATION_FOLDER  [required]

Options:
  --split-files / --no-split-files
                                  [default: split-files]
  --help                          Show this message and exit.

```

```text
Usage: main.py translate [OPTIONS] SOURCE_FOLDER DESTINATION_FOLDER
                         SOURCE_LANGUAGE TARGET_LANGUAGE OPENAI_API_KEY
                         OPEN_AI_ORGANIZATION

Arguments:
  SOURCE_FOLDER         [required]
  DESTINATION_FOLDER    [required]
  SOURCE_LANGUAGE       [required]
  TARGET_LANGUAGE       [required]
  OPENAI_API_KEY        [required]
  OPEN_AI_ORGANIZATION  [required]

Options:
  --gpt-model TEXT  [default: gpt-3.5-turbo]
  --help            Show this message and exit.
```