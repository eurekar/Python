# Install Gitbook


Use gitbook to record, share, and communicate

## Install node.js

* use link https://nodejs.org/en/
* download and install


## Install gitbook
Use windows cmd (run as admin)

* create a directory for gitbook, type ```md gitbook```

* enter the directory, type ```npm gitbook-cli -g```

* then check version ```gitbook -V```

* update 
``` gitbook versions: install latest ```


## Link gitbook and github 



There seem more issues to be studied, such as the import function of github, the offline use of gitbook. I will study them in the future.


## Install disqus for comments

Register at disqus website. Create a new website there with a shortname. Add the disqus plugin to the book.json file, along with the shortname 

Then type

``` {
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "XXXXXXX"
        }
    }
}```



Then run gitbook install to download and install the plugin.

 npm install gitbook-plugin-disqus -g