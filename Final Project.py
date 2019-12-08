#Annual Sales Report for a Company
#Program to calculate the total from all the quarters and then to display in a table form
#Author:Rebecca Abraham
#variables are id_list,sales_data,infile,line,ids,value,qtr,amount,location,max_id,max_value,qtr1,qtr2,qtr3,qtr4

#function to get the salesperson's ID numbers
def get_IDs(filename):
    id_list=[]
    sales_data=[]
    infile=open(filename,'r')
    for line in infile:
        id_list.append(line.strip())
        sales_data.append([0,0,0,0])
    #to sort the ID numbers
    id_list.sort()
    infile.close() #to close the file after complete reading
    return id_list,sales_data

#function to read all the sales data and uss
def process_sales_data(filename, id_list, sales_data):
    infile=open(filename,'r')
    for line in infile:
        line=line.strip().split()
        ids=line[0]
        value=int(line[1])
        if value>=1 and value<=3:
            qtr=0
        elif value>=4 and value<=6:
            qtr=1
        elif value>=6 and value<=9:
            qtr=2
        else:
            qtr=3

        amount=float(line[2])

        # to find the position of the id
        location=id_list.index(ids)

        sales_data[location][qtr]=round((sales_data[location][qtr]+amount),2)
    infile.close() #to close the file
    return sales_data

#function to print the report having all the details of the salesperson
def print_report(id_list, sales_data):
    print('\n  -------Annual Sales Report------\n')
    print(('ID\t\t   QT1\t\t   QT2\t\t   QT3\t\t   QT4\t\t Total'))
    qtr1=0
    qtr2=0
    qtr3=0
    qtr4=0
    max_id=0
    max_value=0
    for i in range(len(id_list)):
        qtr1=qtr1+sales_data[i][0]
        qtr2=qtr2+sales_data[i][1]
        qtr3=qtr3+sales_data[i][2]
        qtr4=qtr4+sales_data[i][3]
        total=round(sum(sales_data[i]),2) #calculating the total of the all the sales_data

        # finding the maximum value among the four quarters
        value=max([sales_data[i][0],sales_data[i][1],sales_data[i][2],sales_data[i][3]])
        if value>max_value:
            max_value=value
            max_id=id_list[i]
        print('%s\t%8.2f\t%8.2f\t%8.2f\t%8.2f\t%8.2f' %(id_list[i],sales_data[i][0],sales_data[i][1],sales_data[i][2],sales_data[i][3],total))
    qtr_total=qtr1+qtr2+qtr3+qtr4
    print('%s\t%8.2f\t%8.2f\t%8.2f\t%8.2f\t%8.2f\t'%('Total',round(qtr1,2),round(qtr2,2),round(qtr3,2),round(qtr4,2),round(qtr_total,2)))
    amount=max([qtr1,qtr2,qtr3,qtr4])
    position = [qtr1,qtr2,qtr3,qtr4].index(amount)
    print('\nMax sales by Salesperson: ID =',max_id+', Amount = $'+str(round(max_value,2)))
    print('Max sales by Quarter: Quarter = ',str(position+1)+', Amount = $'+str(round(amount,2)))

#the main function
def main():
    id_file_name=input('Enter the name of the sales ids file: ')
    id_list, sales_data=get_IDs(id_file_name)
    data_file_name=input('Enter the name of the sales data file: ')
    sales_data=process_sales_data(data_file_name, id_list, sales_data)
    print_report(id_list,sales_data)

#calling the main function
main()
