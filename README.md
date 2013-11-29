k-means
=======

Algoritmo K-Means

Agrupa vectores de mas de 2 dimenciones,en una cantidad de cluster determinada.


Class: 

        k_means(narray, n_cluster)
        
      
Parameters:

            narray; Arreglo de tipo numpy, con un tamaño mayor a 2 dimenciones
                    y cada elemento mayor a 1 dimencion.
                    array = [(x,y), (x+1,y+1), (x+2,y+2)]
                    
            n_cluster; numero de cluster deseados,si no existe el parametro
                       la clase lo calcula en referencia a la data entrante.
                       no puede ser mayor a la dimencion del arreglo.
                       
Example:        
        
         import k_means
         
             data = np.array([[1, 1], [2, 1], [1, 3], [3, 3], [4, 5], [4, 4], [5, 3]])
             kmeans = k_means.k_means(data)
             grupos = kmeans.calculate()
             
             grupos ->
                       [[0 0]
                        [1 0]
                        [2 0]  
                        [3 1]
                        [4 1]
                        [5 1]
                        [6 1]]
                        
             calculate() retorna una matriz donde la columna 0 es el numero del vector y la
             columna 1 es el cluster asociado a dicho vector.
             
             Para obtener los clusters finales: get_cluster()
                        
             cluster 0 -> [[ 1.33333333  1.66666667]
             cluster 1 ->  [ 4.          3.75      ]]
              
              
             
             

        

