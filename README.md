# Finite-Element-Analysis-of-Solid-Mechanics-Problem
Finite element simulation is done using Abaqus Standard. 
# First Problem
This problem has been taken from a research paper named “Experimental and numerical analyses of the structural response of adhesively reconstituted beech timber beams” by Van-Dang Tran, Marc Oudjene and Pierre-Jean Méausoone. The dimensions of the standard specimen are as shown below in the Figure. We will determine Load vs Displacement curve and compare it with published plot.
![dcb](https://user-images.githubusercontent.com/88960574/129481211-0b145efc-6536-4a15-9b92-ca98db3d3f81.png)
Results & Discussion:
Elastic material model has been assumed to describe the behaviour of the beech timber, while the behaviour of glue-lines has been modelled with the help of the Cohesive Zone Model (CZM). While simulating this problem, Elastic properties are only taken into consideration. This can be the possible reason for difference between Abaqus and Literature results.
![1st problem](https://user-images.githubusercontent.com/88960574/129481230-47cf7fd7-1e51-468f-a677-489afa1a81fb.png)

# Second Problem
A small copper ball of 5 mm diameter at 500 K is dropped into an oil bath whose temperature is 300 K. The thermal conductivity of copper is 400 W/mK, its density 9000kg/m3 and its specific heat 400 J/kgK.1f the heat transfer coefficient is 250 W/m2K. We have to determine temperature of the sphere after 30 seconds (Lumped capacity analysis is assumed to be valid).
Analytical Solution:
![2nd prob analytical](https://user-images.githubusercontent.com/88960574/129481340-5fdcd0b2-0ade-411a-83d9-8c09a138ab5f.png)
Results & Discussion:
![Transient heat](https://user-images.githubusercontent.com/88960574/129481647-20807e88-61eb-44dc-84d7-c78622ef850f.png)
The temperature distribution in the body is shown in the figure below. There is no temperature gradient setup within the body as lumped mass analysis is valid. So, the results seems to be as expected.
Percentage accuracy can be calculated as: (316.41/316.6)*100 = 99.939 or 99.94

# Third Problem
To find the stresses in the members of the truss subjected to load as shown below. (All the members have same cross sectional area with radius = 0.01m)
![truss](https://user-images.githubusercontent.com/88960574/129481585-1894ecab-eb21-4eb8-9407-1befd8238ec8.png)
Results & Discussion:
![2d truss](https://user-images.githubusercontent.com/88960574/129481624-c038a6b8-7549-440e-9ce1-42b09a17102d.png)
Stresses in various members of the truss is shown in the figure below. The stress values obtained from FEA simulation are almost equal to the analytical value. For e.g. Stress in member BD is 4.5032MPa which is in conjunction with value 4.504e+06Pa. We have considered the most stressed member of truss for accuracy calculation.

Percentage accuracy can be calculated as: (4.5032/4504)*100 = 99.982238 or 99.98
