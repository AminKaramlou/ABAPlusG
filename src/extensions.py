import json
import os
from src.labelling_algorithms import construct_grounded_labelling


def construct_grounded_extension(framework):
    '''
    :param framework: An ABAPlusG framework.
    :return: A grounded extension of framework.
    '''
    grounded_labelling = construct_grounded_labelling(framework)
    extension = frozenset({a for a, label in grounded_labelling.items() if label == Label.IN})
    return extension


def get_extensions(framework):
    preferred_extensions = framework.get_preferred_extensions()
    set_stable_extensions = framework.get_set_stable_extensions()
    grounded_extension = construct_grounded_extension(framework)
    extensions = {
        'Preferred': preferred_extensions, 'Set-stable': set_stable_extensions, 'Grounded': grounded_extension
        }

    return extensions


def dump_extensions(extensions, filename):
    output_file = f"{os.path.splitext(filename)[0] + '_extensions' + '.json'}"
    with open(output_file, 'w') as file:
        json.dump(extensions, file, cls=SetEncoder, indent=4)
    file.close()

    return print(f"Extensions recorded in {output_file}.")


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (set, frozenset)):
            return list(obj)
        return json.JSONEncoder.default(self, obj)