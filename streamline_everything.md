# Streamline everything

## Use a batch file for running the Python program

https://automatetheboringstuff.com/appendixb/

To make it convenient to run your Python program, create a .bat batch file for running the Python program with py.exe. To make a batch file, make a new text file containing a single line like the following:


```@py.exe C:\path\to\your\pythonScript.py %*```


## Keeping time


**measure how long a piece of code takes to run**

  import time 

  def calcProd(): 
	# Calculate the product of the first 100,000 numbers.
	product = 1
	for i in range(1,100000):
    		product = product * i #    	print product
	return product

  startTime = time.time()
  prod = calcProd()
  endTime = time.time()


print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))```