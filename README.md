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

        

