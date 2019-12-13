export LANG="en_US.UTF-8"
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
# POWERLEVEL9K_MODE='awesome-fontconfig'
POWERLEVEL9K_MODE='nerdfont-complete'
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(vi_mode status root_indicator background_jobs)
# User configuration
# load zgen
if [[ ! -f "${HOME}/.zgen/zgen.zsh" ]];then
     git clone https://github.com/b4b4r07/zplug $ZPLUG_HOME
fi
source "${HOME}/.zgen/zgen.zsh"

# if the init scipt doesn't exist
if ! zgen saved; then
    echo "Creating a zgen save"

    zgen oh-my-zsh

    # plugins
    zgen oh-my-zsh plugins/git
    zgen oh-my-zsh plugins/vi-mode
    zgen load laurenkt/zsh-vimto
    zgen oh-my-zsh plugins/extract
    # zgen oh-my-zsh plugins/command-not-found
    zgen load zsh-users/zsh-syntax-highlighting

    # bulk load
    # zgen loadall <<EOPLUGINS
        # zsh-users/zsh-history-substring-search
        # /path/to/local/plugin
# EOPLUGINS
    # ^ can't indent this EOPLUGINS

    # completions
    zgen load zsh-users/zsh-completions src

    # theme
    # zgen oh-my-zsh themes/arrow
    zgen load bhilburn/powerlevel9k powerlevel9k

    # save all to init script
    zgen save
fi

#has to come after zplug
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

###############################################################
# Settings
###############################################################
stty -ixon # Disable ctrl-s and ctrl-q.
# HISTSIZE= HISTFILESIZE= # Infinite history.

[ -f "$HOME/.shortcuts" ] && source "$HOME/.shortcuts" # Load shortcut aliases
[ -f "$HOME/.config/aliasrc" ] && source "$HOME/.config/aliasrc"

export CONFIG_DIR=~/.config

# source
alias sz="source ~/.zshrc"
###############################################################
# binding
###############################################################
#vimlike
# bindkey -v
# set show-mode-in-prompt on
# bindkey '^P' up-line-or-search
# bindkey '^N' down-line-or-search
set -s escape-time 0
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
