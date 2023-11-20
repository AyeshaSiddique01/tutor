from tutor import hooks as tutor_hooks

from . import cmd

from .__about__ import __version__

# pylint: disable=c-extension-no-member
tutor_hooks.Filters.CLI_COMMANDS.add_item(cmd.license_command)
