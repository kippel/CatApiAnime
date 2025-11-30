import typer

from app.seed.dev_app import dev_app

app = typer.Typer()

@app.command()
def dev():
    dev_app()
    
if __name__ == "__main__":
    app()
