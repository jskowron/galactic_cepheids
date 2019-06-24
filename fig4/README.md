The Python code to reproduce simulations presented in Fig. 4 of Skowron et al. (2019)

The code in [spiral_arms_now.py](../fig4/spiral_arms_now.py) will create output file with the centers of spiral arm structure at the current time. To get the spiral arms outline at any time before now, use [spiral_arms_earlier.py](../fig4/spiral_arms_earlier.py) with a proper parameter (in Myrs).

Use [generate_64Myr.py](../fig4/generate_64Myr.py) to generate an example of a star formation burst 64 Myrs ago. This will create an output file with the initial (birth) positions in columns 1-4 and the evolved positions (up to the current epoch) in columns 5-8. Similarly, for other proposed times, use: [generate_113Myr.py](../fig4/generate_113Myr.py) and [generate_175Myr.py](../fig4/generate_175Myr.py).

