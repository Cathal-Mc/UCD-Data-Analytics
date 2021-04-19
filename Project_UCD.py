import  matplotlib as plt
import  pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
GITHUB_URL = 'https://github.com/Cathal-Mc/UCD-Data-Analytics'

Netflix = pd.read_csv('C:\\Users\\catha\\PycharmProjects\\UCD Introduction to Data Analytics\\netflix_titles.csv', index_col=0)

Netflix_data = pd.DataFrame(Netflix)
print(Netflix_data.reset_index(drop= True))

droprows= Netflix_data.dropna()
print(Netflix_data.shape, droprows.shape)

Netflix_sorted = Netflix_data.set_index(['title', 'director']).sort_index()
print(Netflix_sorted)


Loop = 10
while Loop != 0 :
    print("correcting...")
    Loop = Loop - 1
    print(Loop)

Movies_Data = pd.read_csv('C:\\Users\\catha\\PycharmProjects\\UCD Introduction to Data Analytics\\MoviesOnStreamingPlatforms_updated.csv')

concat_data= pd.concat([Netflix_data, Movies_Data])
print(concat_data)

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

np_baseball = np.array(baseball)

print(type(np_baseball))
print(np_baseball)

Tesla_stock = pd.read_csv('C:\\Users\\catha\\PycharmProjects\\UCD Introduction to Data Analytics\\TSLA.csv')
Apple_stock = pd.read_csv('C:\\Users\\catha\\PycharmProjects\\UCD Introduction to Data Analytics\\apple.csv')

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(Tesla_stock['Date'], Tesla_stock['Open'], color = 'b')
ax[0, 1].plot(Tesla_stock['Date'], Tesla_stock['Close'], color = 'b')
ax[1, 0].plot(Apple_stock['Date'], Apple_stock['Open'], color = 'r')
ax[1, 1].plot(Apple_stock['Date'], Apple_stock['Close'], color = 'r')
ax[0,0].set_title('Opening Tesla Stock')
ax[0,0].set_ylabel('Stock Price')
ax[0,1].set_title('Closing Tesla Stock Price')
ax[0,1].set_ylabel('Stock Price')
ax[1,0].set_title('Opeing Apple Stock Price')
ax[1,0].set_xlabel('Time')
ax[1,0].set_ylabel('Stock Price')
ax[1,1].set_title('Closing Apple Stock Price')
ax[1,1].set_xlabel('Time')
ax[1,1].set_ylabel('Stock Price')
plt.show()

#1 We can see from the tesla graphs that there was a huge jump in price in December 2019
#2 Apple had a massive drop off in price mid way through 2014
#3 Apple stock price stayed steady after the massive drop in price
#4 The opening and closing graphs are very similar.
#5 Tesla's stock was steady for the first 3 years and then started to rise rapidly