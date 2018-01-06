#!/bin/sh

files="ConvertCase.py
ConvertCase.sublime-commands"

package_name="ConvertCase"
packages_dir=~/Library/Application\ Support/Sublime\ Text\ 3/Packages

if [ ! -d "$packages_dir" ]; then
  echo "Can't find Sublime Text packages directory. Expected it to be at:"
  echo "$packages_dir"
  exit 1
fi

mkdir -p "$packages_dir/$package_name"
for file in $files; do
  cp "$file" "$packages_dir/$package_name/"
done
