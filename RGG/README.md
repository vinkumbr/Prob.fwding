Details of different files with typical procedure to run codes
1. Generate the reduced adjacency matrix for a RGG using RGG_generate.py. Provide the intensity, the size of the area where it should be generated and the radius. You can use multiple_RGG_gen.py to generate multiple reduced adjacency matrices for RGGs.
2. This will be stored in ./AdjMats/test_formula/ folder
3. Run the probabilistic forwarding algorithm from prob_fwding_parallel_recs_avg.py. Set the parameters between lines 87-94.
4. The prob_fwding _parallel_recs_avg.py file needs to be run for each value of n separately, changing it when the pkndelta value has been found for a  particular value of n: the number of coded packets. You can use prob_fwding_parallel.py if you want to run it on a single realization of the RGG.
5. The pkndelta values will be displayed on screen as well as appended onto pkndelta.txt file. Remember to clear this file when starting with a new adjacency matrix ensuring that older values have been stored elsewhere.
6. Copy the pkndelta values into Line 99 of trans_from_pkndelta_avg_RGG.py file and set the correct adjacency matrix on Line 87. Run it to obtain tau_kndelta values. These are appended to tau_kndelta.txt and are also displayed on the console. You can use trans_from_pkndelta_parallel.py if running on a single realization of the RGG.
7. Copy the pkndelta values from pkndelta.txt and tau_kndelta values from tau_kndelta.txt into prob_fwding_results.py file. Running this file generates results into simu_results.json.
8. Plot the results of probabilistic forwarding by running plot_simu_results.py which takes data from simu_results.json and outputs the plot for pkndelta and tau_kndelta.

For the percolation probability theta(lambda)
1. Select the area size and the lambda values on lines 96,98 of the theta_lambda_parallel_mpi.py file and run it.
2. This will generate the theta(lambda) values on the console. It also updates it on the theta_lambda_251.json file.
