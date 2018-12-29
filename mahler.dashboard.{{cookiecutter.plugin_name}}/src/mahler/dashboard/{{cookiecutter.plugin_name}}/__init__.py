# -*- coding: utf-8 -*-
"""
:mod:`mahler.dashboard.{{ cookiecutter.plugin_name }} -- {{ cookiecutter.short_description }}
======================={{ '=' * cookiecutter.plugin_name|length }}===={{ '=' * cookiecutter.short_description|length }}

.. module:: {{ cookiecutter.plugin_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
from ._version import get_versions
from .main import main

VERSIONS = get_versions()
del get_versions

__descr__ = '{{ cookiecutter.short_description }}'
__version__ = VERSIONS['version']
__license__ = 'GNU GPLv3'
__author__ = u'{{ cookiecutter.author_name }}'
__author_short__ = u'{{ cookiecutter.author_short }}'
__author_email__ = '{{ cookiecutter.author_email }}'
__copyright__ = u'{{ cookiecutter.copyright }}'
__url__ = 'https://github.com/{{ cookiecutter.github_username }}/mahler.dashboard.{{ cookiecutter.plugin_name }}'


def build_parser(parser):
    """Return the parser that needs to be used for this command"""
    {{ cookiecutter.commandline_name }}_parser = parser.add_parser('{{ cookiecutter.commandline_name }}', help='local help')

    # Add arguments...
    # {{ cookiecutter.commandline_name }}_parser.add_argument(
    #     '--processes', type=int, default=CPU_COUNT,
    #     help='number of concurrent process to spawn. Default: number of CPUs available')

    # Set main function to execute
    {{ cookiecutter.commandline_name }}_parser.set_defaults(func=main)
