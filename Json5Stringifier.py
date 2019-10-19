import sublime
import sublime_plugin

import os
from subprocess import Popen, PIPE, STDOUT

class Json5StringifierCommand (sublime_plugin.TextCommand):
  def run (self, edit):
    pkgName = 'dxinefJson5Stringifier'

    view = self.view
    window = view.window()
    window.destroy_output_panel(pkgName + '_errOutput')
    # 获取选择区域的文字内容。如没有选区，默认为全文
    region = view.sel()[0]
    if (region.size() == 0):
      region = sublime.Region(0, view.size())
    text = view.substr(region).encode("utf-8")
    # 发送到shell命令
    pkgPath = os.path.join( sublime.packages_path(), pkgName, 'node_modules', '.bin')
    os.chdir(pkgPath)
    cmd = Popen(['json5', '-s', '2'], shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    result, err = cmd.communicate(input=text)

    if err:
      outputPanel = window.create_output_panel(pkgName + '_errOutput')
      outputPanel.insert(edit, 0, err.decode("utf-8"))
      window.run_command('show_panel', { 'panel': 'output.' + pkgName + '_errOutput' })
    else:
      outputPanel = window.new_file();
      outputPanel.set_name('output.json')
      outputPanel.assign_syntax('Packages/JavaScript/JSON.sublime-syntax')
      outputPanel.insert(edit, 0, result.decode("utf-8"))


