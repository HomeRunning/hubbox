# filter 需要判断真假或1,0
list_x = [1,2,1,1,2,1,1]
r = filter(lambda x: True if x==1 else False, list_x)
print(list(r))