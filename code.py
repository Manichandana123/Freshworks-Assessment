import time
import json
class datastore:
    def create(self,key,value,ttl=0):
        if key in data:
             print("The key is already present in the datastore.\n")          
        else:
            if(key.isalpha()):
                if(len(data)<(1024*1024*1024)):#checks whether size of datastore is less than 1GB
                    if((len(key)<=32) and len(value)<=(16*1024*1024)):#checks whether key is capped to 32 chars and value is capped to 16KB
                         if(ttl==0):
                            l=[value,ttl]
                         else:
                            l=[value,time.time()+ttl]   
                         data[key]=l
                         with open("data_df.json", 'w') as json_file:
                                json.dump(data, json_file)#stores the data in json file to maintain consu
                         print("key value pair is added to DATA STORE")
                         print("THE DATASTORE IS:")
                         print(data)
                    else:
                        print("ERROR:Length of key must not exceed 32 bytes")
                else:
                    print("ERROR:file size should not exceed 1 GB")
            else:
                print("ERROR:key must be only string.Please enter valid string")
                
    def delete(self,key):
         if key in data:
                store=data[key]
                if(store[1]!=0):
                    if time.time()<store[1]: 
                            print("The value for the above key is: ")
                            print(data[key])  
                            del data[key]
                            a_file = open("data_df.json", "w")
                            json.dump(data, a_file)
                            a_file.close()
                            print("Key and value are deleted") 
                           
                    else:
                        print("ERROR: time-to-live of",key,"has expired")
         else:
            print("ERROR:key is not present in datastore")
            
    def read(self):
         key=input("Enter key value: ")
         if key in data:
            store=data[key]
            if(store[1]!=0):
                if time.time()<store[1]: 
                    updated_string=str(key)+":"+str(store[0]) 
                    print(updated_string)#returns the value in the format of JsonObject
                else:
                      print("ERROR: time-to-live of",key,"has expired") 
            else:
                updated_string=str(key)+":"+str(store[0])
                print(updated_string)#returns the value in the format of JsonObject         
         else: 
            print("ERROR:The key does not exist in the dictionary.Enter the correct key")

data={}#initializing empty dictionary
inp=datastore()#creates object to class
while(1):
    print("1.create 2.delete 3.read")
    x=int(input("Enter any one of the above operations"))
    if(x==1):
        key=input("Enter key: ")
        value=input("Enter value: ")
        print("Do you want to give timeout? 1.yes 2.no ")
        z=int(input())
        if(z==1):
            timeout=int(input("Enter timeout: "))
            inp.create(key,value,timeout)
        else:
            inp.create(key,value)
    elif(x==2):
        key=input("Enter key value: ")
        inp.delete(key)
    elif(x==3):
        inp.read()
    print("Do you want to continue? 1.yes 2.no")
    y=int(input())
    if(y==1):
        continue
    else:
        break
        
