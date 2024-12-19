if:

    Git error - gpg failed to sign data

then:
    https://stackoverflow.com/questions/41052538/git-error-gpg-failed-to-sign-data
    git config --global user.signingkey ${ssid}


if:
    pass too slow
then: 
    local/share/gnupg/gnu-agent pinentry
    remove ~/.gnupg
