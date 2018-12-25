from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import RMSprop
import numpy as np
import xlrd

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excel_table_byname(d, file= u'D:\\仿真数据.xlsx', by_name = u'normal'):#修改自己路径
    data = open_excel(file)
    table = data.sheet_by_name(by_name) #获得表格
    # nrows = table.nrows  # 拿到总共行数
    for rownum in range(0, 80): #也就是从Excel第一行开始
        row = []
        row = table.row_values(rownum)
        d.append(row)
    return d

def excel_table_byname1(t, file= u'D:\\仿真数据.xlsx', by_name = u'normal'):#修改自己路径
    data = open_excel(file)
    table = data.sheet_by_name(by_name) #获得表格
    # nrows = table.nrows  # 拿到总共行数
    for rownum in range(80, 100): #也就是从Excel第一行开始
        row = []
        row = table.row_values(rownum)
        t.append(row)
    return t

train_data = []
train_label = []
train_data = excel_table_byname(d = train_data, by_name = u'normal')
train_data = excel_table_byname(d = train_data, by_name = u'R1_open')
train_data = excel_table_byname(d = train_data, by_name = u'R1_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R2_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R2_short')
train_data = excel_table_byname(d = train_data, by_name = u'R3_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R3_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R4_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R4_short')
train_data = excel_table_byname(d = train_data, by_name = u'R5_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R5_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R6_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R6_short')
train_data = excel_table_byname(d = train_data, by_name = u'R7_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R7_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R8_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R8_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R9_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R9_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R10_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R10_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R11_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R11_short')
#train_data = excel_table_byname(d = train_data, by_name = u'R12_open')
#train_data = excel_table_byname(d = train_data, by_name = u'R12_short')
train_data = excel_table_byname(d = train_data, by_name = u'C1_open')
#train_data = excel_table_byname(d = train_data, by_name = u'C1_short')
#train_data = excel_table_byname(d = train_data, by_name = u'C2_open')
#train_data = excel_table_byname(d = train_data, by_name = u'C2_short')
#train_data = excel_table_byname(d = train_data, by_name = u'C3_open')
#train_data = excel_table_byname(d = train_data, by_name = u'C3_short')
#train_data = excel_table_byname(d = train_data, by_name = u'C4_open')
#train_data = excel_table_byname(d = train_data, by_name = u'C4_short')

temp = []
for i in range(0, 7):
    for j in range(0, 80):
        if i == 0:
            temp = [1, 0, 0, 0, 0, 0, 0]
        elif i == 1:
            temp = [0, 1, 0, 0, 0, 0, 0]
        elif i == 2:
            temp = [0, 0, 1, 0, 0, 0, 0]
        elif i == 3:
            temp = [0, 0, 0, 1, 0, 0, 0]
        elif i == 4:
            temp = [0, 0, 0, 0, 1, 0, 0]
        elif i == 5:
            temp = [0, 0, 0, 0, 0, 1, 0]
        elif i == 6:
            temp = [0, 0, 0, 0, 0, 0, 1]
        train_label.append(temp)
        
train_data = np.array(train_data)
train_label = np.array(train_label)

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(8, activation='relu', input_shape=(4,)))
#model.add(Dropout(0.2))
#model.add(Dense(8, activation='relu'))
#model.add(Dropout(0.1))
model.add(Dense(7, activation='softmax'))

model.summary()#该函数给出了网络结构信息表
#sgd = SGD(lr=0.001, decay=1e-4, momentum=0.9, nesterov=1)

model.compile(loss='mse', 
              optimizer=RMSprop(), 
              metrics=['accuracy'])

model.fit(train_data, train_label, 
          epochs = 100, verbose = 1, 
          batch_size = 1)

test_data = []
test_label = []
test_data = excel_table_byname1(t = test_data, by_name = u'normal')
test_data = excel_table_byname1(t = test_data, by_name = u'R1_open')
test_data = excel_table_byname1(t = test_data, by_name = u'R1_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R2_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R2_short')
test_data = excel_table_byname1(t = test_data, by_name = u'R3_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R3_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R4_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R4_short')
test_data = excel_table_byname1(t = test_data, by_name = u'R5_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R5_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R6_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R6_short')
test_data = excel_table_byname1(t = test_data, by_name = u'R7_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R7_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R8_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R8_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R9_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R9_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R10_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R10_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R11_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R11_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'R12_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'R12_short')
test_data = excel_table_byname1(t = test_data, by_name = u'C1_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'C1_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'C2_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'C2_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'C3_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'C3_short')
#test_data = excel_table_byname1(t = test_data, by_name = u'C4_open')
#test_data = excel_table_byname1(t = test_data, by_name = u'C4_short')

for i in range(0, 7):
    for j in range(80, 100):
        if i == 0:
            temp = [1, 0, 0, 0, 0, 0, 0]
        elif i == 1:
            temp = [0, 1, 0, 0, 0, 0, 0]
        elif i == 2:
            temp = [0, 0, 1, 0, 0, 0, 0]
        elif i == 3:
            temp = [0, 0, 0, 1, 0, 0, 0]
        elif i == 4:
            temp = [0, 0, 0, 0, 1, 0, 0]
        elif i == 5:
            temp = [0, 0, 0, 0, 0, 1, 0]
        elif i == 6:
            temp = [0, 0, 0, 0, 0, 0, 1]
        test_label.append(temp)

test_data = np.array(test_data)
test_label = np.array(test_label)

score = model.evaluate(test_data, test_label)
sim =model.predict(test_data)

pre = []
for i in range(sim.shape[0]):
    row = list(sim[i])
    m = max(row)
    ind = row.index(m)
    if ind == 0:
        pre.append(0)
    elif ind == 1:
        pre.append(1)
    elif ind == 2:
        pre.append(2)
    elif ind == 3:
        pre.append(3)
    elif ind == 4:
        pre.append(4)
    elif ind == 5:
        pre.append(5)
    elif ind == 6:
        pre.append(6)
    for j in range(len(row)):
        if sim[i, j] < m:
            sim[i, j] = 0
        elif sim[i, j] == m:
            sim [i, j] = 1