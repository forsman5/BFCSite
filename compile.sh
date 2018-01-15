#!/bin/sh
for file in ./html/*.html; do
    name=$(basename "$file" ".html")
    html-partials-compiler ./html/$name.html > ./dist/$name.html
done

