# BFCSite
Development location for website for Buckeye Fencing Club.

Currently, the website is managed by the two webmasters of the fencing club: Zach Allegretti (snackking) and Joe Forsman (forsman5).

It is now hosted using Amazon's S3, Route 53, and Cloudfront services, at www.osufencingclub.org.

Once the next webmaster is elected, this repo and the DNS name will be passed on, but another hosting solution should be found.

## Compilation and Other Upkeeps

The html folder contains the source code for the website. This includes references to partials and such.
Partials are used to create the code to be uploaded to the static site, these are stored in the partials folder.

These are managed by html-partials-compiler, a simple plugin. https://github.com/Tecktron/html-partials-compiler

Running compile.sh will output the production code to the dist folder. This is the final html that should be hosted.

### For Future Webmasters
Requirements: Node Package Manager (NPM). Run npm install in order to get all dependencies.
              Python 3.0 or higher, on your path (run python on your command window anywhere to verify).

The way it works, in short, is that the html source files (in html folder) use the <! partial > tag to include partials.
When a run option is included in this, a python script is called, and then html-partials-compiler grabs the output to std-out
and then takes that as the partial. This is how one partial can be used for every image, for example - the python script
grabs every image and re-prints the partial as many times as needed.
