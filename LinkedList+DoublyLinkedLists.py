
# coding: utf-8

# # Linked Lists

# In[10]:


class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


# In[25]:


# This code does not have a dummy head.

class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
        
    def __repr__(self):  # 출력설정 
        if self.nodeCount == 0:
            return ('LinkedList: empty')
        
        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                 s += ' => '
        return s
        
        
    def getAt(self, pos):  # pos번째 값 찾기, 순차탐색
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1   # start from at 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:  # 맨 앞에 삽입
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:  # 맨 끝에 삽입
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)  # 삽입하려면 앞에서부터 순회필요ㅠ
                
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:  # 노드삽입 후 만약 끝노드면 tail 재지정
            self.tail = newNode

        self.nodeCount += 1
        return True
    
    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount :  # pos가 아예 다른 경우
            raise IndexError

        if pos == 1 :  # 리스트의 맨 앞을 제거 
            curr = self.head
            self.head = self.head.next
            
            if self.nodeCount==1 :  # 만약 노드가 1개 였던 경우, tail도 조정필요
                self.tail = None  
        else :
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            
            if pos == self.nodeCount :  # 리스트의 맨 끝을 제거
                self.tail = prev

        self.nodeCount -= 1
        return curr.data
    

    def traverse(self):  
        
        my_list = []
        curr = self.head
        
        while curr != None :
            my_list.append(curr.data)
            curr = curr.next
                    
        return my_list 
    
    
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:  # 주의 : 만약 뒤에 이어붙는 L리스트가 빈 것이면 tail이 None이므로..
            self.tail = L.tail
        self.nodeCount += L.nodeCount
        


# In[24]:


# This code have a dummy head.

class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None
        
    def __repr__(self):  # 출력설정 
        if self.nodeCount == 0:
            return ('LinkedList: empty')
        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                s += ' => '
        return s        

class LinkedList:

    def __init__(self):  # 빈 연결리스트 생성 
        self.nodeCount = 0
        self.head = Node(None)   # None이 들어있는 더미헤드 추가 
        self.tail = None  # tail을 만든다.
        self.head.next = self.tail  # head 와 tail을 연결해놓는다.
        
    def traverse(self):
        my_list = []
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
            my_list.append(curr.data)
        return my_list 
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:  # start from at 0 (dummy)
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next  # 앞에서부터 순차탐색해야 한다 
            i += 1

        return curr
    
    # 추가된 메서드
    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:  # 맨 마지막노드면 tail 조정
            self.tail = newNode 
        prev.next = newNode
        self.nodeCount += 1
        return True
    
    # insertAfter를 활용하여 위에 insertAt보다 더 간결해진 코드
    # (1) pos 범위 조건을 확인
    # (2) pos == 1, head뒤에 새 node 삽입 
    # (3) pos == nodeCount + 1, prev = self.tail (순차탐색필요X)
    # (4) 그렇지 않으면 prev = getAt() 순차탐색
    
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        
        # pos == 1 이고, nodecount 가 0인경우에는 빈 리스트라는 소리...
        if pos != 1 and pos == self.nodeCount + 1:  # 맨 끝에 삽입, 빈 리스트체크
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)
    

        # prev가 마지막노드일 때 prev.next == None, 삭제할 노드없음, return None
        # 리스트 맨 끝의 node 삭제할때, tail 조정필요
    def popAfter(self, prev):
        if prev.next == None : 
            return None
        curr = prev.next
        
        if curr.next == None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = curr.next
            
        self.nodeCount -= 1
        return curr.data

    # popAfter 를 활용해서 더 간단하게 만듬, tail 을 따로 조정할 필요없음
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount :
            raise IndexError
        
        if pos == 1 and self.nodeCount == 1:
            prev = self.head
        else:
            prev = self.getAt(pos-1) 
        return LinkedList.popAfter(self, prev)


# # Doubly Linked Lists

# In[71]:


class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None 
        self.next = None 


# In[72]:


# 리스트 처음과 끝에 dummy node를 두자 (모두 같은모양으로)

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
        
    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        my_list = []
        curr = self.tail.next
        while curr.prev.prev:
            curr = curr.prev
            my_list.append(curr.data)  #data만 append시켜야함 유의
        return my_list
        
        
    def insertBefore(self, next, newNode):  # 4개의 링크, 순서주의 조정
        prev = next.prev
        newNode.prev = prev  # 우선 newNode의 링크를 연결 
        newNode.next = next
        prev.next = newNode  # 기존 링크차단
        next.prev = newNode  # 기존 링크차단
        self.nodeCount += 1
        return True
    
    def insertAfter(self, prev, newNode):  
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1  # 항상 이런 것은 잘 변경해줘야 한다.
        return True
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr
    
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)
    
    def popAfter(self, prev):  # prev 다음 노드삭제
        curr = prev.next
        next = prev.next.next
        
        prev.next = next
        next.prev = prev
        
        self.nodeCount -=1
        return curr.data
    
    def popBefore(self, next):  # next전 노드삭제
        curr = next.prev
        prev = next.prev.prev
        
        prev.next = next
        next.prev = prev
        
        self.nodeCount -=1  
        return curr.data
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos-1)  
        return self.popAfter(prev) 
    
    def concat(self, L):
        
        last = self.tail.prev
        first = L.head.next
        
        last.next = first
        first.prev = last 
    
        self.tail = L.tail
        self.nodeCount += L.nodeCount


# In[73]:


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')


# In[74]:


DL = DoublyLinkedList()
DL.insertAt(1,a)
DL.insertAt(2,b)
DL.insertAt(3,c)
DL.popAt(3)


# (잘못된 코드) 처음 내가 작성했던 코드 
# 
#     def popAfter(self, prev):
#         curr = prev.next
#         next = prev.next.next
#         
#         next = prev.next
#         prev = next.prev
#         
#         self.nodeCount -=1
#         return curr.data
# 
# - 어떤 변수의 값을 조정해줘야 할 지 잘 생각해보면 된다. 
# 
