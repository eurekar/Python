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


update 2/22/2016: it seems all are ready without the offline use of gitbook. Just follow the [help](https://help.gitbook.com/github/index.html)


There seem more issues to be studied, such as the import function of github, the offline use of gitbook. I will study them in the future.


## Install disqus for comments

Register at disqus website. Create a new website there with a shortname. Add the disqus plugin to the book.json file, along with the shortname 

Then type

    {
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "XXXXXXX"
            }
        }
    }



Then run gitbook install to download and install the plugin.

    npm install gitbook-plugin-disqus -g
 
 
 ## Install other plugin or theme
 
### Example: GitBook Plugin - MaXiang Theme

需要gitbook2.0以上版本. 这是基于www.maxiang.info(马克飞象)站点的gitbook主题插件，

在此主题的基础上添加了目录导航功能，自动抓取h2标签，就是markdown中的##二级标题

安装使用:   ```npm install gitbook-plugin-maxiang```

在使用gitbook项目的根路径中book.json, 添加内容如下：

    {
    "plugins": [
            "maxiang"
        ]
    }
 
 