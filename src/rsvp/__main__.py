import click

@click.group()
def cli():
    pass

keywords_option = click.option(
    "-w", "--keywords", "keywords",
    default=None,
    #prompt="Keywords, comma-separated",
    type=str,
    help="Comma-separated list of keywords to change.")

# config_filename_option = click.option(
#     "-c", "--config", "config_filename",
#     default=USER_CONFIG_FILENAME,
#     type=click.Path(exists=True, file_okay=True, dir_okay=False),
#     help="Kaomoji database file name.")

@cli.command()
def rsvp(keywords):
    print(keywords)

if __name__ == "__main__":
    cli()