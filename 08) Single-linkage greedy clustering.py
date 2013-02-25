# Algorithms - design and analysis (Stanford), Part II.
# Programming Assignment 2: Single-linkage clustering

import sys

infinity = sys.maxint

def single_linkage_clusters(proximity_matrix, k):
    # Naive O(n^3) single linkage clustering algorithm

    n = len(proximity_matrix)
    clusters = range(n)
    
    for _ in xrange(n-k):
        _, clusters_to_merge = spacing_function(proximity_matrix, clusters)
        for i in xrange(n): # Merging clusters
            if clusters[i] == clusters_to_merge[1]:
                clusters[i] = clusters_to_merge[0]
                
    return clusters
                
    
def spacing_function(proximity_matrix, clusters):
    n = len(proximity_matrix)
    spacing = infinity
    clusters_to_merge = (None, None)
    for i in xrange(n):
        for j in xrange(i+1, n):
            if clusters[i] != clusters[j] and proximity_matrix[i][j] < spacing:
                spacing = proximity_matrix[i][j]
                clusters_to_merge = (clusters[i], clusters[j])
    return spacing, clusters_to_merge
    
    
def main():
    
    f = open('clustering1.txt')
    
    n = int(f.readline())
    k = 4
    proximity_matrix = [[None for _ in xrange(n)] for _ in xrange(n)]
    for line in f:
        v1, v2, d = [int(x) for x in line.split()]
        proximity_matrix[v1-1][v2-1] = proximity_matrix[v2-1][v1-1] = d
        
    clusters = single_linkage_clusters(proximity_matrix, k)
    
    spacing, _ = spacing_function(proximity_matrix, clusters)
    print 'Spacing = %i' % spacing
    

main()
