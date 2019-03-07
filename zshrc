###############################################################
# PlugIns
###############################################################
# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

POWERLEVEL9K_COLOR_SCHEME='dark'
POWERLEVEL9K_CONTEXT_DEFAULT_BACKGROUND='5'
POWERLEVEL9K_CONTEXT_DEFAULT_FOREGROUND='0'
POWERLEVEL9K_STATUS_OK_BACKGROUND='8'
POWERLEVEL9K_VCS_CLEAN_BACKGROUND='11'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='8'
POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='10'
# User configuration
export ZPLUG_HOME=$HOME/.zplug
if [[ ! -d $ZPLUG_HOME ]];then
    git clone https://github.com/b4b4r07/zplug $ZPLUG_HOME
fi
source $ZPLUG_HOME/init.zsh

zplug "zsh-users/zsh-syntax-highlighting", from:github, defer:3
zplug "lib/git", from:oh-my-zsh

zplug "lib/completion", from:oh-my-zsh
zplug "lib/correction", from:oh-my-zsh
zplug "lib/directories", from:oh-my-zsh
zplug "lib/history", from:oh-my-zsh
zplug "lib/theme-and-appearance", from:oh-my-zsh

# zplug "laurenkt/zsh-vimto"

# zplug "mafredri/zsh-async", from:github, defer:0
# zplug "sindresorhus/pure", use:pure.zsh, from:github, as:theme
zplug "bhilburn/powerlevel9k", use:powerlevel9k.zsh-theme
zplug load
#has to come after zplug
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

###############################################################
# Settings
###############################################################
stty -ixon # Disable ctrl-s and ctrl-q.
# HISTSIZE= HISTFILESIZE= # Infinite history.

[ -f "$HOME/.shortcuts" ] && source "$HOME/.shortcuts" # Load shortcut aliases
[ -f "$HOME/.aliasrc" ] && source "$HOME/.aliasrc"

export CONFIG_DIR=~/.config

# source
alias sz="source ~/.zshrc"
###############################################################
# binding
###############################################################
#vimlike
bindkey -v
bindkey '^P' up-line-or-search
bindkey '^N' down-line-or-search

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

###############################################################
# Custom functions
###############################################################
# # ex - archive extractor
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# preventing nested ranger opening with_$
ranger() {
    if [ -z "$RANGER_LEVEL" ]; then
        /usr/bin/ranger "$@"
    else
        exit
    fi
}

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
###############################################################
# Software settings
###############################################################
export PATH=$PATH::/home/zzz/softwares/node-v6.11.1-linux-x64/bin/
#latex
#export PATH=/usr/local/texlive/2017/bin/x86_64-linux/:$PATH

# added by Anaconda3 4.4.0 installer
#export PATH="/home/zzz/softwares/anaconda3/bin:$PATH"

#java
#export PATH=/home/zzz/softwares/jdk1.8.0_162/bin:$PATH

# clang
export PATH=$PATH:/home/zzz/softwares/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/bin:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/zzz/softwares/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04/lib:

# acplt
export ACPLT_HOME=~/hiwi/ACPLT-DevKit-linux64/acplt
export ACPLT_GIT=$ACPLT_HOME/git
export LD_LIBRARY_PATH=$ACPLT_HOME/system/addonlibs:$ACPLT_HOME/system/syslibs:$LD_LIBRARY_PATH
export PATH=$ACPLT_HOME/system/sysbin:$PATH
