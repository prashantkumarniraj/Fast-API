# what is API ?

# API stands for Application Programming Interface.
# It is a set of rules and protocols that allows different software applications to communicate with each other. 
# APIs define how requests and responses should be structured, enabling developers to access and use the functionality of another application or service without needing to understand its internal workings. 
# APIs are commonly used for web services, allowing applications to interact with each other over the internet.
# As for analogy it is just like a waiter in a restaurant

#need for api

# let say we made a website in which we want to know the train running between the two station 
# for this we made one database then one backend system in which there is a function called fetch which help to find the train 
# then we made one frontend for user interaction in which user know the train Name
# so all this possible using monolithic structure this structure is tightly packed 
# so before the api this is how websites are made

# now let say yatri makemytrip whereismytrain wants to know the train information so they go to irctc and demand this but 
# irctc will not give them the databse because of security reasons as well as not the backend because it is tightly coupled by the whole system 
# backend is not single function it is a part of whole system and tightly coupled
# so by this we can't even share a single informatio of databse to any third party 

# how to overcome this problem

# 1> firslty we decoupled the whole System
# 2> then we make a single backend system in which there is a layers of api
# 3> then we give the access of api to third party