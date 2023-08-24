import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')
result = reader.readtext('position1.png')

def f1(a):
    '''
    输入的a是一个列表，每一条数据是四个坐标，每一个坐标是一个横坐标，一个纵坐标。
    '''
    output = 0
    #what is i?
    for i in a:
        if i[0] == [720, 346]:
            output = i
    return output

def f2(b):
    output = 0
    for i in b:
        if i[0][0] ==[720, 346]:
            output = i[1]
    return output
list_positions = []
for i in result:
    list_positions.append(i[0])
    # print(i,type(i),i[0])

for i in list_positions:
    print(i,type(i),i[0],i[1])
    if i[0] == [720, 346]:
        print('here')

print(f2(result))
#"""
'''
now the question is 
'''

