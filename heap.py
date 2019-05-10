# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:31:45 2019

@author: DinoBob
"""

class max_heap:
    
    '''
    Indices of parent, left and right children of a node
    '''
    def parent(self, i):
        return int((i-1)/2)
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    
    
    
    def max_heapify(self, A, i):
        '''
        Assume all the array[i] children maintain the max heap property.
        Float down array[i] to make it also maintain max heap property.
        '''
        l = self.left_child(i)
        r = self.right_child(i)
        if l < len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            self.max_heapify(A, largest)
        return
    
    def build_max_heap(self, A):
        '''
        build a max heap from an array
        '''
        for i in range(int(len(A)/2) - 1,-1,-1):
            self.max_heapify(A, i)
            
    def heapsort(self, A):
        '''
        Sort with a heap
        1) Heapify the array
        2) Swap A[0] with A[len(A)-1] and pop A[len(A)-1)]
        3) Max heapify A[0]
        '''
        self.build_max_heap(A)
        sorted_A = []
        while len(A) > 1:
            A[0], A[-1] = A[-1], A[0]
            sorted_A.append(A.pop(-1))
            self.max_heapify(A,0)
        sorted_A.append(A[0])
        return sorted_A
    
    

class priority_queue(max_heap):
    
    def heap_max(self, A):
        '''
        Assume A is already max heapified, return the max
        '''
        return A[0]
    
    def heap_extract_max(self, A):
        '''
        Extract the max and keep the heap structure
        '''
        A[0], A[-1] = A[-1], A[0]
        m_heap = A.pop(-1)
        self.max_heapify(A, 0)
        return m_heap
    
    def heap_increase_key(self, A, i, key):
        '''
        Increase the key of node i and keep heap structure.
        Compare the new key with parent and bubble up
        Note: using -1 as index here will not work because of the while
        loop condition
        '''
        A[i] = key
        while A[i] > A[self.parent(i)] and i > 0:
            p = self.parent(i)
            A[i], A[p] = A[p], A[i]
            i = p
        
    def heap_insert(self, A, key):
        '''
        Insert a key into A and keep heap structure
        '''
        A.append(float('-inf'))
        self.heap_increase_key(A, len(A)-1, key)
        
        
        
            
        
if __name__ == '__main__' :           
    test = [11,1,3,2,16,9,10,14,8,7]



        