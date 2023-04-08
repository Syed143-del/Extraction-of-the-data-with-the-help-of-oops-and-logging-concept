import logging

logging.basicConfig(filename="extract.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s %(name)s")

logging.info("Just checking weather the logging code is working or not")

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

class Datastructures:
    def __init__(self,data):
        self.data=data

    def extract_values(self):
        """extract values from the dictionary"""
        try:
       #     logging.info("extracting values from the dictionary")
        #    values_dict = []
         #   #if type(self.data) == dict:
                #values_dict = self.data.values()
          #  if type(self.data) == list:
           #     for i in self.data:
            #        if type(i) == dict:
             #           values_dict.append(i.values())
            #logging.info("The keys from the dictionary are %s", values_dict)
            #return values_dict
        #except Exception as e:
         #   logging.exception(e)

#new=Datastructures(l)
#print(new.extract_values())

    def extract_values_from_dic(self):
        try:
            logging.info("Now we are entering the function which extracts the values from the dictionar")
            dict_values=[]
            if type(self.data)==list:
                for i in self.data:
                    if type(i)==dict:
                        dict_values.append(i.values())
            logging.info("The extracted dictionary values are %s", dict_values)
            return "The extracted values of the dictionary from the list is ", dict_values
        except Exception as e:
            logging.exception(e)


    def extract_keys(self):
        try:
            dict_keys=[]
            logging.info("Now we have entered into the function which extracts the keys from dic in list")
            logging.info("The data which is passed is %s", self.data)
            if type(self.data)==list:
                for i in self.data:
                    if type(i)==dict:
                        dict_keys.append(i.keys())
                        logging.info("The keys which are present in the list is %s",dict_keys)
            return "The keys which are present in the list is ", dict_keys
        except Exception as e:
            logging.info(e)

#keyy=Datastructures(l)
#print(keyy.extract_keys())

    def extract_list(self):
        try:
            ext_lst=[]
            logging.info("Now we have entered into the function which extract the list from the given data")
            logging.info("The data which is passed by the user is %s", self.data)
            if type(self.data)==list:
                for i in self.data:
                    if type(i)==list:
                        ext_lst.append(i)
                        logging.info("The extracted list are %s", ext_lst)
            return "The extracted list from the list is ", ext_lst
        except Exception as e:
            logging.exception(e)

#lst=Datastructures(l)
#print(lst.extract_list())

    def ext_dict(self):
        try:
            dicct=[]
            logging.info("Now we have entered into the function which exctracts the dict from the given data")
            logging.info("The data which is entered by the user is %s", self.data)
            for i in self.data:
                if type(i)==dict:
                    dicct.append(i)
                    logging.info("The dictionary data which is extracted is %s", i)
            return "The dictionary item which is present in the list is", dicct
        except Exception as e:
            logging.exception(e)

#di=Datastructures(l)
#print(di.ext_dict())

    def extct_tup(self):
        try:
            tup=[]
            logging.info("Now we have entered into the function which extracts the tuple from the given data")
            logging.info("The data which is passed by the user is %s", self.data)
            for i in self.data:
                if type(i)==tuple:
                    tup.append(i)
                    logging.info("The extracted tuple data from the list is %s",i)
            return "The extracted tuple data is ", tup
        except Exception as e:
            logging.exception(e)

#tu=Datastructures(l)
#print(tu.extct_tup())


#lt=Datastructures(l)
#print(lt.extract_list())

    #def extract_odd_list(self):
     #   try:
      #      odd_no=[]
       #     logging.info("Now we have entered into the function which extracts the odd num from list")
        #    lsst=self.extract_list()
         #   logging.info("Now we have the extracted list %s", lsst)
          #  for i in lsst:
           #     for j in i:
            #        if type(j)==int:
             #           if (j%2) != 0:
              #              odd_no.append(j)
            #eturn odd_no
        #except Exception as e:
         #   logging.exception(e)


#print(ext_lst)
#od=Datastructures(l)
#print(od.extract_odd_list())

   # def extract_list_odd(self):
        """extract odd numbers from list"""
        #try:
         #   logging.info("extracting odd numbers from lists")
          #  q8 = self.extract_list()
           # odd_num = []
            #for i in q8:
             #   for j in i:
              #      if type(j) == int:
               #         if (j % 2) != 0:
                #            odd_num.append(j)
           #logging.info(f"odd numbers {odd_num}")
            #return odd_num
        #except Exception as e:
         #   logging.exception(e)

#od=Datastructures(l)
#print(od.extract_list_odd())

#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]


    #def extrct_odd(self):
        #try:
          #  odd_no=[]
          #  logging.info("Now we are entering inside the function which tkes out odd no")
           # for i in self.data:
           #     if type(i)==int:
            #        if i%2 !=0:
             #          logging.info("The first odd nos are %s", i)
             #   elif type(i)==list:
              #      for j in i:
               #         if j%2!=0:
                #            odd_no.append(j)
                 #           logging.info("The odd nos in the list is %s",j)
              #  elif type(i)==tuple:
               #     for k in i:
                #        if k%2!=0:
                 #           odd_no.append(k)
                  #          logging.info("The odd no from the tuples is %s",k)



         #   return odd_no
      #  except Exception as e:
       #     logging.exception(e)

#od=Datastructures(l)
#print(od.extrct_odd())

#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

    def extract_string(self):
        try:
            st=[]
            logging.info("The function will extract the string from the given list")
            logging.info("The data which is passed by the user is %s", l)
            for i in self.data:
                if type(i)==list:
                    for j in i:
                        if type(j)==str:
                            st.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            st.append(k)
                        if type(v)==str:
                            st.append(v)
                        logging.info("The extracted strings are %s",st)

            return "The extracted strings are ", st
        except Exception as e:
            logging.exception(e)

#stt=Datastructures(l)
#print(stt.extract_string())

    #def occurrences_all(self):
        """
        Number of occurrences of all data
        """
     #   try:
      #      logging.info("Number of occurrences of all data")
      #      q10 = []
       #     for i in self.data:
        #        if type(i)==dict:
        #            for k,v in i.items():
         #               q10.append(k)
         #               q10.append(v)
          #      if type(i)==list or type(i)==tuple or type(i)==set:
           #         for j in i:
            #            q10.append(j)
             ##      q10.append(i)
          #  for i in set(q10):
           #     c=q10.count(i)
          #      q10[i]=c
           # return q20
       # except Exception as e:
        #    logging.exception(e)



#occ=Datastructures(l)
#print(occ.occurrences_all())


#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

    def extract_numeric(self):
        try:
            num=[]
            logging.info("Now we have entered such function which extracts only the numeric from list")
            logging.info("The data which is entered by the user is %s", l)
            for i in self.data:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int or type(j)==float:
                            num.append(j)


                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(k)==float:
                            num.append(k)
                        if type(v)==int or type(k)==float:
                            num.append(v)
            logging.info("The extracted numeric values are %s", num)
            return num
        except Exception as e:
            logging.exception(e)

#ext_nu=Datastructures(l)
#print(ext_nu.extract_numeric())

    def summ_numeric(self):
        try:
            logging.info("Now we have entered into the function which calculates the sum of numbers")
            numbers=self.extract_numeric()
            total=sum(numbers)
            return total
        except Exception as e:
            logging.exception(e)

#suu=Datastructures(l)
#print(suu.summ_numeric())


    def summ_up_numeric(self):
        try:
            logging.info("Now we have entered into the function which clculate the sum of the numeric")
            numbers1=self.extract_numeric()
            logging.info("This we need to check %s",numbers1)
            total=sum(numbers1)
            logging.info("The sum is %s",total)

            return total
        except Exception as e:
            logging.exception(e)

#sm=Datastructures(l)
#print(sm.summ_up_numeric())

    def reverse_list(self):
        try:
            logging.info("This function reverse the list")
            logging.info("The data entered by the user is %s", l)
            if type(self.data)==list:
                logging.info("The revered pattern is %s",self.data[-1::-1])
                return self.data[-1::-1]
            else:
                logging.info("Data is not list not possible to reverse")
        except Exception as e:
            logging.exception(e)


rev=Datastructures(l)
print(rev.reverse_list())