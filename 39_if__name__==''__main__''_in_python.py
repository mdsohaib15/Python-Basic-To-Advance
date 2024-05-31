# ************************** THIS IS MAIN PROGRAM FILE *****************************************
# without __name__ =="__main__"
# by this run twice bcz one time it automatically run and second we call a function
# import good # it run a function automatically 
# good.hey() # we run a function by calling
#=============================================================================================#

# using __name__ == "__main__" in good file
import good  # IF WE RUN THIS ONLY IT CANNOT PRINT FUNCTION THAT ARE IN THE __name__ == '__main__'
good.hey()