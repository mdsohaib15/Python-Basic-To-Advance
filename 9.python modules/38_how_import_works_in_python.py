# import greetings # by this we can access all function in this file
# greetings.welcome()
# greetings.Hello()

# from greetings import welcome # ->by this can only access one function in this file
# welcome()
# Hello() # -> it thrown an error bcz only import welcome function in greetings file

# from greetings import Hello # ->by this can only access one function in this file
# Hello()
# welcome() # -> similarly it shows an error

# import all things in file 
# from greetings import * 
# welcome()
# Hello()

# as keyword using for short name
import greetings as gr
gr.Hello()
gr.welcome()