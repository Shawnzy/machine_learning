This file contains the instructions for how to run the code for Assignment 2

Important Notes
1) This project uses a modified version of ABAGAIL, located in the ABAGAIL sub-folder
2) To run the Jython files, please modify the files (line 5 for non-neural network experiments and line 9 for neural network experiments) so that the ABAGAIL.jar file is in the system path.

Reports:
1) smailo3-analysis.pdf - Assignment 2 report

Code Files:
1) NN0.py - Code for Backpropagation training of neural network
2) NN1.py - Code for Randomised Hill Climbing training of neural network
3) NN2.py - Code for Simulated Annleaing training of neural network
4) NN3.py - Code for Genetic Algorithm training of neural network
5) continuouspeaks.py - Code to use Randomised Optimisation to solve the Continuous Peaks problem
5) flipflop.py - Code to use Randomised Optimisation to solve the Flip Flop problem
6) tsp.py - Code to use Randomised Optimisation to solve the Traveling Salesman Problem
7) plot_p1.ipynb and plot_p2.ipynb - Code to do the plotting and computation of summary statistics
8) requirements.txt - All required python libraries to run the scripts (pip3 install -r requirements.txt)

There are also a number of folders
1) part1_plots and part2_plots - contains that plots outputted by plot_p1.ipynb and plot_p2.ipynb
2) NNOUTPUT - output folder for the Neural Network experiments
3) CONTPEAKS - output folder for the Continuous Peaks experiments
4) FLIPFLOP - output folder for the Flip Flop experiments
5) TSP - output folder for the Traveling Salesman Problem experiments
6) ABAGAIL - folder with source, ant build file, and jar for ABAGAIL

Data Files
1) c_test.csv - The test set
2) c_trg.csv - The training set
3) c_val.csv - The validation set


Java code was built with ant 1.10.1 on java 1.8.0_121.
The code files in the code files section were written in Jython 2.7.0.

Plotting code was  written in Python 3.6
