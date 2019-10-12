import subprocess

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Config
config.source('shortcuts.py')
# c.? are options set at launch.
c.auto_save.session = True
c.tabs.favicons.scale = 1
c.tabs.position = "top"
#  c.tabs.show = "switching"
c.content.cookies.accept = 'all'
c.content.geolocation = 'ask'
c.content.webgl = True
c.editor.command = ["st", '-e', 'nvim',  '{file}']
c.scrolling.smooth = True
c.confirm_quit =['multiple-tabs', 'downloads']
c.session.lazy_restore = True

c.content.host_blocking.enabled = True
c.content.host_blocking.lists.append("http://sbc.io/hosts/hosts")
c.content.host_blocking.whitelist = ["thepiratebay.org"]

c.url.start_pages = ["https://duckduckgo.com"]

#Bindings
# Unbind shite defaults
config.unbind('q')
#  config.unbind('z')
config.unbind('<Ctrl-v>')

# X configs change options / QB features
config.bind('xc', 'config-cycle tabs.show always never')
config.bind('xx', 'set tabs.show always;; later 5000 set tabs.show switching')
config.bind('xg', 'tab-give')
config.bind('xb', 'config-cycle statusbar.hide')
config.bind('xh', 'config-cycle content.user_stylesheets /home/hexdsl/.config/qutebrowser/styles/solarized-dark-all-sites.css ""')
config.bind('xs', 'spawn --userscript tts.py replay')
config.bind('B', 'set-cmd-text -s :bookmark-load')
config.bind('sc', 'config-source')


# configs are for downloading videos and music
config.bind('zy', 'hint links spawn ~/.bin/ytdv {hint-url}')
#  config.bind('zp', 'hint links spawn ~/.bin/ytdlp {hint-url} ~/Downloads/qbdownloads')
config.bind('zv', 'spawn ~/.bin/ytdv {url}')
config.bind('qr', 'spawn ~/.bin/qr {url}')

# Ctrl shortcuts run scripts / applications
config.bind(',m', 'spawn --detach mpv --force-window yes {url}')
config.bind(',M', 'hint links spawn --detach mpv --force-window yes {hint-url}')
config.bind(',r', 'spawn --userscript readability')


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
config.bind('J', 'scroll left', mode='caret')
config.bind('K', 'scroll down', mode='caret')
config.bind('L', 'scroll up', mode='caret')
config.bind(':', 'scroll right', mode='caret')
config.bind('j', 'move-to-prev-char', mode='caret')
config.bind('k', 'move-to-next-line', mode='caret')
config.bind('l', 'move-to-prev-line', mode='caret')
config.bind(';', 'move-to-next-char', mode='caret')

config.bind('q', 'tab-close')

config.bind(',b', 'set-cmd-text -s :buffer')

config.bind('T', 'config-cycle tabs.width 35 400')

c.tabs.width = 35
#  c.tabs.position = 'left'
c.tabs.close_mouse_button = "right"

# search engine shortneners
c.url.searchengines = {
"DEFAULT": "https://duckduckgo.com/?q={}",
"!g": "https://www.google.de/search?&q={}",
"!w": "https://en.wikipedia.org/w/index.php?search={}",
"!steam": "http://store.steampowered.com/search/?term={}",
"!ddg": "https://duckduckgo.com/?q={}",
"!aur": "https://aur.archlinux.org/packages/?O=0&K={}",
"!arch": "https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}",
"!imdb": "http://www.imdb.com/find?ref_=nv_sr_fn&s=all&q={}",
"!dic": "http://www.dictionary.com/browse/{}",
"!ety": "http://www.etymonline.com/index.php?allowed_in_frame=0&search={}",
"!urban": "http://www.urbandictionary.com/define.php?term={}",
"!yt": "https://www.youtube.com/results?search_query={}",
"!ddgi": "https://duckduckgo.com/?q={}&iar=images",
"!lutris": "https://lutris.net/games/?q={}",
"!deal": "https://isthereanydeal.com/search/?q={}",
"!gog": "https://www.gog.com/games?sort=popularity&search={}&page=1",
"!proton": "https://www.protondb.com/search?q={}",
"!qwant": "https://www.qwant.com/?q={}",
"!sp": "https://www.startpage.com/do/dsearch?query={}",
"!itch": "https://itch.io/search?q={}"}

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


#Test
config.bind('<Ctrl-m>', "prompt-yank -s;;spawn uget-gtk --quiet --folder=Downloads '{primary}';;enter-mode normal", mode='prompt')
config.bind('<Ctrl-shift-m>', "prompt-yank -s;;spawn uget-gtk '{primary}';;enter-mode normal", mode='prompt')

config.bind(',yd', "spawn ytMusic '{url}'")
config.bind('gd', 'spawn uget-gtk')
config.bind('gD', 'spawn st -e ranger /home/zzz/Downloads')
config.bind('<ctrl-b>', "set-cmd-text -s :quickmark-add {url}")
config.bind('<ctrl-shift-j>', "tab-focus 1")
config.bind('<ctrl-shift-k>', "tab-move +")
config.bind('<ctrl-shift-l>', "tab-move -")

config.bind('za', 'config-cycle content.host_blocking.enabled')
config.bind('zt', 'config-cycle tabs.position left top')
config.bind('zl', 'spawn --userscript qute-pass')
config.bind('zb', 'config-cycle tabs.show switching always;;config-cycle statusbar.hide')
config.bind('zul', 'spawn --userscript qute-pass --username-only')
config.bind('zpl', 'spawn --userscript qute-pass --password-only')
config.bind('zol', 'spawn --userscript qute-pass --otp-only')

try:
    from qutebrowser.api import message

    config.source('qutenyan/nyan.py')
    config.source('pyconfig/redirectors.py')
except ImportError:
    pass

config.unbind('h')
config.bind('hI','hint images tab')
config.bind('hO','hint links fill :open -t -r {hint-url}')
config.bind('hR','hint --rapid links window')
config.bind('hY','hint links yank-primary')
config.bind('hb','hint all tab-bg')
config.bind('hc','hint code userscript code_select.py')
config.bind('hd','hint all delete')
config.bind('hf','hint iframe fill :open -t {hint-url}')
config.bind('hh','hint all hover')
config.bind('hi','hint images')
config.bind('ho','hint links fill :open {hint-url}')
config.bind('hr','hint --rapid links tab-bg')
config.bind('hs','hint div userscript tts.py')
config.bind('ht','hint inputs')
config.bind('hv','hint video yank')
config.bind('hy','hint links yank')

c.hints.selectors["code"] = [
    # Selects all code tags whose direct parent is not a pre tag
    ":not(pre) > code",
    "pre"
]

c.hints.selectors["video"] = [
    "video",
]

c.hints.selectors["iframe"] = [
    "iframe",
]
c.hints.selectors["*"] = [
    "*",
]
c.hints.selectors["div"] = [
    "div",
]
#colours
#  c.colors.completion.fg = "#ffffff"
#  c.colors.completion.even.bg = "#262626"
#  c.colors.completion.odd.bg = "#000000"
#  c.colors.completion.category.fg = "#ffffff"
#  c.colors.completion.category.bg = "#000000"
#  c.colors.completion.category.border.top = "#8c8c8c"
#  c.colors.completion.item.selected.fg = "#ffffff"
#  c.colors.completion.item.selected.bg = "#cc00cc"
#  c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.bg
#  c.colors.completion.item.selected.border.bottom = c.colors.completion.category.border.top
#  c.colors.completion.match.fg = "#ccb3ff"
#  c.colors.statusbar.insert.bg = "#cc0099"
#  c.colors.tabs.odd.fg = "#ffffff"
#  c.colors.tabs.odd.bg = "#000000"
#  c.colors.tabs.even.fg = c.colors.tabs.odd.fg
#  c.colors.tabs.even.bg = c.colors.tabs.odd.bg
#  c.colors.tabs.selected.odd.bg = "#cc00cc"
#  c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg
#  c.colors.tabs.bar.bg = "#000000"
#  c.hints.border = "#000000"
#  c.colors.hints.fg = "#cc00cc"
#  c.colors.hints.bg = "#000000"
#  c.colors.hints.match.fg = "#ffffff"
#  c.colors.downloads.bar.bg = "#000000"

