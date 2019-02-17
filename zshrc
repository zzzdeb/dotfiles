# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH=/home/zzz/.dotfiles/oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="gnzh"

# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
# plugins=(
  # git
  # zsh-autosuggestions
  # python
  # zsh-syntax-highlighting
# )
# must come before sourcing zsh
# source "$HOME/.homesick/repos/homeshick/homeshick.sh"
# fpath=($HOME/.homesick/repos/homeshick/completions $fpath)

source $ZSH/oh-my-zsh.sh

# User configuration
export ZPLUG_HOME=$HOME/.zplug
if [[ ! -d $ZPLUG_HOME ]];then
    git clone https://github.com/b4b4r07/zplug $ZPLUG_HOME
fi
source $ZPLUG_HOME/init.zsh

zplug "zsh-users/zsh-syntax-highlighting", from:github, defer:3
zplug "plugins/git", from:oh-my-zsh
zplug "laurenkt/zsh-vimto"

zplug load
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
 if [[ -n $SSH_CONNECTION ]]; then
   export EDITOR='nvim'
 else
   export EDITOR='nvim'
#export EDITOR='mvim'
 fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"

export MYVIMRCTMP="~/.vim/vimrctmp"

export CONFIG_DIR=~/.config

#vimlike
bindkey -v
bindkey '^P' up-line-or-search
bindkey '^N' down-line-or-search
bindkey '^R' history-incremental-pattern-search-backward

#
bindkey -M vicmd "j" vi-backward-char
bindkey -M vicmd "k" down-line-or-history
bindkey -M vicmd "l" up-line-or-history
bindkey -M vicmd ";" vi-forward-char
bindkey -M vicmd "s" vi-repeat-find
bindkey -M vicmd "S" vi-rev-repeat-find

bindkey -M visual "j" vi-backward-char
bindkey -M visual "k" down-line
bindkey -M visual "l" up-line
bindkey -M visual ";" vi-forward-char

export PATH=$PATH::/home/zzz/softwares/node-v6.11.1-linux-x64/bin/

. ~/softwares/fromsource/devel/setup.zsh
#latex
#export PATH=/usr/local/texlive/2017/bin/x86_64-linux/:$PATH

# added by Anaconda3 4.4.0 installer
#export PATH="/home/zzz/softwares/anaconda3/bin:$PATH"



#export CWD="/home/zzz/hiwi/ACPLT-DevKit-linux64"
#export IFBS_HOME=$CWD/clients/iFBSpro
#export ACPLT_HOME=$CWD/acplt
#export PATH=$CWD/acplt/system/sysbin:$PATH
#export LD_LIBRARY_PATH=$CWD/acplt/system/addonlibs:$CWD/acplt/system/syslibs:$LD_LIBRARY_PATH
#export PATH=/home/zzz/hiwi/ACPLT-DevKit-linux64:/home/zzz/softwares/jdk1.8.0_162/bin:/home/zzz/hiwi/ACPLT-DevKit-linux64/acplt/system/sysbin:/home/zzz/softwares/anaconda3/bin:/opt/ros/kinetic/bin:/home/zzz/bin:/home/zzz/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/zzz/softwares/node-v6.11.1-linux-x64/bin/

export PATH=/home/zzz/hiwi/ACPLT-DevKit-linux64:$PATH
#export UBUNTU_MENUPROXY=0

#java
#export PATH=/home/zzz/softwares/jdk1.8.0_162/bin:$PATH

# Sets the Mail Environment Variable
MAIL=/var/spool/mail/zzz && export MAIL
#export XDG_CONFIG_HOME=~/.config/

# zsh
alias vim="stty stop '' -ixoff ; vim"
# `Frozing' tty, so after any command terminal settings will be restored
ttyctl -f
export PATH=$PATH:/home/zzz/softwares/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/bin:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/zzz/softwares/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/lib:

# acplt
export ACPLT_HOME=~/hiwi/ACPLT-DevKit-linux64/acplt
export ACPLT_GIT=$ACPLT_HOME/git
export LD_LIBRARY_PATH=$ACPLT_HOME/system/addonlibs:$ACPLT_HOME/system/syslibs:$LD_LIBRARY_PATH
export PATH=$ACPLT_HOME/system/sysbin:$PATH

alias vim=echo
alias glac=gcalcli
alias gcal=gcalcli
alias vi=nvim
alias ra=ranger

alias suai='sudo apt install'
alias suar='sudo apt remove'
alias suau='sudo apt update'
alias suaU='sudo apt upgrade'

# export TERM=xterm-256color
alias cdd='cd ~/Downloads'
alias cdhd='$ACPLT_HOME/dev'
alias py3=python3
source ~/.shortcuts
alias sz="source ~/.zshrc"

alias mv='mv -i'
alias cp='cp -i'
alias open=xdg-open

# preventing nested ranger opening with_$
ranger() {
    if [ -z "$RANGER_LEVEL" ]; then
        ${HOME}/.local/bin/ranger "$@"
    else
        exit
    fi
}


alias cd..="cd .."
alias cd...="cd ../.."
alias cd....="cd ../../.."

# Create a directory and cd into it
mcd() {
    mkdir "${1}" && cd "${1}"
}

# Jump to directory containing file
jump() {
    cd "$(dirname ${1})"
}

# Execute a command in a specific directory
xin() {
    (
        cd "${1}" && shift && ${@}
    )
}
# Mirror a website
alias mirrorsite='wget -m -k -K -E -e robots=off'
# Mirror stdout to stderr, useful for seeing data going through a pipe
alias peek='tee >(cat 1>&2)'
export TERMINAL=st


  #Scripts for life logging
 alias today='zsh ~/.dotfiles/scripts/open_logs_today.sh'

#has to come after zplug
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
alias nb="nvim -c 'set nonumber' -c 'set norelativenumber' -c 'set laststatus=0' term://newsboat"

export BROWSER='qutebrowser'
