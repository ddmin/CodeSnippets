#!/bin/bash
# COPYLOCAL: automatically move dotfiles from ~/ to this repository

DOTDIR="./dotfiles"
SCRIPTDIR="./scripts"
CONFIGDIR="./config"

echo "============== DOTFILES =============="
echo Copying zsh aliases
    cp ~/.aliases "$DOTDIR/aliases"

echo Copying zshrc
    cp ~/.zshrc "$DOTDIR/zshrc"

echo Copying profile
    cp ~/.profile "$DOTDIR/profile"

echo Copying gitconfig
    cp ~/.gitconfig "$DOTDIR/gitconfig"

echo Copying vimrc
    cp ~/.vimrc "$DOTDIR/vimrc"

echo Copying init.vim
    cp ~/.config/nvim/init.vim "$DOTDIR/init.vim"

echo DONE

# copy scripts from ~/Code/Bash

echo "============== SCRIPTS =============="
echo "Copying scripts from ~/Code/Bash."
cp -a ~/Code/Bash/* "$SCRIPTDIR/."
echo DONE

# copy configs
echo "============== CONFIGS =============="
echo "Copying configs from ~/.config"

# program directories
dirs=("feh" "kitty" "lazygit" "mpd" "ncmpcpp" "neofetch" "ranger" "rofi" "zathura")

# loop through directories
for d in ${dirs[@]}; do
    mkdir -p "$CONFIGDIR/$d"
    echo "Copying $d"
    cp -r "$HOME/.config/$d/"/* "$CONFIGDIR/$d/."
done
echo DONE
