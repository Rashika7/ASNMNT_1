#!/usr/bin/env python
# coding: utf-8

#                                                JAI GURUJI

# # Q-1) In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# *, 
# "hello", 
# -87.8, 
# -, 
# /, 
# +, 
# 6
# # Ans- 1
#   According to definition and eg given in the question, the values are * , "hello", -87.8, 6. While rest of the elements(-, /, +) are expressions.

# # Q-2) What is the difference between string and variable?
# # Ans- 2
#   The measure difference between string and variable is written below:
#   
#   String always writes in single and double quotes, it is immutable and datatype.
#   Variable stores datatypes, and can't start by integer and special characters.

# # Q-3) Describe three different data types.
# # Ans- 3
#   The three data types are int, string and bool.
#   int always represents integer values, and also convert float data type into integer.
#   string contains integers, words, alphabets and special characters in single and double quotes.
#   bool data type conveys when variable contains True and False, it works as 1 and 0.

# # Q-4) What is an expression made up of? What do all expressions do?
# # Ans- 4
#   An expression made up of values, variables, operators, and calls to functions. If we type an expression at the Anaconda     prompt or jupyter notebook, the interpreter evaluates it and displays the result, which is always a value:
#   eg- input = 1+1
#      After run input variable, we get output:
#      2.
# 
#   

# # Q-5) This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# # Ans- 5
#   In programming language, an “expression” is a combination of values and functions that are combined and interpreted by the compiler to create a new value, while a “statement” which is just a standalone unit of execution and doesn’t return anything.

# # Q-6) After running the following code, what does the variable bacon contain?
# # bacon = 22
# # bacon + 1
# # Ans- 6
#   

# In[3]:


bacon = 22
bacon + 1


# In[4]:


bacon


#  After run the code, bacon contains 22, since bacon is a variable and 22 is the assigned value for bacon variable.

# # Q-7) What should the values of the following two terms be?
# "spam" + "spamspam"
# "spam" * 3

# In[7]:


"spam" + "spamspam" # Both the strings concatenate.


# In[8]:


"spam" * 3 # the string repeates three times.


# # Q-8) Why is eggs a valid variable name while 100 is invalid?
# # Ans- 8
#   eggs is a word while 100 is a numeric value, in python variable can't starts by numeric value.

# # Q-9) What three functions can be used to get the integer, floating-point number, or string version of a value?
# # Ans- 9
#   The three functions are: int, float, str uses to get the integer, floating-point number, or string version of a value respectively.

# # Q-10) Why does this expression cause an error? How can you fix it?
# 'I have eaten' + 99 + 'burritos'

# In[9]:


'I have eaten' + 99 + 'burritos'


# 99 is a integer in the given expression,it's type is int. So, two different data types can't concatenate. To fix this error change 99 in to string by using str function.

# In[1]:


t = str(99)
t


# In[10]:


t = str(99)
p='I have eaten ' + t  + ' burritos'
print(p)


#                                         """ Thank You """
