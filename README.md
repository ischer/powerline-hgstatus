Powerline Hgstatus
===================

A simple [Powerline][1] segment for showing the status of a Mercurial working copy.

By [Ian Scherer][2].

Glossary
--------
- ``: branch name or commit hash
- `!`: missing files
- `✖`: removed files
- `●`: changed files
- `✚`: added files
- `…`: untracked files

Requirements
------------

The Hgstatus segment requires [hg][5].

Installation
------------

Installing the Hgstatus segment can be done with pip:

```txt
pip install powerline-hgstatus
```

The Hgstatus segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme,
for example in `.config/powerline/colorschemes/default.json`:

```json
{
	"groups": {
		"hgstatus":                 { "fg": "gray8",           "bg": "gray1", "attrs": [] },
		"hgstatus_branch":          { "fg": "gray9",           "bg": "gray1", "attrs": [] },
		"hgstatus_branch_clean":    { "fg": "gray9",           "bg": "gray1", "attrs": [] },
		"hgstatus_branch_dirty":    { "fg": "mediumorange",    "bg": "gray1", "attrs": [] },
		"hgstatus_missing":         { "fg": "brightred",       "bg": "gray1", "attrs": [] },
		"hgstatus_removed":         { "fg": "brightred",       "bg": "gray1", "attrs": [] },
		"hgstatus_modified":        { "fg": "green",           "bg": "gray1", "attrs": [] },
		"hgstatus_added":           { "fg": "darkgreen",       "bg": "gray1", "attrs": [] },
		"hgstatus_untracked":       { "fg": "brightestorange", "bg": "gray1", "attrs": [] },
		"hgstatus:divider":         { "fg": "gray5",           "bg": "gray1", "attrs": [] }
	}
}
```

Then you can activate the Hgstatus segment by adding it to your segment configuration,
for example in `.config/powerline/themes/shell/default.json`:

```json
{
    "function": "powerline_hgstatus.hgstatus",
    "priority": 40
}
```

Special Thanks
--------------

Jasper N. Brouwer for [powerline-gitstatus][3]

Shrey Banga for [powerline-shell][4]

License
-------

Licensed under [the MIT License][6].

[1]: https://powerline.readthedocs.org/en/master/
[2]: https://github.com/ischer
[3]: https://github.com/jaspernbrouwer/powerline-gitstatus
[4]: https://github.com/banga/powerline-shell
[5]: https://www.mercurial-scm.org/
[6]: https://github.com/ischer/powerline-hgstatus/blob/master/LICENSE
