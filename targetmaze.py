

from dijkstar import Graph, find_path
import json
import urllib
import pprint

graph = Graph()

cost_func = lambda u, v, e, prev_e: e['cost']

graph.add_edge(-1, 0, {'cost':1, 'url':'https://www.codewithtarget.com/api/maze'})

def travelgraph( graph, previousnode, added ):
    
    for key in graph[previousnode].keys():
        

        r = urllib.urlopen( graph[previousnode][key]['url'] )
    
    
        jr = json.loads(r.read())

        if 'exits' in jr:

            for exit in jr['exits'].keys():

                nodenum = int(jr['exits'][exit].replace('https://www.codewithtarget.com/api/maze/', '' ))

                graph.add_edge(key, nodenum, 
                           {'cost':1, 
                            'url': jr['exits'][exit],
                            'direction': exit,
                            'raw': jr } )
           
                if nodenum not in added:
                    added.append(nodenum)
                    travelgraph( graph, key, added )
            

        elif 'howToWin' in jr:

            print ( 'goal node: %s' % graph[previousnode][key]['url'].replace('https://www.codewithtarget.com/api/maze/', '' ) )


added = []

travelgraph(graph, -1, added)


print ( find_path(graph, 1, 15, cost_func=cost_func) )

pprint.pprint ( graph.items() )


