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
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv context dir vcs)
# User configuration
# Load zgen only if a user types a zgen command
export ZGEN_DIR=${HOME}/.config/zsh/.zgen
zgen () {
  if [[ ! -s ${ZGEN_DIR}/zgen.zsh ]]; then
    git clone --recursive https://github.com/tarjoilija/zgen.git ${ZGEN_DIR}
  fi
  source ${ZGEN_DIR}/zgen.zsh
  zgen "$@"
}

# if the init scipt doesn't exist
if ! zgen saved; then
    echo "Creating a zgen save"

    zgen oh-my-zsh

    # plugins
    # zgen oh-my-zsh plugins/git
    zgen oh-my-zsh plugins/vi-mode
    zgen load laurenkt/zsh-vimto
    zgen oh-my-zsh plugins/extract
    zgen oh-my-zsh plugins/virtualenv
    zgen oh-my-zsh plugins/virtualenvwrapper
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
    # zgen load bhilburn/powerlevel9k powerlevel9k
    zgen load romkatv/powerlevel10k powerlevel9k

    # save all to init script
    zgen save
    zcompile ${ZGEN_DIR}/init.zsh
fi

#has to come after zplug
[ -f "${XDG_CONFIG_HOME:-$HOME/.config}"/fzf/fzf.zsh ] && source "${XDG_CONFIG_HOME:-$HOME/.config}"/fzf/fzf.zsh

###############################################################
# Settings
###############################################################
stty -ixon # Disable ctrl-s and ctrl-q.
# HISTSIZE= HISTFILESIZE= # Infinite history.

[ -f "$XDG_CONFIG_HOME/shortcutrc" ] && source "$XDG_CONFIG_HOME/shortcutrc" # Load shortcut aliases
[ -f "$XDG_CONFIG_HOME/aliasrc" ] && source "$XDG_CONFIG_HOME/aliasrc"

bindkey -M vicmd "s" vi-repeat-find
bindkey -M vicmd "S" vi-rev-repeat-find

export DIRMODUS='jkl;'
if [[ "$DIRMODUS" == 'jkl;' ]]; then
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

  bindkey -M visual "j" vi-backward-char
  bindkey -M visual "k" down-line
  bindkey -M visual "l" up-line
  bindkey -M visual ";" vi-forward-char
fi

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


###############################################################
# Software settings
###############################################################
#latex
#export PATH=/usr/local/texlive/2017/bin/x86_64-linux/:$PATH

#java
#export PATH=/home/zzz/softwares/jdk1.8.0_162/bin:$PATH

[ -f "${XDG_CONFIG_HOME:-$HOME/.config}"/fzf/fzf.zsh ] && source "${XDG_CONFIG_HOME:-$HOME/.config}"/fzf/fzf.zsh

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
