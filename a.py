import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')
result = reader.readtext('chinese.jpg')

for i in result:
    print(i)



#"""
'''
now the question is 
'''