The Python code to reproduce simulations presented in Fig. 4 of Skowron et al. (2019)

The code in [spiral_arms_now.py](../fig4/spiral_arms_now.py) will create output file with the centers of spiral arm structure at the current time. To get spiral arms at any time before use [spiral_arms_earlier.py](../fig4/spiral_arms_earlier.py) with a proper parameter in Myrs.

Use ../fig4/generate_64Myr.py to generate example of a star formation burst 64 Myrs before now. This will create an output file with positions in column 1-4 and evolved positions up to the current epoch in columns 5-8. Similarly for other proposed times: [generate_113Myr.py](../fig4/generate_113Myr.py) and [generate_175Myr.py](../fig4/generate_175Myr.py).

