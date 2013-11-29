# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 17:41:19 2013

@author: Deltalo
"""
import numpy as np

class k_means:
    
    def __init__(self,array,n_cluster = False): 
        self.error_data(array)
        self.data = array
        self.clusters = []
        self.array_assignment = []
        self.array_assignment_old = []
        
        self.num_cluster = self.set_num_clusters(n_cluster)
        self.set_cluster()
        self.set_array_assignment()
        
    def set_num_clusters(self,n_clsuter):
        if(n_clsuter != False):
            if(n_clsuter > len(self.data)):
                n_cluster = int(np.sqrt(len(self.data)/2))
                if(n_cluster == 1):
                    n_cluster = 2
            return n_clsuter
        else:
            n_cluster = int(np.sqrt(len(self.data)/2))
            if(n_cluster == 1):
                n_cluster = 2
            return n_cluster                  
            
    def set_cluster(self):
        if(len(self.clusters) == 0):
            random_index = np.arange(0,len(self.data)) 
            random_index = np.random.choice(random_index,self.num_cluster,replace=False)
            for i in range(0,len(self.data)):
                for j in range(0,self.num_cluster):
                    if(random_index[j] == i):
                        self.clusters.append(self.data[i])
            self.clusters = np.row_stack(self.clusters)
        else:
            self.clusters = []
            for i in range(0,self.num_cluster):
                vect_select = []
                for j in range(0,len(self.array_assignment)):
                    if(self.array_assignment[j][1] == i):
                        vect_select.append(self.data[self.array_assignment[j][0]])
                vect_select = np.row_stack(vect_select)       
                vect_prom = np.mean(vect_select,axis = 0)
                self.clusters.append(vect_prom)
            self.clusters = np.row_stack(self.clusters)
                
    def get_cluster(self):
        return self.clusters
        
    def set_array_assignment(self):
        if(len(self.array_assignment) == 0):
            for i in range(0,len(self.data)):
                distances = []
                for j in range(0,self.num_cluster):
                    distances.append(self.distance(self.data[i],self.clusters[j]))
                min_distance = np.argmin(distances)
                self.array_assignment.append((i,min_distance))
            self.array_assignment = np.row_stack(self.array_assignment)
        else:
            self.array_assignment_old = self.array_assignment
            self.array_assignment = []
            for i in range(0,len(self.data)):
                distances = []
                for j in range(0,self.num_cluster):
                    distances.append(self.distance(self.data[i],self.clusters[j]))
                arg_min_distance = np.argmin(distances)
                self.array_assignment.append((i,arg_min_distance))
            self.array_assignment = np.row_stack(self.array_assignment)
            
    def get_array_assignment(self):
        return self.array_assignment
    
    def get_array_assignment_old(self):
        return self.array_assignment_old
    
    def distance(self,vector_1,vector_2):
        distance = 0
        for i in range(0,len(vector_1)):
            distance += (vector_1[i] - vector_2[i])**2
        return np.sqrt(distance)
        
    def calculate(self):
        while(not np.array_equal(self.array_assignment,self.array_assignment_old)):
            self.set_cluster()
            self.set_array_assignment()
        return self.array_assignment
        
    def error_data(self,array):
        if(len(array) < 3):
            raise NameError, 'Error de dimencion'
            
        
            
            
    
