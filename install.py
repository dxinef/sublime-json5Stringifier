import os

pkgName = 'dxinefJson5Stringifier'

def plugin_loaded():
  from package_control import events
  if events.install(pkgName):
    pkgPath = os.path.join( sublime.packages_path(), pkgName)
    os.chdir(path)
    os.system('npm i')
