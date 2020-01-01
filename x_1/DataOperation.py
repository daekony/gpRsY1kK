import csv,random, string
import os

class CsvHanlder:
    def __init__(self, name):
        self.name = name
        CurrentDirectory = os.getcwd()
        path = CurrentDirectory + "\\" + "ilovecoffee"
        if not os.path.isdir(path):
            os.mkdir(path)
        file = open(path + "\\" + "customers.csv", "w")

    def create_csv(self):
        c_name_table =[
                'tom',
                'jason',
                'peter',
                'andrew',
                'anderson',
                'andrea',
                'pippen',
                'oscar',
                'andy',
                'sandra',
                ]
        c_table =[
                'customer_id',
                'customer_name',
                'customer_mobile',
                'frequency',
        ]
        i = 0
        j = 1
        while i==0:
            with open('ilovecoffee\customers.csv','w', newline='') as csvfile:

                writer = csv.writer(csvfile)
                writer.writerow(c_table)
                while j <= 500:
                    firstNum = ''.join(random.sample(string.ascii_letters, 1))
                    lastNum = ''.join(random.sample(string.ascii_letters + string.digits, 7))
                    customer_id = firstNum + lastNum
                    randomChoose = c_name_table[random.randint(0,9)]
                    customer_name = randomChoose + "." + customer_id
                    phoneNum = ''.join(random.sample(string.digits, 8))
                    customer_mobile = '+' + '886' + '9' + phoneNum
                                         #print(customer_mobile)
                    frequency = str(random.randint(0,20))
                    temp_table =[
                        customer_id,
                        customer_name,
                        customer_mobile,
                        frequency,
                    ]
                    writer.writerow(temp_table)
                    j += 1
                i +=1

pusheen = CsvHanlder('Pusheen')
pusheen.create_csv()
