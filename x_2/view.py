import sys, csv, operator, random, string, json, requests,os
#from django.shortcuts import render,redirect
#from django.http import HttpResponse


def sort_by_recency(request):
	CurrentDirectory = os.getcwd()
	path = CurrentDirectory  +"\\"+"rfm.csv"

	with open(path,"r", newline='') as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)
		data = [line for line in reader]

    
		column = "R"
		index = headers.index(column)

		sorted_data = []

		sorted_data = sorted(data, key=lambda x: x[index])

		newzip = []
		newzip.append(headers)
		newzip.append(sorted_data)
		metadata = json.dumps(newzip)

		return render (request,'yourhtml' ,metadata)


def sort_by_frequency(request):
	CurrentDirectory = os.getcwd()
	path = CurrentDirectory  +"\\"+"rfm.csv"

	with open(path,"r", newline='') as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)
		data = [line for line in reader]

    
		column = "F"
		index = headers.index(column)

		sorted_data = []

		sorted_data = sorted(data, key=lambda x: x[index])
    

		newzip = []
		newzip.append(headers)
		newzip.append(sorted_data)
		metadata = json.dumps(newzip)


		return render (request,'yourhtml' ,metadata)

def sort_by_monetary(request):
	CurrentDirectory = os.getcwd()
	path = CurrentDirectory  +"\\"+"rfm.csv"

	with open(path,"r", newline='') as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)
		data = [line for line in reader]

    
		column = "M"
		index = headers.index(column)

		sorted_data = []

		sorted_data = sorted(data, key=lambda x: x[index], reverse = False)
    

		newzip = []
		newzip.append(headers)
		newzip.append(sorted_data)
		metadata = json.dumps(newzip)

		return render (request,'yourhtml' ,metadata)



def sort_by_RFM(request):
	CurrentDirectory = os.getcwd()
	path = CurrentDirectory  +"\\"+"rfm.csv"

	with open(path,"r", newline='') as csvfile:
		reader = csv.reader(csvfile)
		headers = next(reader)
		data = [line for line in reader]

		headers.append('RFM')

		for d in range(len(data)):
			x = int(data[d][1]) + int(data[d][2]) + int(data[d][3])
			data[d].append(str(x))


    
		column = "RFM"
		index = headers.index(column)

		sorted_data = []

		sorted_data = sorted(data, key=lambda x: x[index], reverse = False)
    

		newzip = []
		newzip.append(headers)
		newzip.append(sorted_data)
		metadata = json.dumps(newzip)

		return render (request,'yourhtml' ,metadata)


