# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

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

stty -ixon # Disable ctrl-s and ctrl-q.

# HISTSIZE= HISTFILESIZE= # Infinite history.

[ -f "$HOME/.shortcuts" ] && source "$HOME/.shortcuts" # Load shortcut aliases
[ -f "$HOME/.aliasrc" ] && source "$HOME/.aliasrc"

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

#has to come after zplug
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
