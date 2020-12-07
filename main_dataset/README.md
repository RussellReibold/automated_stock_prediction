# What were the data?
The main data set was the price development of 130 shares over the last 14 years. I chose 14 years because it was important to me to cover the time before and during the US real estate bubble.
## What exactly was i looking for in the data?
Once I had the main data set, I had to develop a function that searched for certain price patterns I had specified and extracted the days on which these patterns occurred.
## How to define win and loss trades
Once I had the new data set, which consisted only of data points/days where the previously defined price patterns occurred, I had to determine how exactly a win and a loss trade was defined. 
I also created a function with a for loop that checked each data set. If the price reached the target price within 2.5 months, it was a win trade. If the price fell below a certain level within these 2 months, the trade was classified as a loss. 



## License
[MIT](https://choosealicense.com/licenses/mit/)
