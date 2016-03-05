# dotfiles-manager
Simple dotfile configuration manager.

## Installation
Python version 3+ is required.
The only package required is the Jinja 2 template engine.

```bash
pip install Jinja2
```

## Execution
In order to provide the constants' definitions, define a dictionary in the conf.py file, for instance:

```python
conf = {
    'base00': '#2C3E50',
    'base01': '#34495E',
    'base02': '#7F8C8D',
    'base03': '#95A5A6',
    ...
}
```

This dictionary will replace the entries `base00` with `#2C3E50`, `base01` with `#34495E`, and so on, in every single template declared. This allows you to have multiple definitions of the same color in multiple files that can be simultaneously changed.

In order to define define all your templates, use the [Jinja2 templating syntax](http://jinja.pocoo.org/docs/dev/templates/). It might look rather intimidating, but you'll most likely never use all of the functions described. In most situations, all you want to do is to declare simple variables in your templates, like so:

.i3/i3config
```
...
client.focused          {{base00}} {{base01}} {{base02}} {{base03}}
client.focused_inactive {{base00}} {{base01}} {{base02}} {{base03}} 
client.unfocused        {{base00}} {{base01}} {{base02}} {{base03}}
client.urgent           {{base00}} {{base01}} {{base02}} {{base03}}
...
```

.Xresources
```
...
*.color0:       {{base00}}
*.color1:       {{base01}}
*.color2:       {{base02}}
*.color3:       {{base03}}
...
```

By default, **dotfiles-manager** will look for templates in the `templates` directory. However, you can choose a different directory with the `-d` option, like `python dotfiles_manager.py -d other_directory`.

Finally, the rendered templates will be written in the `output` directory. You can also change this directory with the `-o` option, like `python dotfiles_manager.py -o other_directory`. The output directory will keep the same directory hierarchy defined in the templates directory.

The exemplified process will then result in the following outputs:

.i3/i3config
```
...
client.focused          #2C3E50 #34495E #7F8C8D #95A5A6
client.focused_inactive #2C3E50 #34495E #7F8C8D #95A5A6 
client.unfocused        #2C3E50 #34495E #7F8C8D #95A5A6
client.urgent           #2C3E50 #34495E #7F8C8D #95A5A6
...
```

.Xresources
```
...
*.color0:       #2C3E50
*.color1:       #34495E
*.color2:       #7F8C8D
*.color3:       #95A5A6
...
```
