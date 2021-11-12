from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen"),
    Key([mod], "j", 
        lazy.layout.left(),
        lazy.layout.previous().when(layout='stack'),
        desc="Move focus to left"),
    Key([mod], "semicolon", 
        lazy.layout.right(),
        lazy.layout.next().when(layout='stack'),
        desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.next_screen(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_left(),
        lazy.layout.client_to_previous().when(layout='stack'),
        desc="Move window to the left"),
    Key([mod, "shift"], "semicolon", 
        lazy.layout.shuffle_right(),
        lazy.layout.client_to_next().when(layout='stack'),
        desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([mod], "b",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
]

groups = [Group(i) for i in "234780"]
groups_short="weruip"

#  def to_group_screen(group):
  #  def callback(qtile):
    #  if group.name == "0":
      #  qtile.cmd_to_screen(1)
    #  qtile.current_screen.toggle_group(group.name)

    #  windows = windows_matching_shuffle(qtile, **kwargs)
    #  if windows:
        #  window = windows[0]
        #  if window.group != qtile.current_group:
            #  if window.group.screen:
                #  qtile.cmd_to_screen(window.group.screen.index)
            #  qtile.current_screen.set_group(window.group)
        #  window.group.focus(window, False)

  #  return lazy.function(callback)


for i, k in zip(groups, groups_short):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], k, lazy.group[i.name].toscreen(toggle=False),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], k, lazy.window.togroup(i.name),
           desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack='#BD93F9'),
    layout.Stack(num_stacks=1, border_focus='#BD93F9', border_width=2),
    layout.Stack(num_stacks=2, border_focus='#BD93F9', border_width=2),
    layout.Stack(num_stacks=3, border_focus='#BD93F9', border_width=2),
    layout.Bsp(),
    layout.Tile(),
]

widget_defaults = dict(
    font='sans',
    fontsize=20,
    padding=3,
)

extension_defaults = widget_defaults.copy()
fake_screens = [
  Screen(
      bottom=bar.Bar(
          [
              widget.Prompt(),
              widget.Sep(),
              widget.WindowName(),
              widget.Sep(),
              widget.Systray(),
              widget.Sep(),
              widget.Volume(),
              widget.Sep(),
              widget.Clock(format='%H:%M:%S %d.%m.%Y')
          ],
          40,
          background="#282828"
      ),
      right=bar.Gap(5),
      x=0,
      y=0,
      width=2060,
      height=1440
  ),
  Screen(
      bottom=bar.Bar(
          [
              widget.GroupBox(),
              widget.WindowName(),
              widget.Clock()
          ],
          40,
      ),
      left=bar.Gap(5),
      x=2060,
      y=0,
      width=1380,
      height=1440
  ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
