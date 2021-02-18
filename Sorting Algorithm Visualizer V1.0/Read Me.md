# Important.
With threading i was able to visualize larger arrays without the 
program freezing on me while sorting the array half-way some
sortings may interfere with the mainthread wich would cause
freezes and bugs 

some bugs of the threaded version
blinking of the tkinter canvas because its not built to endure
quick updates & deletes, even though its double buffered..

some bugs of the non threaded version
no blinking of the canvas but only one task beside the main thread
is allowed hence pressing any button while sorting could cause
the program to crash

## Use the threaded version to:
  - Visualize bigger arrays

## Use the non threaded version to:
  - Visualize smaller arrays without getting the blink effect
  - trying to understand how the sorting works.
