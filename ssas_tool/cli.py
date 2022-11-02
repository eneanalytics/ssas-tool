import typer
from pathlib import Path

from ssas_tool.ssas_utils import clean_ssas_model_bim


app = typer.Typer()


@app.command()
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
    Clean ssas model.bim
    """
    clean_ssas_model_bim(
        model_file_path,
        model_file_output_path,
        rename_tables
    )
