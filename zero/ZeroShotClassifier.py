import networkx as nx
import numpy as np
import pkg_resources
import pandas as pd

class ZeroShotClassifier():

    def __init__(self):

        resource_package = __name__
        resource_path = '/'.join(('graph', 'wordnet_graph_all.csv'))  # Do not use os.path.join()
        template = pkg_resources.resource_string(resource_package, resource_path)
        
        stream = pd.read_csv(template)
        N_all_data_nodes = stream[['node1', 'node2']]
        N_all_data_nodes = N_all_data_nodes.drop_duplicates()
        records = N_all_data_nodes.to_records(index=False)
        full_relations = list(records)
        self.Graph = nx.DiGraph(full_relations)

    def predict(self, token, label):

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
