The Python code to reproduce simulations presented in Fig. 4 of Skowron et al. (2019)

Use [do](../fg4/do) script to generate simulated data and to plot the results.

The code in [spiral_arms_now.py](../fig4/spiral_arms_now.py) will create output file with the centers of spiral arm structure at the current time. To get the spiral arms outline at any time before now, use [spiral_arms_earlier.py](../fig4/spiral_arms_earlier.py) with a proper parameter (in Myrs).

Use [generate_64Myr.py](../fig4/generate_64Myr.py) to generate an example of a star formation burst 64 Myrs ago. This will create an output file with the initial (birth) positions. Similarly, for other proposed times, use: [generate_113Myr.py](../fig4/generate_113Myr.py) and [generate_175Myr.py](../fig4/generate_175Myr.py).

The [evolve.py](../fig4/evolve.py) program will rotate the generated sample of stars from the past until current time. Provide generate\_\*.out file as an argument. See [do](../fg4/do) script for the example of use. 

The [plot.py](./plot.py) and [plot2.py](./plot2.py) scripts plot the simulations. The second script also takes the real data (from galactic\_cepheids\_*.dat files) and presents them along the simulations.
