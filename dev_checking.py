import csv
import json

def checking(list_dict,name):
    if list_dict:
        for i in list_dict:
            if name in i.values():
                return True
    return False

with open("data.csv",'r') as csv_file:
    r=csv.reader(csv_file)
    json_out=[]
    temp_dict={}
    for i,j in enumerate(r):
        if i==0:
            header=j
            #print(header)
        else:
            a=j
            if any(s.strip() for s in a):
                if checking(json_out,a[0]):
                    if 'children' in json_out[-1].keys():

                        if  not checking(json_out[-1]['children'],a[3]):

                            m = json_out[-1]
                            if 'children' in m.keys():
                                if checking(m['children'], a[3]):
                                    continue
                                else:

                                    for k in range(len(a[3:6])):
                                        k=k+3
                                        row=a[k]
                                        temp_dict[header[k]] = row
                                    m['children'].append(temp_dict)
                                    temp_dict = {}
                            else:
                                m['children'] = []
                                for k,row in enumerate(a[3:6]):
                                    k=k+3
                                    temp_dict[header[k]] = row
                                m['children'].append(temp_dict)
                                #print(m)
                                temp_dict = {}
                        print(a[6])

                        if  a[6]:
                            x = m['children'][-1]
                            if 'children' in x.keys():
                                if checking(x['children'], a[6]):
                                    continue
                                else:
                                    for k in range(len(a[6:9])):
                                        k = k + 6
                                        row = a[k]
                                        temp_dict[header[k]] = row
                                    x['children'].append(temp_dict)
                                    temp_dict = {}
                            else:
                                x['children'] = []
                                for k, row in enumerate(a[6:9]):
                                    k = k + 6
                                    temp_dict[header[k]] = row
                                x['children'].append(temp_dict)
                                # print(m)
                                temp_dict = {}

                    else:
                        if a[3]:
                            m = json_out[-1]
                            if 'children' in m.keys():
                                if checking(m['children'], a[3]):
                                    continue
                                else:

                                    for k in range(len(a[3:6])):
                                        k = k + 3
                                        row = a[k]
                                        temp_dict[header[k]] = row
                                    m['children'].append(temp_dict)
                                    temp_dict = {}
                            else:
                                m['children'] = []
                                for k, row in enumerate(a[3:6]):
                                    k = k + 3
                                    temp_dict[header[k]] = row
                                m['children'].append(temp_dict)
                                # print(m)
                                temp_dict = {}
                else:
                    if a[0]:
                        for k in range(len(a[:3])):

                            row=a[k]
                            temp_dict[header[k]]=row
                        json_out.append(temp_dict)

                        temp_dict={}
    with open("output.json", 'w') as json_file:
        json_file.write(json.dumps(json_out,indent=3))

    print(json_out)













