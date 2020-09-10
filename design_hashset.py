class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #import numpy as np
        self.buckets=1001
        self.bucketsItem=1001
        self.ram=[[False for i in range(self.buckets)] for j in range(self.bucketsItem)]
        #self.ram=np.empty(shape=[self.buckets,self.bucketsItem],dtype=bool)
        #print(self.ram.shape)
        #print('RAMMMMMM a lot',self.ram[2][0] )
        
    def hash1(self,key):
        return int(key%self.buckets)
    def hash2(self,key):
        return int(key/self.bucketsItem ) 
    
    def add(self, key: int) -> None:        
        self.bucket=self.hash1(key)
        self.bucketItem=self.hash2(key)
        #print('333333333',self.ram[3][0] )
        #print('RAMMMMMM',self.ram[15][0] )
        print('add',self.bucket)
        print('add',self.bucketItem)
        print('######')
        if self.ram[self.bucket]== None:
            #print('@#$%^@$%%#',self.ram)
            self.ram[self.bucket]=bool([self.bucketsItem])
            
        #print('333333333',self.ram[15][0] )
        #print('11111',self.ram[self.bucket][self.bucketItem])
        self.ram[self.bucket][self.bucketItem]=True
        
        #self.ram[self.bucket][self.bucketItem]=True
        
        #print('RAMMMMMM',self.ram[2][0] )
        print("1111111",self.ram[1][0])
        #print('333333333',self.ram[15][0] )
        
    def remove(self, key: int) -> None:
        self.bucket=self.hash1(key)                        
        self.bucketItem=self.hash2(key)
        print('remove',self.bucket)
        print('remove',self.bucketItem)
        print('RAMMMMMM a lot',self.ram[2][0] )
        print('@@@@@@@@@@@@@@@@@@@@@')
        if self.ram[self.bucket]!= None:
            #print(self.ram[self.bucket])
            self.ram[self.bucket][self.bucketItem]=False
            #print('reeee',self.ram[self.bucket][self.bucketItem])
            print('333333333',self.ram[15][0] )
        print('priya is good girl',self.ram[2][0] )
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        self.bucket=self.hash1(key)  
        print('contains',self.bucket)
        self.bucketItem=self.hash2(key) 
        print('conatins',self.bucketItem)          
        #print("@@@@@@@@@@@@@@@@@@@@@@",self.ram[2][0])
       
       
        return self.ram[self.bucket] != None and self.ram[self.bucket][self.bucketItem] == bool([self.buckets])
            

    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
