import networkx as nx
import numpy as np

class ZeroShotClassifier():

    def __init__(G):
        self.Graph = G

    def predict(token, label):

           unique = {}
            for k in range(0, len(tokens)):

                if tokens[k] in unique:
                    unique[tokens[k]] += 1
                else:
                    unique[tokens[k]] = 1
            unique_tokens = list(unique.keys())

            intersection = {}
            #degree_list = {}
            degree_list = []
            label_neighbors = list(self.Graph.neighbors(label))
            
            w = []
            for word in unique_tokens:
                try:
                    
                    if word in label_neighbors:
                        intersection[word] = 1
                        degree = self.Graph.in_degree(word)
                        degree_log = f(degree)
                        degree_list.append(degree_log)
                        w.append((word, label))
                    
                    else:
                        neigbors = list(G.neighbors(word))

                        for n in neigbors:
        
                            
                            if n in label_neighbors:
                                intersection[n] = 1
                                degree = self.Graph.in_degree(n)
                                degree_log = f(degree)
                                degree_list.append(degree_log)
                                w.append((word, n, label))
                            else:
                                intersection[n] = 0
                except nx.NetworkXError:
                    pass
            return degree_list, intersection, w

    def f(node):
        l = np.log(node)
        return l