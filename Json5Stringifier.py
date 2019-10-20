import sublime
import sublime_plugin

import os
from subprocess import Popen, PIPE, STDOUT

class Json5StringifierCommand (sublime_plugin.TextCommand):
  def run (self, edit):
    view = self.view
    window = view.window()
    window.destroy_output_panel('Json5Stringifier_errOutput')

    region = view.sel()[0]
    if (region.size() == 0):
      region = sublime.Region(0, view.size())
    text = view.substr(region).encode("utf-8")

    pkgDir = os.path.dirname(__file__)
    json5CliPath = os.path.join( pkgDir, 'node_modules', '.bin')
    os.chdir(json5CliPath)

    cmd = Popen(['json5', '-s', '2'], shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    result, err = cmd.communicate(input=text)

    if err:
      outputPanel = window.create_output_panel(pkgName + '_errOutput')
      outputPanel.insert(edit, 0, err.decode("utf-8"))
      window.run_command('show_panel', { 'panel': 'output.Json5Stringifier_errOutput' })
    else:
      outputPanel = window.new_file();
      outputPanel.set_name('output.json')
      outputPanel.assign_syntax('Packages/JavaScript/JSON.sublime-syntax')
      outputPanel.insert(edit, 0, result.decode("utf-8"))
