# Install Ipython 2/21

Type in the command line: ```python -m pip install ipython```

* Not sure how to open it...
* Enter C:\phtyon27\Script and type ```ipython```


# Start using ipython


[A short intro](http://www.pythonforbeginners.com/basics/ipython-a-short-introduction)


* To use ipython for different projects

Make an ipython shortcut in each of your project directories. For example if you have a new project in C:\fake\example\directory, then right click on the shortcut's icon and "Edit Properties."

Set the shortcut's "start in"=the directory of your project. Every time you open the shortcut, the default directory is your project's directory.

* You can use any editor, which is separated from your ipython shell.


# Windows Powershell?


# Install Anaconda on Sublime Text 3
http://damnwidget.github.io/anaconda/

After installation, use control+b to build python files.


# Setup Python scientific stack

SciPy: modules for scientific computing


> python -m pip install scipy

NumPy: support for multidimensional arrays


> python -m pip install numpy

pandas: time series library

matplotlib:plotting library

scikit-learn: machine learning


# Read remote data

install pandas-datareader

Read end-of-day history from Yahoo Finance 

> from pandas_datareader.data import DataReader
> 
> ticker = 'SPY'
> 
> source = 'yahoo'
> 
> start = '01/01/2012'
> 
> end = '03/22/2014'
> 
> qt_spy = DataReader(ticker, source, start, end) 
> 
> print qt_spy.head() 
> 
> print qt_spy.tail()
> qt_spy.to_csv('C:\Users\mih\Documents\Learn_coding') 

Read end-of-day history from Google Finance

> from pandas_datareader.data import DataReader
> 
> ticker = 'SPY'
> 
> source = 'google'
> 
> start = '01/01/2012' 
> 
> end = '03/22/2014'
> 
> qt = DataReader(ticker, source, start, end)
> 
> print qt.head()
> 
> print qt.tail()


