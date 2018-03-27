SublimeCommandOnSave
====================

Sublime Text 3 plugin which executes given commands on file save

The Sublime Text 2 version of this plugin is available at [ST2-CommandOnSave](https://github.com/klaascuvelier/ST2-CommandOnSave)


Installation
============
The easiest way to install this plugin is via [Sublime Package Control](http://wbond.net/sublime_packages/package_control) by adding an extra repository.

An other way is by cloning this repository into the package folder of Sublime


Usage
=====
This plugin reads commands from the settings file. The commands settings-key is an associative array of paths and their commands. Everytime a file is saved, all commands for every matched path-key is executed.

The path of the file that is being save can get injected into your command with the `_file_` placeholder.

If your command updates the content of the save file, the file will be reloaded in Sublime afterwards (thanks to @evanj).

For more info, see the examples


Examples
========
    {
      "commands": {
        // example 1: project is in folder /Users/klaascuvelier/Projects/example/
        // rsync files to other server on save
        "/Users/klaascuvelier/Projects/example/": [
            "rsync -avz /Users/klaascuvelier/Projects/example/ server@server:/home/server/projects/example/ &"
        ],

        // example 2:
        // just run a bash script on save (you can put much more commands in there)
        "/Users/klaascuvelier/Projects/example2/": [
            "/Users/klaascuvelier/Projects/example2/command.sh &"
        ],

        // example 3:
        // everytime a file is saved, add, commit and push it to git
        "/Users/klaascuvelier/Projects/Sublime3/SublimeCommandOnSave/": [
            "git add -u",
            "git commit",
            "git push"
        ]
      }
    }