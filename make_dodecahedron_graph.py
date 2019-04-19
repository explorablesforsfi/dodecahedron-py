import json
import numpy as np
import matplotlib.pyplot as pl
import networkx as nx

# get the graph from networkx
G = nx.dodecahedral_graph()

# divide the whole circle in 5 parts
d_theta = 2*np.pi/5

# start at 90degrees ~(x=0, y=1)
theta_offset = np.pi/2

# iterate through all four rings and define angular offset
angle_offset1 = -0.5
inner1 = [1,0,19,3,2]

angle_offset3 = -1
outer1 = [9,11,17,5,7]

angle_offset2 = -0.5
inner2 = [8,10,18,4,6]

angle_offset4 = -1
outer2 = [13,12,16,15,14]

ring_nodes = [ inner1, inner2, outer1, outer2 ]
angles = [angle_offset1, angle_offset2, angle_offset3, angle_offset4]
radii = np.array([ 1,2,3,5 ])

x = {}
y = {}

# iterate and compute node positions
for i in range(4):
    r = radii[i]
    nodes = ring_nodes[i]
    theta0 = theta_offset + d_theta * angles[i]

    for inode, node in enumerate(nodes):
        theta = theta0 - inode * d_theta 
        x[node] = r*np.cos(theta)
        y[node] = r*np.sin(theta)

# write node positions to graph
nx.set_node_attributes(G, x, 'x')
nx.set_node_attributes(G, y, 'y')


# draw
fig, ax = pl.subplots(1,1, figsize=(5,4))
ax.axis('equal')
nx.draw(G,
        pos={node:(x[node],y[node]) for node in G.nodes()},
        node_color="#1b9e77",
        edge_color="#333333",
        node_size=200,
        )

# save in json
node_link_data = nx.node_link_data(G)

with open('dodecahedron.json','w') as f:
    json.dump(node_link_data,f,indent=2,sort_keys=True)

fig.savefig('dodecahedron.png',dpi=150)

pl.show()



