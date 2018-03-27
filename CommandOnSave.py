import os
import sublime
import sublime_plugin
import subprocess


_STATUS_KEY = 'CommandOnSave'

class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        settings = sublime.load_settings('CommandOnSave.sublime-settings').get('commands')
        if settings is None:
            return

        file = view.file_name()
        before_stat = None

        view.erase_status(_STATUS_KEY)
        for path, commands in settings.items():
            if file.startswith(path):
                for command in commands:
                    # record the mtime so we can check if we need to reload the file
                    if before_stat is None:
                        before_stat = os.stat(file)

                    command = re.sub(
                        r"\b_file_\b",
                        file,
                        command
                    )
                    
                    process = subprocess.Popen(command,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    output = process.stdout.read()
                    code = process.wait()
                    if code != 0:
                        view.set_status(_STATUS_KEY, 'ERROR: Command failed: %s' % (
                            ' '.join(command)))
                        print('CommandOnSave %s failed code %d; output: %s' % (
                            ' '.join(command), code, output))
                        # attempt to execute any other commands

        if before_stat is not None and not view.is_dirty():
            after_stat = os.stat(file)
            if before_stat.st_mtime != after_stat.st_mtime:
                # it seems like the file changed: reload the view
                view.run_command('revert')
