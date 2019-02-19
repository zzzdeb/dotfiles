set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath

let g:python_host_prog = '/usr/bin/python'
let g:python3_host_prog = '/usr/bin/python3'
let g:ruby_host_prog = '/usr/local/bin/neovim-ruby-host'

set clipboard+=unnamedplus

let $NVIM_TUI_ENABLE_TRUE_COLOR=1
"Cursor shape in Insert Mode
let $NVIM_TUI_ENABLE_CURSOR_SHAPE=2

set nocompatible              " be iMproved, required

set nowrap
set linebreak     " when wrapping, wrap at word boundaries (vs last char)
if exists('+breakindent')
  set breakindent " preserves the indent level of wrapped lines
  set showbreak=↪ " illustrate wrapped lines
  set wrap        " wrapping with breakindent is tolerable
endif

set encoding=utf8
set clipboard^=unnamed " This sets the clipboard as the default register. Useful for copy paste from tmux

" cpoptions is a sequence of single-char flags that make Vim do different
" things. The $ flag enables showing a $ marker at the end boundary of cw
set cpoptions+=$

set updatetime=1000
" Switch syntax highlighting on, when the terminal has colors
" Also switch on highlighting the last used search pattern.
if &t_Co > 2 || has("gui_running")
  syntax on
  set hlsearch
endif

" In many terminal emulators the mouse works just fine, thus enable it.
if has('mouse')
  set mouse=a
endif

if has('langmap') && exists('+langnoremap')
  " Prevent that the langmap option applies to characters that result from a
  " mapping.  If unset (default), this may break plugins (but it's backward
  " compatible).
  set langnoremap
endif

" erase everything
set backspace=indent,eol,start


" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Enable file type detection.
  " Use the default filetype settings, so that mail gets 'tw' set to 72,
  " 'cindent' is on in C files, etc.
  " Also load indent files, to automatically do language-dependent indenting.
  filetype plugin indent on

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78
  set colorcolumn=78
  highlight ColorColumn ctermbg=darkgray
  "define BadWhitespace before using in a match
  highlight BadWhitespace ctermbg=red guibg=darkred
  " When editing a file, always jump to the last known cursor position.
  " Don't do it when the position is invalid or when inside an event handler
  " (happens when dropping a file on gvim).
  autocmd BufReadPost *
    \ if line("'\"") >= 1 && line("'\"") <= line("$") |
    \   exe "normal! g`\"" |
    \ endif
  augroup END
else
  set autoindent		" always set autoindenting on
endif " has("autocmd")


" neovim
if !has('nvim')
    set ttymouse=xterm2
endif

"""" START vim-plug Configuration 
if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
" set the runtime path to include Vundle and initialize
set rtp+=~/.local/share/nvim/plugged/vim-plug

" Specify a directory for plugins
call plug#begin('~/.local/share/nvim/plugged')

" let vimplug manage
Plug 'junegunn/vim-plug'

" General
" Plug 'zzzdeb/vim-better-default'
" fancy start
Plug 'mhinz/vim-startify'
Plug 'tpope/vim-sleuth' "autoshiftwidth

Plug 'kana/vim-textobj-user'
Plug 'kana/vim-textobj-entire'
Plug 'kana/vim-textobj-function'
Plug 'idbrii/textobj-word-column.vim'
Plug 'Julian/vim-textobj-variable-segment'

" Plug 'lucapette/vim-textobj-underscore' " variable object handles this
Plug 'jceb/vim-textobj-uri'
" Utility
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'scrooloose/nerdcommenter'
Plug 'majutsushi/tagbar'
Plug 'ervandew/supertab'
Plug 'git://git.wincent.com/command-t.git', {'do': 'cd ruby/command-t/ext/command-t && ruby extconf.rb && make'}
"Plug 'BufOnly.vim'
"Plug 'wesQ3/vim-windowswap'
Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'
"Plug '
"Plug 'junegunn/fzf.vim'
"Plug 'junegunn/fzf'
"Plug 'godlygeek/tabular'
"Plug 'ctrlpvim/ctrlp.vim'
"Plug 'benmills/vimux'
"Plug 'jeetsukumaran/vim-buffergator'
"Plug 'gilsondev/searchtasks.vim'
"Plug 'Shougo/neocomplete.vim'
"Plug 'tpope/vim-dispatch'
" Plug replace with register
Plug 'vim-scripts/ReplaceWithRegister'

Plug 'tpope/vim-surround'
" for easy 
Plug 'tpope/vim-unimpaired'

" Note taking
Plug 'jceb/vim-orgmode'
Plug 'tpope/vim-speeddating'
Plug 'mattn/calendar-vim'
Plug 'dhruvasagar/vim-table-mode'
Plug 'vim-scripts/utl.vim'
" Generic Programming Support
Plug 'Valloric/YouCompleteMe', { 'do': './install.py --all'}

" Git Support
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'gregsexton/gitv'

" C/Cpp
Plug 'rhysd/vim-clang-format'
" test
Plug 'craigemery/vim-autotag'

Plug 'robertbasic/snipbar'

"doesntworsemantichihliht
"Plug 'davits/DyeVim'
Plug 'jaxbot/semantic-highlight.vim'
"c/cpp old
Plug 'justinmk/vim-syntax-extra'

" this Plug stops <c-j>
" Plug 'WolfgangMehner/c-support'
"Plug 'gilligan/vim-lldb'
"Plug 'vim-scripts/indexer.tar.gz'
if has('nvim')
  Plug 'dbgx/lldb.nvim'
endif
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plug 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plug 'ascenator/L9', {'name': 'newL9'}



"Plug 'ap/vim-buftabline'
Plug 'tikhomirov/vim-glsl'

" Themes
Plug 'morhetz/gruvbox'
Plug 'romainl/Apprentice'
Plug 'altercation/vim-colors-solarized'
Plug 'lifepillar/vim-solarized8'

" Automatically sort python imports
Plug 'fisadev/vim-isort'
if has('python')
    " YAPF formatter for Python
    Plug 'pignacio/vim-yapf-format'
endif
"test
Plug 'mileszs/ack.vim'
Plug 'kassio/neoterm'
Plug 'tpope/vim-repeat'
Plug 'vim-scripts/DoxygenToolkit.vim'
"Plug 'jeaye/color_coded'
" old
" Plug replace with register
"Plug 'tpope/vim-rhubarb'
"Plug 'Townk/vim-autoclose'
"Plug 'chaoren/vim-wordmotion'

" test python
Plug 'vim-scripts/indentpython.vim'
" Plug 'w0rp/ale'
Plug 'python-mode/python-mode', { 'branch': 'develop' }
Plug 'ivanov/vim-ipython'
Plug 'Vigemus/iron.nvim'

Plug 'fabi1cazenave/suckless.vim'
Plug 'mboughaba/i3config.vim'
" test spellcheck
" Plug 'kamykn/CCSpellCheck.vim'
" Plug 'dhruvasagar/vim-highlight-word'

" Initialize plugin system
call plug#end()


" Disable file type for vundle
filetype indent off                  " required

"""""""""""""""""""""""""""""""""""""
" Configuration Section
"""""""""""""""""""""""""""""""""""""

" better backup, swap and undos storage
set directory=~/.vim/dirs/tmp     " directory to place swap files in
if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  set undofile		" keep an undo file (undo changes after closing)
endif
set backupdir=~/.vim/dirs/backups " where to put backup files
set undofile                      " persistent undos - undo after you re-open the file
set undodir=~/.vim/dirs/undos
set viminfo+=n~/.vim/dirs/viminfo
" store yankring history file there too
let g:yankring_history_dir = '~/.vim/dirs/'

" create needed directories if they don't exist
if !isdirectory(&backupdir)
    call mkdir(&backupdir, "p")
endif
if !isdirectory(&directory)
    call mkdir(&directory, "p")
endif
if !isdirectory(&undodir)
    call mkdir(&undodir, "p")
endif

set autochdir

set ttimeout
set ttimeoutlen=100

" when scrolling, keep cursor 3 lines away from screen border
set scrolloff=3
set sidescrolloff=5
set sidescroll=1
set display+=lastline " show the last line that fits in window (vs '@@@@')

" Show linenumbers
set number
set relativenumber
set ruler
"search
set hlsearch
set incsearch
set ignorecase
set smartcase

" Set Proper Tabs
set tabstop=2
set softtabstop=2
set shiftwidth=2
set smarttab
set expandtab

" Always display the status line
set laststatus=2
set showcmd
set showtabline=1

set wildmenu
set virtualedit=block,insert,all,onemore
" set digraph
"
set report=0

set winminheight=0
set wildmode=list:longest,full
set wildignore+=*swp,*.class,*.pyc,*.png,*.jpg,*.gif,*.zip
set wildignore+=*/tmp/*,*.o,*.obj,*.so     " Unix
set wildignore+=*\\tmp\\*,*.exe            " Windows

set foldenable
set foldmarker={,}
set foldlevel=0
set foldmethod=marker
" set foldcolumn=3
set foldlevelstart=99

nnoremap <Leader>f0 :set foldlevel=0<CR>
nnoremap <Leader>f1 :set foldlevel=1<CR>
nnoremap <Leader>f2 :set foldlevel=2<CR>
nnoremap <Leader>f3 :set foldlevel=3<CR>
nnoremap <Leader>f4 :set foldlevel=4<CR>
nnoremap <Leader>f5 :set foldlevel=5<CR>
nnoremap <Leader>f6 :set foldlevel=6<CR>
nnoremap <Leader>f7 :set foldlevel=7<CR>
nnoremap <Leader>f8 :set foldlevel=8<CR>
nnoremap <Leader>f9 :set foldlevel=9<CR>

" The semicolon will cause Vim to search back (up) in the directory tree
if has('path_extra')
  setglobal tags-=./tags tags^=./tags;
endif

set autoread

set history=1000

set sessionoptions-=options " exclude options from the :mksession command

" During insert, ctrl-u will break undo sequence then delete all entered chars
" Note that YouCompleteMe breaks this mapping
" https://github.com/Valloric/YouCompleteMe#ctrl-u-in-insert-mode-does-not-work
inoremap <C-U> <C-G>u<C-U>" Enable Elite mode, No ARRRROWWS!!!!

let g:elite_mode=1

" Theme and Styling 
set t_Co=256
set background=light

if (has("termguicolors"))
  set termguicolors
endif

	" Neovim Terminal Colors {{{
" if has("nvim")
  let g:terminal_color_0 = "#000000"
  let g:terminal_color_1 = "#FF5555"
  let g:terminal_color_2 = "#50FA7B"
  let g:terminal_color_3 = "#F1FA8C"
  let g:terminal_color_4 = "#BD93F9"
  let g:terminal_color_5 = "#FF79C6"
  let g:terminal_color_6 = "#8BE9FD"
  let g:terminal_color_7 = "#BFBFBF"
  let g:terminal_color_8 = "#4D4D4D"
  let g:terminal_color_9 = "#FF6E67"
  let g:terminal_color_10 = "#5AF78E"
  let g:terminal_color_11 = "#F4F99D"
  let g:terminal_color_12 = "#CAA9FA"
  let g:terminal_color_13 = "#FF92D0"
  let g:terminal_color_14 = "#9AEDFE"
  let g:terminal_color_15 = "#E6E6E6"
" endif
" }}}
let base16colorspace=256  " Access colors present in 256 colorspace
let g:solarized_termcolors=256
colorscheme solarized8_high
"
"
set textwidth=78
" split
set splitbelow
set splitright
"ask before leaving buffer to save
set confirm
"wraps long lines
set wrap
" Enable highlighting of the current line
set cursorline


if $TERM =~ '^\(rxvt\|screen\|interix\|putty\)\(-.*\)\?$'
    set notermguicolors
elseif $TERM =~ '^\(tmux\|iterm\|vte\|gnome\)\(-.*\)\?$'
    set termguicolors
elseif $TERM =~ '^\(xterm\)\(-.*\)\?$'
    if $XTERM_VERSION != ''
        set termguicolors
    elseif $KONSOLE_PROFILE_NAME != ''
        set termguicolors
    elseif $VTE_VERSION != ''
        set termguicolors
    else
        set notermguicolors
    endif
elseif $TERM =~ '^\(st\)\(-.*\)\?$'
    set termguicolors
elseif $TERM =~ ...
    ... and so forth ...
endif

" -------------------------------------------------------------------------------
"changes cursor color between insert mode and normal mode
if &term =~ "xterm\\|urxvt"
  " use an orange cursor in insert mode
  let &t_SI = "\<Esc>]12;green\x7"
  " use a red cursor otherwise
  let &t_EI = "\<Esc>]12;red\x7"
  silent !echo -ne "\033]12;red\007"
  " reset cursor when vim exits
  autocmd VimLeave * silent !echo -ne "\033]112\007"
  " use \003]12;gray\007 for gnome-terminal and urxvt up to version 9.21
endif

" Stop automatic indentation when copied from another application at insert
" mode
set pastetoggle=<F2>

"external vimrc
set exrc
set secure

" setting indent markers-------------------------------------------------------------------
set list " Show invisible characters
let &listchars = "tab:.,trail:\u2591,extends:>,precedes:<,nbsp:\u00b7"

autocmd FileType html setlocal shiftwidth=4 tabstop=4 softtabstop=4
autocmd FileType htmldjango setlocal shiftwidth=4 tabstop=4 softtabstop=4
autocmd FileType javascript setlocal shiftwidth=4 tabstop=4 softtabstop=4

function! AutoRelativeNumber()
  if &number
    set relativenumber
  endif
endfunction

augroup numbertoggle
 autocmd!
 autocmd BufEnter,FocusGained,InsertLeave * call AutoRelativeNumber()
 autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END
"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" STATUS LINE (won't see much unless we disable Airline)
" see: :help 'statusline
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set statusline=         "reset
" set statusline+=%n      "buffer number
set statusline+=%<      "cut from here if line is too long
" set statusline+=%#number# "set color
set statusline+=[       "open bracket char
set statusline+=./%f    "relative path of the filename
set statusline+=%M      "modifiable/modified flag
set statusline+=%R      "Readonly flag
set statusline+=%W      "Preview window flag
set statusline+=]     "close bracket & reset color
" set statusline+=%*
set statusline+=[%{strlen(&fenc)?&fenc:'wtf-enc'}\| "file encoding
set statusline+=%{&ff}\| "file format
set statusline+=%{strlen(&ft)?&ft:'zomg'}] "file type
set statusline+=%=      "left/right separator
set statusline+=%{fugitive#statusline()}\  "git branch
set statusline+=%c\|     "cursor column
set statusline+=%l/%L   "cursor line/total lines
set statusline+=\ (%P)  "escaped space, percent through file
"""""""""""""""""""""""""""""""""""""
" Plugin config
"""""""""""""""""""""""""""""""""""""
" better default

" Nerd Tree file manager
let g:NERDTreeWinSize=40 
" Nerd Commenter
let g:NERDSpaceDelims = 1
let g:NERDTrimTrailingWhitespace = 1
let g:NERDToggleCheckAllLines = 1

" CommandT
" let g:CommandTTraverseSCM="dir"
let g:CommandTTraverseSCM='pwd'

" Tagbar
let g:tagbar_sort = 0
let g:tagbar_autoshowtag = 1
"let g:tagbar_autopreview = 1
let g:tagbar_autofocus = 1

let g:spacegray_underline_search = 1
let g:spacegray_italicize_comments = 1

" Vim-Supertab Configuration
let g:SuperTabDefaultCompletionType = "<C-X><C-O>"

let g:ycm_key_list_select_completion = ['<C-n>', '<Down>']
let g:ycm_key_list_previous_completion = ['<C-p>', '<Up>']
let g:SuperTabDefaultCompletionType = '<C-n>'

" better key bindings for UltiSnipsExpandTrigger
let g:UltisnipssnippetsDirectories = ['UltiSnips']
let g:UltiSnipsExpandTrigger = "<tab>"
let g:UltiSnipsJumpForwardTrigger = "<tab>"
let g:UltiSnipsJumpBackwardTrigger = "<s-tab>"

" YouCompleteMe
let g:ycm_collect_identifiers_from_tags_files = 1
let g:ycm_seed_identifiers_with_syntax = 1
let g:ycm_always_populate_location_list = 1
" let g:ycm_autoclose_preview_window_after_completion=1
" Ultisnips
let g:UltiSnipsEditSplit = "vertical"


" Clang
let g:clang_format#code_style="llvm"

"Git
"git-gutter
let g:gitgutter_map_keys = 0


" Ack
let g:ackprg = 'ag --skip-vcs-ignore --nogroup --nocolor --column'

" Startify
let g:startify_bookmarks = [{'C': '~/.config/nvim/init.vim'}, 
      \ {'D': '~/hiwi/ACPLT-DevKit-linux64/acplt/dev/'},
      \'~/.zshrc',
      \{'O': '~/Owncloud/Notes/test.org'},
      \{'L': '~/.vim/commandsToLearn.txt'}]
let g:startify_relative_path = 1
let g:startify_change_to_dir = 1
let g:startify_update_oldfiles     = 1
let g:startify_session_autoload    = 0
let g:startify_session_persistence = 1
let g:startify_use_env = 0
let g:startify_session_before_save = [
        \ 'echo "Cleaning up before saving.."',
        \ 'silent! NERDTreeTabsClose'
        \ ]
let g:startify_session_dir = '~/.config/nvim/session'
" suckless 
let g:suckless_mappings = {
\        '<c-[QQf]>'      :   'SetTilingMode("[sdf]")'    ,
\        '<m-[hjkl]>'     :    'SelectWindow("[hjkl]")'   ,
\        '<M-[HJKL]>'     :      'MoveWindow("[hjkl]")'   ,
\      '<C-M-[hjkl]>'     :    'ResizeWindow("[hjkl]")'   ,
\        'v[ov]'       :    'CreateWindow("[sv]")'     ,
\        '<c-w>'          :     'CloseWindow()'           ,
\   'gt[123456789]' :       'SelectTab([123456789])',
\  'Mt[123456789]' : 'MoveWindowToTab([123456789])',
\  'MT[123456789]' : 'CopyWindowToTab([123456789])',
\}

" Pythonmode
let g:pymode_python = 'python3'
let g:pymode = 1
let g:pymode_options = 1
let g:pymode_folding = 1
let g:pymode_run_bind = '<f10>'
let g:pymode_breakpoint_bind = '<f9>'
" let g:pymode_rope = 1
hi Folded guibg=Black
hi Folded guifg=White

" Vimwiki
let g:vimwiki_list = [{'path': '~/Owncloud/Notes'}]
let g:notes_list_bullets=['-','•', '▸', '▹', '▪', '▫']

" Org
let g:org_agenda_files=['~/Owncloud/Notes/test.org']

" Tablemode
let g:table_mode_map_prefix= '<localleader>t'
let g:table_mode_tableize_d_map= '<localleader>T'
" Highlight
" let g:highlight_cursor=1
"""""""""""""""""""""""""""""""""""""
" Custom functions
"""""""""""""""""""""""""""""""""""""
" Convenient command to see the difference between the current buffer and the
" file it was loaded from, thus the changes you made.
" Only define it when not defined already.
if !exists(":DiffOrig")
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis
		  \ | wincmd p | diffthis
endif

command -nargs=0 -bar Update if &modified 
                           \|    if empty(bufname('%'))
                           \|        browse confirm update
                           \|    else
                           \|        confirm update
                           \|    endif
                           \|endif
" highlighting search on enter
let g:highlighting = 0
function! Highlighting()
  if g:highlighting == 1 && @/ =~ '^\\<'.expand('<cword>').'\\>$'
    let g:highlighting = 0
    return ":silent nohlsearch\<CR>"
  endif
  let @/ = '\<'.expand('<cword>').'\>'
  let g:highlighting = 1
  return ":silent set hlsearch\<CR>"
endfunction
" nnoremap <silent> <expr> <c-CR> Highlighting()
let w:windowmaximized = 0
function! MaxRestoreWindow()
	if w:windowmaximized == 1
		let w:windowmaximized = 0
" restore the window
		:winc |
	else
		let w:windowmaximized = 1
		" maximize the window
		:winc =
	endif
endfunction 

"""""""""""""""""""""""""""""""""""""
" Autocommands for filetypes
"""""""""""""""""""""""""""""""""""""
augroup xdefaults 
au BufWritePost .Xdefaults !xrdb ~/.Xdefaults
augroup END

augroup python 
au BufNewFile,BufRead *.py:
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix
    au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
augroup END

augroup cprograms 
  au FileType c.doxygen,cpp nmap <buffer> <leader>i :ClangFormat<cr>
  au FileType c.doxygen,cpp nnoremap <buffer> <Leader>o <s-a>;<return>
  au FileType c.doxygen,cpp imap <buffer> <Leader>o <Esc><Leader>o
augroup END

augroup ovprograms 
  au FileType ovm set tabstop=2
  au FileType ovm set shiftwidth=2
augroup END

augroup json 
  au FileType json nnoremap <buffer> <leader>i :%!python -m json.tool<cr>
augroup END

augroup sh 
  au FileType sh nnoremap <buffer> <leader>i :! bashbeautify %<cr>:e<cr>
  au FileType sh nnoremap <buffer> <c-b> :!bash %<cr>
augroup END

augroup term
  au TermOpen * startinsert
augroup END

"""""""""""""""""""""""""""""""""""""
" Mappings configurationn
"""""""""""""""""""""""""""""""""""""
let mapleader = ","
let maplocalleader =" "
noremap s ;
noremap <s-s> ,

nnoremap <leader>xl :exe getline(".")<cr>
vnoremap <leader>x join(getline("'<","'>"),'<bar>')<cr>

let MYVIMRCTMP="~/.vim/vimrctmp"
" Edit my vimrc file through <leader>ev default leader is 
nmap <leader>ez :vsplit ~/.zshrc<cr>
" Edit my vimrc file through <leader>ev default leader is 
nmap <leader>en :vsplit $MYVIMRC<cr>
nmap <leader>ev :vsplit ~/.vim/vimrc<cr>
nmap <leader>et :vsplit ~/.vim/vimrctmp<cr>
let MYVIMRCTMP="~/.vim/vimrctmp"
" Take the contents of given file and execute it in Vimscript, default $MYVIMRC is ~/.vimrc
nnoremap <leader>sn :source! $MYVIMRC<cr>
nnoremap <leader>sv :source! ~/.vim/vimrc<cr>
nnoremap <leader>st :source ~/.vim/vimrctmp<cr>

nnoremap <leader>ei :vsplit ~/.config/i3/config<cr>

nnoremap <silent> <expr> <leader>/ Highlighting()
let w:windowmaximized = 0
nmap <leader>/ :let @/ = '\<'.expand('<cword>').'\>'<cr>

imap kj <esc>
" make Y behave similarly to D and C
nnoremap Y y$
" map j to gj and k to gk, so line navigation ignores line wrap
" ...but only if the count is undefined (otherwise, things like 4j
" break if wrapped LINES are present)
nmap <expr> j (v:count == 0 ? 'gj' : 'j')
nmap <expr> k (v:count == 0 ? 'gk' : 'k')

" Expand %% into the directory of the current file
cnoremap <expr> %% getcmdtype() == ':' ? expand('%:h').'/' : '%%'

" nnoremap <c-w> :q<cr>
" nnoremap <a-w> <c-w>
nnoremap <a-t> <c-t>
"simulating ctrl
nnoremap <a-j> :join<cr>

" Emacs-like beginning and end of line.
imap <c-e> <c-o>$
imap <c-a> <c-o>^

" Key repeat hack for resizing splits, i.e., <C-w>+++- vs <C-w>+<C-w>+<C-w>-
" see: http://www.vim.org/scripts/script.php?script_id=2223
nmap <a-w>+ <C-w>+<SID>ws
nmap <a-w>- <C-w>-<SID>ws
nmap <a-w>> <C-w>><SID>ws
nmap <a-w>< <C-w><<SID>ws
nnoremap <script> <SID>ws+ <a-w>+<SID>ws
nnoremap <script> <SID>ws- <a-w>-<SID>ws
nnoremap <script> <SID>ws> <a-w>><SID>ws
nnoremap <script> <SID>ws< <a-w><<SID>ws
nmap <SID>ws <Nop>

"clipboard
vnoremap <a-y> "+y
nnoremap <a-y> "+y

nnoremap <f2> :NERDTreeToggle<CR>
nnoremap <f4> :TagbarToggle<CR>

" nnoremap <leader>crl :<c-u>cl<CR>
nnoremap <c-n> :<c-u>bnext<CR>
nnoremap <c-p> :<c-u>bp<CR>

" Preview
nnoremap <a-d> <c-w>}
inoremap <a-d> <esc><c-w>}a

" Functional mapping """""""""""""""""""""""""""""""""""""
" Open
nmap <leader>fc <Plug>(CommandTCommand)
nmap <leader>fl <Plug>(CommandTLine)
nmap <leader>fs <Plug>(CommandTSearch)
nmap <leader>fh <Plug>(CommandTHistory)
nmap <leader>ft <Plug>(CommandTTag)
nmap <silent> <leader>b <Plug>(CommandTMRU)

"function! CtrlPWithSearchText(search_text, ctrlp_command_end)
    "execute ':CtrlP' . a:ctrlp_command_end
    "call feedkeys(a:search_text)
"endfunction
"" same as previous mappings, but calling with current word as default text
"nmap ,wg :call CtrlPWithSearchText(expand('<cword>'), 'BufTag')<CR>
"nmap ,wG :call CtrlPWithSearchText(expand('<cword>'), 'BufTagAll')<CR>
"nmap ,wf :call CtrlPWithSearchText(expand('<cword>'), 'Line')<CR>
"nmap ,we :call CtrlPWithSearchText(expand('<cword>'), '')<CR>
"nmap ,pe :call CtrlPWithSearchText(expand('<cfile>'), '')<CR>
"nmap ,wm :call CtrlPWithSearchText(expand('<cword>'), 'MRUFiles')<CR>
"nmap ,wc :call CtrlPWithSearchText(expand('<cword>'), 'CmdPalette')<CR>
""
" Error
nnoremap <leader>rl :<c-u>cli<CR>
nnoremap <leader>rn :<c-u>cn<CR>
nnoremap <leader>rp :<c-u>cp<CR>
nnoremap <Leader>ri :<C-u>cfir<CR>
nnoremap <Leader>ro :<C-u>cop<CR>
nnoremap <Leader>rc :<C-u>ccl<CR>
nnoremap <Leader>rw :<C-u>cw<CR>

nnoremap <localleader>rl :<c-u>lli<CR>
nnoremap <localleader>rn :<c-u>lne<CR>
nnoremap <localleader>rp :<c-u>lp<CR>
nnoremap <localLeader>ri :<C-u>lfir<CR>
nnoremap <localLeader>ro :<C-u>lop<CR>
nnoremap <localLeader>rc :<C-u>lcl<CR>
nnoremap <localLeader>rw :<C-u>lw<CR>


" Git
" tpope
nnoremap <leader>gdi :Gdiff<cr>
nnoremap <leader>ge :Gedit<cr>
nnoremap <leader>gs :Gstatus<cr>
nnoremap <leader>gb :Gblame<cr>
nnoremap <leader>gdl :Gdelete<cr>
nnoremap <leader>gm :Gmove<cr>
nnoremap <leader>gg :Ggrep<cr>
nnoremap <leader>gl :Glog<cr>
nnoremap <leader>gw :Gwrite<cr>
nnoremap <leader>gr :Gread<cr>
nnoremap <leader>gc :Gcommit<cr>
nnoremap <leader>gps :Gpush<cr>
nnoremap <leader>gpl :Gpull<cr>
" git-gutter
nmap <leader>gh :GitGutterLineHighlightsToggle<cr>
nmap <leader>gf :GitGutterFold<cr>
" gitv
nmap <leader>gv :Gitv<cr> 

" Ycm
map <leader>d  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Ack
nnoremap <leader>a :Ack<cr>
nnoremap <leader>k :Ack 'fix(me)?\|todo'<cr>

" Editor mapping """""""""""""""""""""""""""""""""""""

" nnoremap <c-x> <C-W>c
" Tabs
map <a-s-p> :<c-u>tabp<cr>
map <a-s-n> :<c-u>tabn<cr>
"buffer
map <c-PageDown> :<c-u>tabn<CR>
map <c-PageUp> :<c-u>tabp<CR>
tnoremap <c-PageDown> <C-\><C-N>:<c-u>tabn<CR>
tnoremap <c-PageUp> <C-\><C-N>:<c-u>tabp<CR>
nnoremap <c-t> :<c-u>tabnew<CR>

" press .. for comment using nerd commenter
nnoremap <c-/> <Plug>NERDCommenterToggle
vnoremap <c-/> <Plug>NERDCommenterToggle

" save on c-s
nnoremap <silent> <C-S> :<C-u>Update<CR>
inoremap <silent> <C-S> <ESC>:Update<CR>

" window size toggle
" map <s-w> :call MaxRestoreWindow()<CR>
" Disable arrow movement, resize splits instead.
if get(g:, 'elite_mode')
    nnoremap <Up>    :resize +2<CR>
    nnoremap <Down>  :resize -2<CR>
    nnoremap <Left>  :vertical resize -2<CR>
    nnoremap <Right> :vertical resize +2<CR>
endif

" Easier split navigation
tnoremap <s-space> <C-\><C-N>
tnoremap <c-j> <C-\><C-N><C-w>h
tnoremap <c-k> <C-\><C-N><C-w>j
tnoremap <c-l> <C-\><C-N><C-w>k
tnoremap <c-;> <C-\><C-N><C-w>l
" inoremap <A-h> <C-\><C-N><C-w>h
" inoremap <A-j> <C-\><C-N><C-w>j
" inoremap <A-k> <C-\><C-N><C-w>k
" inoremap <A-l> <C-\><C-N><C-w>l
" nnoremap <c-s-h> <C-w><s-h>
" nnoremap <c-s-j> <C-w><s-j>
" nnoremap <c-s-k> <C-w><s-k>
" nnoremap <c-s-l> <C-w><s-l>
" nnoremap <c-h> <C-w>h
" nnoremap <c-j> <C-w>j
" nnoremap <c-k> <C-w>k
" nnoremap <c-l> <C-w>l

tnoremap <a-x> <C-\><C-N>

nnoremap <silent> vv <c-w>v

"text editing shortcuts
nnoremap <c-a-j> :m +1<CR>
inoremap <c-a-j> <esc>:m +1<CR>i
nnoremap <c-a-k> :m -2<CR>
inoremap <c-a-k> <esc>:m -2<CR>i

" CTRL-U in insert mode deletes a lot.  Use CTRL-G u to first break undo,
" so that you can undo CTRL-U after inserting a line break.
inoremap <C-U> <C-G>u<C-U>
"editing navigation
inoremap <c-h> <c-Left>
inoremap <c-l> <c-Right>
inoremap <a-h> <Left>
inoremap <a-j> <Down>
inoremap <a-l> <Right>
inoremap <a-k> <Up>

" Terminal

" Python
autocmd FileType python nnoremap <LocalLeader>= :0,$!yapf<CR>

" Ultisnips
nmap <leader>eu :UltiSnipsEdit<cr>

" Vim-Notes
augroup notes 
  au FileType notes imap <buffer> <2-LeftMouse> <C-o>:SearchNotes<CR>
  au FileType notes nmap <buffer> <2-LeftMouse> :SearchNotes<CR>
augroup END

" test

"For my life/dev logging purposes

"type nlog followed by space to start new log
iab <expr> nlog strftime("---\n\n%H:%M:%S")

noremap j h
noremap k j
noremap l k
noremap ; l
noremap k gj
noremap l gk
" suckless 
let g:suckless_mappings = {
\        '<c-[QQf]>'      :   'SetTilingMode("[sdf]")'    ,
\        '<c-[jkl;]>'     :    'SelectWindow("[hjkl]")'   ,
\        '<M-[left,down,up,right]>'     :      'MoveWindow("[hjkl]")'   ,
\      '<C-M-[jkl;]>'     :    'ResizeWindow("[hjkl]")'   ,
\        'v[ov]'       :    'CreateWindow("[sv]")'     ,
\        '<c-w>'          :     'CloseWindow()'           ,
\   'gt[123456789]' :       'SelectTab([123456789])',
\  'gT[123456789]' : 'MoveWindowToTab([123456789])',
\  'gTT[123456789]' : 'CopyWindowToTab([123456789])',
\}
nnoremap <c-left> :call MoveWindow("h")<cr>
nnoremap <c-down> :call MoveWindow("j")<cr>
nnoremap <c-up> :call MoveWindow("k")<cr>
nnoremap <c-right> :call MoveWindow("l")<cr>
noremap <a-w> <c-w>

inoremap {<cr> {<cr>}<esc>O
