import sublime
import sublime_plugin
import subprocess


class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('CommandOnSave.sublime-settings')
        commands = settings.get('commands')
        file = view.file_name()

        if not commands == None:
            for entry in commands:
                path, cmd = entry.split('::', 1)
                if file.startswith(path) and len(cmd) > 0:
                    p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
                    out, err = p.communicate()
                    print ("Command on Save:\n" + out.decode('utf-8'))