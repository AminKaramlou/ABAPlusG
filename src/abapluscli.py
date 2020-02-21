import click
import json
from src.aba_plus_g_parse import generate_aba_plus_g_framework_from_file
from src.explanations import get_explanations_json
from src.extensions import get_extensions, dump_extensions

@click.command()
@click.option('--file',
              help='Path to file defining the DSS json data.')


def compute_extensions(file):
    abapf = generate_aba_plus_g_framework_from_file(file)
    extensions = get_extensions(abapf)
    click.echo("--- Framework")
    click.echo("----- Language")
    click.echo(abapf.language)
    click.echo("----- Assumptions")
    click.echo(abapf.assumptions)
    click.echo("----- Rules")
    click.echo(abapf.rules)
    # for rule in abapf.rules:
    #     click.echo("------- rule")
    #     click.echo(rule)
    #     click.echo("---------- body elements")
    #     for b in rule.antecedent:
    #         click.echo(b)
    click.echo("--------------------------Extensions-----------------------")
    click.echo(extensions)
    click.echo("--------------------------Extensions-----------------------")
    dump_extensions(extensions, file)


if __name__ == "__main__":
    compute_extensions()
