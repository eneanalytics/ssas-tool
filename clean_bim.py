import typer
import json

from pathlib import Path


def clean_ssas_model_bim(
    model_file_path: Path = typer.Argument(
        ..., help="The full path to the Model.bim file"
    ),
    model_file_output_path: Path = typer.Argument(
        ..., help="The full path to where you want to store the processed file"
    ),
    rename_tables: bool = typer.Option(
        False,
        help="If you want to rename tables. It may mean that you have to reprocess them in SSAS",
    ),
):
    """
    Clean your SSAS model file from all uppercase column names that often is the result of
    reading data from a database such as Snowflake.
    Input the path to the Model.bim file in the MODEL_FILE_PATH argument and then the path to the output
    file in the MODEL_FILE_OUTPUT_PATH argument. I.e.

    python clean_bim.py Model.bim Model_clean.bim

    """

    try:
        with open(model_file_path) as model_file:
            model = json.load(model_file)

        for table in model["model"]["tables"]:
            if rename_tables:
                # Set table name
                if table["name"].isupper():
                    table["name"] = table["name"].lower().capitalize().replace("_", " ")

            # Set column name
            for column in table["columns"]:
                if column["name"].isupper():
                    column["name"] = (
                        column["name"].lower().capitalize().replace("_", " ")
                    )

        with open(model_file_output_path, "w") as outfile:
            outfile.write(json.dumps(model))

        print(
            f"Successfully cleaned {model_file_path} and stored in {model_file_output_path}"
        )

    except Exception as e:
        print(e)


if __name__ == "__main__":
    typer.run(clean_ssas_model_bim)
