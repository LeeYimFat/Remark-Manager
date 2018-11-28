# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:01:19 2018
@author: Administrator
"""

def leap_year(year):
    
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False
    
def cal_month_day(year,month):
    days = 0
    
    if month == 2:
        days = 29 if leap_year(year) else 28
    else:    
        days = 31 if month in [1,3,5,7,8,10,12] else 30
    return days

def cal_weekday(year,month):
    totaldays = 0
    
    for i in range(1, year):
        totaldays += 366 if leap_year(i) else 365
    for i in range(1,month):
        totaldays += cal_month_day(year,i)
    return totaldays

def calendar(year,month):    
    count_week = 0

    print("\n")
    print("\t\t" + str(year) + "." + str(month))
    print("\n")
    print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
    print("--------------------------------------------------------")   
    
    for i in range((cal_weekday(year,month)%7) + 1):
##两个个关键点： 1. 日历都是从周日开始 2. 公元元年一月一日，是周一。自己参详。 
        print("\t", end = '')
        count_week += 1
        
    for i in range(1, cal_month_day(year,month) + 1):       
        print (str(i) + "\t",  end='')
        count_week += 1   
        if count_week % 7 == 0:
            print("\n")
       
#Above is part of calendar
#Below is part of remark

def quitt():
    pass

def writing_state():
    
    print("Finish? y/n")
    state = input()
    if state == 'y':
        print("\n")
        remark()
    if state == 'n':
        write()

    
def write():
    date = input("notice that the form of date is year.month.day: ")
    to_do = input("what to do: ")
    mark = date + " : " + to_do
        
    doc = open('remark.txt','a')
    doc.write(mark + "\n")
    doc.close()
    
    writing_state()
        
def read():
    read_year = int(input("which year you want to read: "))
    read_month = int(input("which month you want to read: "))
    calendar(read_year, read_month)
    calendar_remark = str(read_year) + '.' + str(read_month)
    print("\n")
    print("REMARK:")
    with open('remark.txt','r') as fffff:
            lines = fffff.readlines()
            for line in lines:
                if calendar_remark in line:
                    print(line)
                else:
                    pass
    print("\n")
    remark()

        
def delete():
    print("delete one or all?")
    a = input()
    if a == 'all':
        with open('remark.txt','w') as f:
            f.truncate()
            remark()
    if a == 'one':
        with open('remark.txt','r') as f:
            text = f.read()
            print(text)
            
        print("Which part you want to delete(some parts of the remark is enough): ")
        b = input()
            
        with open('remark.txt','r') as ff:
            lines = ff.readlines()
        with open('remark.txt','w') as fff:
            for line in lines:
                if b in line:
                    continue#do not run the following code
                fff.write(line)
                    
        print("the new to do list: ")
        read()
        print("\n")
        remark()
        
def remark():
    print("write remark or read remark or delete remark or quit?")
    print("input quit or any other word to quit the remark manager.") 
    function = input()
    
    if function == "quit":
        quitt()
        
    if function == "write":
        write()
    
    if function == "read":
        read()
        
    if function == "delete":
        delete()

if __name__ == "__main__":
    remark()

    












