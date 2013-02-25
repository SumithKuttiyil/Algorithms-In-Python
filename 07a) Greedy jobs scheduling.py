'''
Algorithms - design and analysis (Stanford), Part II.

Programming Assignment 1-1:
Greedy jobs scheduling

@author: Mikhail Dubov
'''

def greedy_minimal_weighted_sum(jobs, greedy_criterion, ties_criterion):
    
    # correct, since .sort() is stable
    jobs.sort(key = ties_criterion)
    jobs.sort(key = greedy_criterion)
    
    timeline = 0
    sum = 0
    for w, l in jobs:
        timeline += l
        sum += w * timeline
        
    return sum
    
    
def main():
    
    f = open('jobs.txt')
    
    n = int(f.readline())
    
    jobs = []
    for line in f:
        w, l = [int(x) for x in line.split()]
        jobs.append((w, l))
        
    greedy_criterion_1 = lambda (w, l): -(w - l)     # not always correct
    greedy_criterion_2 = lambda (w, l): -float(w)/l  # always correct
    ties_criterion = lambda (w, l): -w               # matters for criterion 1 only
    
    print 'Greedy algorithm #1: %i' % greedy_minimal_weighted_sum(jobs, greedy_criterion_1, ties_criterion)     
    print 'Greedy algorithm #2: %i' % greedy_minimal_weighted_sum(jobs, greedy_criterion_2, ties_criterion)  


main()
