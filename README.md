# Prob_fwding
Required packages
1. numpy
2. mpi
3. random

This repository has three subfolders corresponding to trees, grids and random geometric graphs. In each subfolder, the graph is specified using
M - Reduced adjacency matrix for a graph: The i-th roww of the matrix contains the neighburs of vertex i. Vertex 0 is often taken to be the source.

The main code which implements probabilistic forwarding to find the minimum forwarding probability is prob_fwding_parallel.py. To adapt it to different graph structures the matrix M has to be changed. To find the expected total number of transmissions, use trans_from_pkndelta_parallel.py with the probability values obtained using the corresponding prob_fwding_parallel.py code.

Use the command mpirun -n 100 python filename.py to run a file.

References:
1. B. R. Vinay Kumar and N. Kashyap, “Probabilistic forwarding of coded packets on networks” -  IEEE/ACM Transactions on Networking, vol. 29, no. 1, pp. 234-247, 2021. 
2. B. R. Vinay Kumar, N. Kashyap and D. Yogeshwaran, “An analysis of probabilistic forwarding of coded packets on random geometric graphs”, accepted at WiOpt 2021, Philadelphia, October 18-21, 2021. 
3. B. R. Vinay Kumar and N. Kashyap, “Probabilistic forwarding of coded 	packets on networks”, in Proc. 2019 International Symposium on 	Information Theory (ISIT 2019), Paris, Jul 7-12, 2019.	 
4. B. R. Vinay Kumar, R. Antony and N. Kashyap, “The Effect of 	Introducing Redundancy in a Probabilistic Forwarding Protocol”, in 	Proc. 2018 National Conference on Communications (NCC 2018), IIT- 	Hyderabad, Feb 25-28, 2018 
