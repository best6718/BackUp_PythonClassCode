d = '2017-01-01'
year, month, day = d.split('-')        
print(year + ' ' +  month + ' ' + day)           

d = '2017-01-01'
year, rest = d.split('-', 1)  # second input is the max parameter (1 split) 
print(year + ' ' + rest)

txt = "apple#banana#cherry#orange"
print(txt.split("#", 1))
print(txt.split("#", 2))    # (2 splits)
