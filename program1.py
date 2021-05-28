#!/usr/bin/env python
# coding: utf-8

# Problem is we need to have a base class X and 3 sub-classes A,B,C.
# 
# While initializing, we need to assign a name to the object. Each class will have execute method which will print the arguments along with object name and class name.
# 
# We can options to create object of a class, call execute method, delete object and check number of execute method calls for an object or a class.

# In[1]:


# Create a base class X
# Add init, execute and shutdown methods
class X:

    def __init__(self, name):
        # It will assign name of the object and print object and class name
        print('Initializing object')
        self.obj_name = name
        self.className = type(self).__name__
        print('Object name: ', self.obj_name)
        print('Class name: ', self.className)
        
    def execute(self, args = dict()):
        # It will print method arguments along with object and class name
        print('Invoking execute()')
        print('Class name: ', self.className)
        print('Object name: ', self.obj_name)
        if len(args) > 0:
            print('Arguments:')
            for k, v in args.items():
                print('Key: ' + str(k) + 'Val: ' + str(v))       
    
    def shutdown(self):
        # It will print object and class name
        print('Invoking shutdown()')
        print('Object name: ', self.obj_name)
        print('Class name: ', self.className)
    
    def getExecCount(self):
        print('Execution count for object {} : {}'.format(self.obj_name, self.exec_count))


# In[2]:


# Creating child classes of X (A,B,C)
class A(X):
    total_exe_count = 0
    def __init__(self, name):
        super().__init__(name)
        self.exec_count = 0
        
    def execute(self, args = dict()):
        super().execute(args)
        A.total_exe_count += 1
        self.exec_count += 1

class B(X):
    total_exe_count = 0
    def __init__(self, name):
        super().__init__(name)
        self.exec_count = 0
        
    def execute(self, args = dict()):
        super().execute(args)
        B.total_exe_count += 1
        self.exec_count += 1
        
class C(X):
    total_exe_count = 0
    def __init__(self, name):
        super().__init__(name)
        self.exec_count = 0
        
    def execute(self, args = dict()):
        super().execute(args)  
        C.total_exe_count += 1
        self.exec_count += 1


# In[3]:


obj_dict = dict()


# In[9]:


# Create functions to create, delete and call execute methods of different classes
def create():
    className = input('Choose class name (A, B, C):')
    objName = input('Enter object name:')
    obj = None
    # Create object of specific class
    if className == 'A':
        obj = A(objName)
    elif className == 'B':
        obj = B(objName)
    elif className == 'C':
        obj = C(objName)  
    else:
        print('Invalid class name!!')
    
    # list out all created objects
    if obj is not None:
        obj_dict[objName] = obj
        print('Object {} of class {} got created.'.format(objName, className))

def delete():
    objName = input('Enter object name:')
    if len(obj_dict) != 0 and obj_dict.get(objName) is not None:
        obj = obj_dict.get(objName)
        obj.shutdown()
        obj_dict.pop(objName)
        print('Object {} deleted'.format(objName))
    else:
        print('Invalid object or object doesnt exist!!')
        
def execute():
    objName = input('Enter object name:')
    if len(obj_dict) != 0 and obj_dict.get(objName) is not None:
        print('Starting execution..')
        print('Please give inputs as key-value pairs. Example- k1-v1 ENTER and enter q to execute')
        i = 0
        ip_dict = dict()
        while True:
            i += 1
            ip = input('input-{} '.format(i))
            if ip.lower() == 'q':
                break;
            ip_val = ip.split('-')
            if len(ip_val) != 2:
                print('Invalid pair!!')
            else:    
                ip_dict[ip_val[0]] = ip_val[1]
         
        obj = obj_dict.get(objName)
        obj.execute(ip_dict)             
    else:
        print('Invalid object or object doesnt exist!!')

def getExecCount():
    objName = input('Enter object name:')
    if len(obj_dict) != 0 and obj_dict.get(objName) is not None:
        obj = obj_dict.get(objName)
        print('Number execution calls for object {}: {}'.format(objName, obj.exec_count))
    else:
        print('Invalid object or object doesnt exist!!')
        
def getTotalExecCount():
    className = input('Choose class name (A, B, C):')
    count = None
    if className == 'A':
        count = A.total_exe_count
    elif className == 'B':
        count = B.total_exe_count
    elif className == 'C':
        count = B.total_exe_count
    else:
        print('Invalid class!!')
    
    if count is not None:
        print('Number of execution count for class {} : {}'.format(className, count))        


# In[10]:


def main():
    
    print("Program started. \n\nChoose \n\n1 to create an object \n2 to delete object by name \n3 to call execute for an object")
    print("4 to check execution count for an object\n5 to check execution count for a class\n\nPress Q to exit")
    
    while True:
        ip = input('Give input:')
        
        if ip.upper() == 'Q':
            print('Stopping program...Thank you.')
            break;
        
        if ip == '1':
            create()
        elif ip == '2':
            delete()
        elif ip == '3':
            execute()
        elif ip == '4':
            getExecCount()
        elif ip == '5':
            getTotalExecCount()
        else:
            print('Invalid input!!')

if __name__ == "__main__":
    main()


# In[ ]:




