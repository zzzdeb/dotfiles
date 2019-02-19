import subprocess

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Padding (in pixels) for tab indicators.
# Type: Padding
#  c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg
#  c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg

#  c.tabs.indicator.padding = {'bottom': 1, 'left': 0, 'right': 4, 'top': 2}
# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.auto_save.session = True

# Bindings for normal mode
config.bind(',m', 'spawn mpv {url}')
config.source('shortcuts.py')
#  config.source('solarized.py')

config.bind('<z><l>', 'spawn --userscript qute-pass')
config.bind('<z><u><l>', 'spawn --userscript qute-pass --username-only')
config.bind('<z><p><l>', 'spawn --userscript qute-pass --password-only')
config.bind('<z><o><l>', 'spawn --userscript qute-pass --otp-only')

config.bind('d', 'scroll-page 0 0.3')
config.bind('u', 'scroll-page 0 -0.5')

config.bind('<ctrl-j>', 'back')
config.bind('<ctrl-k>', 'tab-next')
config.bind('<ctrl-l>', 'tab-prev')
config.bind('<ctrl-;>', 'forward')
config.bind('J', 'back')
config.bind('K', 'tab-next')
config.bind('L', 'tab-prev')
config.bind('j', 'scroll left')
config.bind('k', 'scroll down')
config.bind('l', 'scroll up')
config.bind(';', 'scroll right')

config.bind('T', 'config-cycle tabs.width 40 400')

c.tabs.width = 40
c.tabs.position = 'left'
c.tabs.close_mouse_button = "right"

# search engine shortneners
c.url.searchengines = {
"DEFAULT": "https://duckduckgo.com/?q={}",
"g": "https://www.google.de/search?&q={}",
"w": "https://en.wikipedia.org/w/index.php?search={}",
"steam": "http://store.steampowered.com/search/?term={}",
"ddg": "https://duckduckgo.com/?q={}",
"aur": "https://aur.archlinux.org/packages/?O=0&K={}",
"arch": "https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}",
"imdb": "http://www.imdb.com/find?ref_=nv_sr_fn&s=all&q={}",
"dic": "http://www.dictionary.com/browse/{}",
"ety": "http://www.etymonline.com/index.php?allowed_in_frame=0&search={}",
"urban": "http://www.urbandictionary.com/define.php?term={}",
"yt": "https://www.youtube.com/results?search_query={}",
"ddgi": "https://duckduckgo.com/?q={}&iar=images",
"lutris": "https://lutris.net/games/?q={}",
"deal": "https://isthereanydeal.com/search/?q={}",
"gog": "https://www.gog.com/games?sort=popularity&search={}&page=1",
"proton": "https://www.protondb.com/search?q={}",
"qwant": "https://www.qwant.com/?q={}",
"sp": "https://www.startpage.com/do/dsearch?query={}",
"itch": "https://itch.io/search?q={}"}

#Theme
config.source('themes/nord-qutebrowser/nord-qutebrowser.py')
#  import themes.dracula.draw

#  themes.dracula.draw.blood(c, {
    #  'spacing': {
        #  'vertical': 6,
        #  'horizontal': 8
    #  },
    #  'font': {
        #  'family': 'Menlo, Terminus, Monaco, Monospace',
        #  'size': 10
    #  }
#  })
