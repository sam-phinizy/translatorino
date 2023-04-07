import os
import pathlib

import openai
import typer
from pypdf import PdfReader
from tqdm import tqdm

app = typer.Typer()


@app.command(help="Extract text from a PDF file")
def extract_text(source_file: str, destination_folder: str, split_files: bool = True):
    print(f"Extracting text from {source_file} to {destination_folder}")
    source_file = pathlib.Path(source_file)
    destination_folder = pathlib.Path(destination_folder)

    if not destination_folder.exists() and typer.confirm(
        f"Folder {destination_folder} does not exist. Create it?", abort=True
    ):
        destination_folder.mkdir(parents=True, exist_ok=True)

    pdf_doc = PdfReader(source_file)
    for i, page in enumerate(tqdm(pdf_doc.pages)):
        if split_files:
            with open(f"{destination_folder}/{i}.txt", "w") as f:
                text = page.extract_text()
                f.write(text)
        else:
            with open(f"{destination_folder}/all.txt", "a") as f:
                text = page.extract_text()
                f.write(text)
                f.write(f"\n====={i}=====\n")


@app.command()
def translate(
    source_folder: str,
    destination_folder: str,
    source_language: str,
    target_language: str,
    openai_api_key: str,
    open_ai_organization: str,
    gpt_model: str = "gpt-3.5-turbo",
):
    print(f"Translating {source_folder} from {source_language} to {target_language}")

    openai.organization = os.environ.get("OPENAI_ORGANIZATION", openai_api_key)
    openai.api_key = os.environ.get("OPENAI_API_KEY", open_ai_organization)

    source_folder = pathlib.Path(source_folder)
    destination_folder = pathlib.Path(destination_folder)

    if not destination_folder.exists() and typer.confirm(
            f"Folder {destination_folder} does not exist. Create it?", abort=True
    ):
        destination_folder.mkdir(parents=True, exist_ok=True)


    for file in source_folder.glob("*.txt"):
        if (destination_folder / f"{file.stem}-0.txt").exists():
            print(f"Skipping: {file} already done")
            continue

        text_one = open(file, "r").read()
        try:
            print(f"Translating {file}...")
            translate = openai.ChatCompletion.create(
                model=gpt_model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Translate this from {source_language} to {target_language} and then reformat it:\n{text_one}",
                    }
                ],
            )
        except openai.APIError:
            print(f"Error for {file}")
            continue
        print(f"got translation for {file}")
        for choice in translate["choices"]:
            with open(destination_folder / f"{file.stem}-{choice['index']}.txt", "w") as fp:
                fp.write(choice["message"]["content"])
            print("file written")


if __name__ == "__main__":
    app()
