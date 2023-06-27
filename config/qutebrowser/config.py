import subprocess
import os
USER = os.environ['USER']
HOME = os.environ['HOME']
DIRMODUS=''
try:
    DIRMODUS = os.environ['DIRMODUS']
except KeyError:
    pass

ENVMODE=''
try:
    ENVMODE = os.environ['ENVMODE']
except KeyError:
    pass

TERMINAL='st'
try:
    TERMINAL = os.environ['TERMINAL']
except KeyError:
    pass


# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Config
#  config.source('shortcuts.py')
#Theme
config.source('themes/base16-qutebrowser/themes/minimal/base16-dracula.config.py')
c.colors.webpage.bg = 'white'
c.colors.statusbar.insert.bg = 'darkgreen'
c.colors.statusbar.caret.bg = 'purple'
c.colors.statusbar.caret.selection.bg = 'purple'
#  c.colors.tabs.selected.even.bg = '#194d19'
c.colors.tabs.selected.even.bg = 'blue'
c.colors.tabs.selected.odd.bg = c.colors.tabs.selected.even.bg
c.fonts.default_size = '15pt'
c.zoom.default = '125%'

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

c.content.blocking.enabled = True
c.content.blocking.whitelist = ["thepiratebay.org"]

c.url.start_pages = ["https://duckduckgo.com"]

#Bindings
# Unbind shite defaults
config.unbind('q')
#  config.unbind('z')
config.unbind('<Ctrl-v>')

config.bind('<ctrl-o>', 'tab-focus stack-prev')
config.bind('<ctrl-i>', 'tab-focus stack-next')
# X configs change options / QB features
config.bind('xc', 'config-cycle tabs.show always never')
config.bind('xx', 'set tabs.show always;; later 5000 set tabs.show switching')
config.bind('xg', 'tab-give')
config.bind('xb', 'config-cycle statusbar.hide')
config.bind('xh', 'config-cycle content.user_stylesheets /home/hexdsl/.config/qutebrowser/styles/solarized-dark-all-sites.css ""')
config.bind('xs', 'spawn --userscript tts.py replay')
config.bind('B', 'set-cmd-text -s :bookmark-load')
config.bind('sc', 'config-source')


config.bind('<ctrl-t>', 'yank -s --quiet selection;; open -t {primary}')
config.bind(',tt', 'spawn --userscript translate.py auto en')
config.bind(',tk', 'spawn --userscript translate.py auto ko')
config.bind(',tj', 'spawn --userscript translate.py auto ja')
config.bind(',td', 'spawn --userscript translate.py auto de')
config.bind(',tt', 'spawn --userscript translate.py auto en', mode='caret')
config.bind(',tk', 'spawn --userscript translate.py auto ko', mode='caret')
config.bind(',tj', 'spawn --userscript translate.py auto ja', mode='caret')
config.bind(',td', 'spawn --userscript translate.py auto de', mode='caret')
# configs are for downloading videos and music
config.bind(',yD', 'hint links spawn yt "{hint-url}"')
config.bind(',ym', "spawn ytDownload m '{url}'")
#  config.bind('zp', 'hint links spawn ~/.bin/ytdlp {hint-url} ~/Downloads/qbdownloads')
config.bind(',yv', 'spawn ytDownload v "{url}"')

# Ctrl shortcuts run scripts / applications
config.bind(',m', 'spawn --detach mpv --force-window=immediate {url}')
config.bind(',M', 'hint links spawn --detach mpv --force-window=immediate {hint-url}')
config.bind(',r', 'spawn --userscript readability')


config.bind('d', 'scroll-page 0 0.3')
config.bind('u', 'scroll-page 0 -0.5')


config.bind('q', 'tab-close')

config.bind(',b', 'set-cmd-text -s :tab-select')

config.bind('T', 'config-cycle tabs.width 35 400')

c.tabs.width = 35
#  c.tabs.position = 'left'
c.tabs.close_mouse_button = "right"

# search engine shortneners
c.url.searchengines = {
"DEFAULT": "https://www.google.de/search?&q={}",
"!g": "https://www.google.de/search?&q={}",
"!w": "http://www.wikiwand.com/en/{}",
"!d": "https://duckduckgo.com/?q={}",
"!aur": "https://aur.archlinux.org/packages/?O=0&K={}",
"!arch": "https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}",
"!gt":
    "https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text={}",
"!dic": "http://www.dictionary.com/browse/{}",
"!urban": "http://www.urbandictionary.com/define.php?term={}",
"!yt": "https://www.youtube.com/results?search_query={}",
"!maps": "https://www.google.com/maps/place/{}",
"!sp": "https://www.startpage.com/do/dsearch?query={}",
"!pirate": "https://www.pirate-bay.net/search?q={}",
"!torrent": "https://www.pirate-bay.net/search?q={}",
}
if ENVMODE == 'indurad':
    c.url.searchengines.update({
        "g": "https://git.indurad.x/search?utf8=%E2%9C%93&search={}&group_id=&project_id=&snippets=false&repository_ref=&nav_source=navbar",
        "w": "https://wiki.indurad.x/foswiki/bin/view/Main/WebSearch?search={}&scope=all&web=Main",
        "j": "https://jenkins.indurad.x/search/?q={}&Jenkins-Crumb=8bfe1ab4d1d762edca143d9a7be37aae752c17de126e62349d4a2d2604993772",
    })


#Test
config.bind('<Ctrl-m>', "prompt-yank -s;;spawn uget-gtk --quiet --folder=Downloads '{primary}';;mode-enter normal", mode='prompt')
config.bind('<Ctrl-shift-m>', "prompt-yank -s;;spawn uget-gtk '{primary}';;mode-enter normal", mode='prompt')

config.bind('gd', 'spawn uget-gtk')

c.fileselect.handler = 'external'
c.fileselect.folder.command = [TERMINAL, '-e', 'ranger', '--choosedir={}']
c.fileselect.single_file.command = [TERMINAL, '-e', 'ranger', '--choosefile={}']
c.fileselect.multiple_files.command = [TERMINAL, '-e', 'ranger', '--choosefiles={}']

config.bind('gD', 'spawn st -e ranger --cmd="chain set sort=atime ; set sort_directories_first=false" {}/Downloads'.format(HOME))
config.bind('<ctrl-b>', "set-cmd-text -s :quickmark-add {url}")
config.bind('<ctrl-shift-j>', "tab-focus 1")

config.bind('za', 'config-cycle content.blocking.enabled')
config.bind('zt', 'config-cycle tabs.position left top')
config.bind('zb', 'config-cycle tabs.show switching always;;config-cycle statusbar.hide')

config.bind('zl', 'spawn --userscript qute-pass')
config.bind('zul', 'spawn --userscript qute-pass --username-only')
config.bind('zpl', 'spawn --userscript qute-pass --password-only')

config.bind('zol', 'spawn --userscript qute-pass --otp-only')


try:
    from qutebrowser.api import message

    config.source('pyconfig/redirectors.py')
except ImportError:
    pass


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
c.hints.selectors["*"]= [
    "*",
]
c.hints.selectors["div"] = [
    "div",
]
c.hints.selectors["ad"] = [
    "a.pull-right > span.glyphicons-remove",
]

if DIRMODUS == 'jkl;':
    config.bind('<ctrl-j>', 'back')
    config.bind('<ctrl-k>', 'tab-next')
    config.bind('<ctrl-l>', 'tab-prev')
    config.bind('<ctrl-;>', 'forward')

    config.bind('<ctrl-shift-k>', "tab-move +")
    config.bind('<ctrl-shift-l>', "tab-move -")

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

    config.unbind('h')
    #  config.unbind('hy')
    config.bind('ha','hint * userscript copy_selected.py')
    config.bind('hI','hint images tab')
    config.bind('hO','hint links fill :open -t -r {hint-url}')
    config.bind('hR','hint --rapid links window')
    config.bind('hY','hint links yank-primary')
    config.bind('hb','hint all tab-bg')
    config.bind('hc','hint code userscript copy_selected.py')
    config.bind('hd','hint all delete')
    config.bind('hf','hint iframe fill :open -t {hint-url}')
    config.bind('hh','hint all hover')
    config.bind('hi','hint images')
    config.bind('ho','hint links fill :open {hint-url}')
    config.bind('hr','hint --rapid links tab-bg')
    config.bind('hs','hint div userscript tts.py')
    config.bind('ht','hint all userscript translate.py')
    config.bind('hv','hint video yank')
    config.bind('hyy','hint links yank')
    config.bind('hyd','hint div userscript copy_selected.py')


config.source('custom_config.py')


# jblock
#  import sys, os

#  sys.path.append(os.path.join(sys.path[0], "jblock"))
#  config.source("jblock/jblock/integrations/qutebrowser.py")
#  config.set(
    #  "content.blocking.lists",
    #  [
        #  "https://easylist.to/easylist/easylist.txt",
        #  "https://easylist.to/easylist/easyprivacy.txt",
        #  "https://easylist.to/easylist/fanboy-annoyance.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
        #  "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
        #  "https://www.malwaredomainlist.com/hostslist/hosts.txt",
        #  "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext",
    #  ],
#  )

