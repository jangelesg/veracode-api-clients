set -o vi
export EDITOR=vim
export PATH=$HOME/.local/bin:$PATH
export PS1='$(hostname)($PWD)$ '
. ./.env
