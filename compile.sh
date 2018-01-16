#!/bin/sh
for file in ./html/*.html; do
    name=$(basename "$file" ".html")
    html-partials-compiler ./html/$name.html > ./docs/$name.html
done

cd docs
rm -r resources
cd ..
cp -r resources docs/resources
