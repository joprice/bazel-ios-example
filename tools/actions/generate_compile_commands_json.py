#!/usr/bin/python3

# This reads the _compile_command files :generate_compile_commands_action
# generates a outputs a compile_commands.json file at the top of the source
# tree for things like clang-tidy to read.

# Overall usage directions: run bazel with
# --experimental_action_listener=//tools/actions:generate_compile_commands_listener
# for all the files you want to use clang-tidy with and then run this script.
# Afer that, `clang-tidy build_tests/gflags.cc` should work.

import sys
import pathlib
import os.path
import subprocess

'''
Args:
  path: The pathlib.Path to _compile_command file.
  command_directory: The directory commands are run from.

Returns a string to stick in compile_commands.json.
'''
def _get_command(path, command_directory):
  with path.open('r') as f:
    contents = f.read().split('\0')
    command = contents[0].replace('"', '\\"')
    if len(contents) != 2:
      # Old/incomplete file or something; silently ignore it.
      return None
    return '''{
        "directory": "%s",
        "command": "%s",
        "file": "%s"
      },''' % (command_directory, contents[0].replace('"', '\\"'), contents[1])


'''
Args:
  path: A directory pathlib.Path to look for _compile_command files under.
  command_directory: The directory commands are run from.

Yields strings to stick in compile_commands.json.
'''
def _get_compile_commands(path, command_directory):
  for f in path.iterdir():
    if f.is_dir():
      yield from _get_compile_commands(f, command_directory)
    elif f.name.endswith('_compile_command'):
      command = _get_command(f, command_directory)
      if command:
        yield command

def get_bazel_info(key):
    cmd = ['bazel', 'info', key]
    return subprocess.check_output(cmd).decode('utf-8').strip()

def main(argv):
  source_path = os.path.join(os.path.dirname(__file__), '../..')
  action_outs = os.path.join(get_bazel_info('output_path'),
	  'apl-darwin_x86_64-fastbuild/extra_actions',
         'tools/actions/generate_compile_commands_action')
  command_directory = get_bazel_info('execution_root')
  commands = _get_compile_commands(pathlib.Path(action_outs), command_directory)
  with open(os.path.join(source_path, 'compile_commands.json'), 'w') as f:
    f.write('[')
    for command in commands:
      f.write(command)
    #Delete the last comma
    f.seek(f.tell()-1)
    f.write(']')

if __name__ == '__main__':
  sys.exit(main(sys.argv))
