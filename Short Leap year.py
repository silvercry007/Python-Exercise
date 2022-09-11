#!/bin/python3
def is_leap(year):
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("Enter a Year Below ")
year = int(input())
print(is_leap(year))