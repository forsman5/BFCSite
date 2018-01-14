# BFCSite
Development location for website for Buckeye Fencing Club.

Currently, the website is managed by the two webmasters of the fencing club: Zach Allegretti and Joe Forsman.

It will soon be hosted using Amazon's Static Web Sites service and their DNS provider.
This will remove any cost from the club, as well as simplify the process and allow the site
to be hosted sooner, but it is not a solution that will last forever.

Thus, once the next webmaster is elected, this repo and the DNS name will be passed on, but another hosting solution should be found.

## Compilation and Other Upkeeps

The html folder contains the source code for the website. This includes references to partials and such.

These are managed by html-partials-compiler, a simple plugin. https://github.com/Tecktron/html-partials-compiler

Running compile.sh will output the production code to the dist folder. This is the final html that should be hosted.
