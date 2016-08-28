# Streamline everything

## Use a batch file for running the Python program

https://automatetheboringstuff.com/appendixb/

To make it convenient to run your Python program, create a .bat batch file for running the Python program with py.exe. To make a batch file, make a new text file containing a single line like the following:


```@py.exe C:\path\to\your\pythonScript.py %*```

## Error Handling

You can put the previous divide-by-zero code in *a try clause and have an except clause contain code to handle what happens when this error occurs*.


    def spam(divideBy):
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            print('Error: Invalid argument.')

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
    
When code in a try clause causes an error, the program execution immediately moves to the code in the except clause. After running that code, the execution continues as normal. The output of the previous program is as follows:


    21.0
    3.5
    Error: Invalid argument.
    None
    42.0



## Keeping time


**measure how long a piece of code takes to run**

    import time 

    def calcProd(): 
      # Calculate the product of the first 100,000 numbers.
      product = 1
      for i in range(1,100000):
              product = product * i 
      return product

    startTime = time.time()
    prod = calcProd()
    endTime = time.time()

    print('The result is %s digits long.' % (len(str(prod))))
    print('Took %s seconds to calculate.' % (endTime - startTime))
    
    

## Project: Super Stopwatch

**Track how long each lap lasts between your "enter"s.**


    #! python2
    # stopwatch.py - A simple stopwatch program.

    import time

    # Display the program's instructions.
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    raw_input()                    # press Enter to begin
    print('Started.')
    startTime = time.time()    # get the first lap's start time
    lastTime = startTime
    lapNum = 1      # TODO: Start tracking the lap times.

    # Start tracking the lap times.
    try:
      while True:
          raw_input()
          lapTime = round(time.time() - lastTime, 2)
          totalTime = round(time.time() - startTime, 2)
          print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime))
          lapNum += 1
          lastTime = time.time() # reset the last lap time
    except KeyboardInterrupt:
         # Handle the Ctrl-C exception to keep its error message from displaying.
      print('\nDone.')
