# Experiment Selection Strategy

## Description

After each generation, parent individuals are selected to perform a crossover and thus produce offsprings for the next generation.
For this procedure, there are multiple different approaches. This experiment will test the strategy "selection fittest", where the better half of the population will strictly selected to perform crossover, and the offsprings will replace the worse half of the population.

The second strategy will rank the individuals by their fitness and then select individuals by their rank, where higher ranked individuals will have a better chance to reproduce than lower ranked individuals.

In general, the expected result is that the selection strategy with a higher pressure has a better convergence behaviour since deleting the worse half of the population will guide the population towards a solution. 

Another finding might be, that a selection with a high selection pressure offers these attributes aswell, but also leaves leaves the possibility for lower ranked individuals to reproduce and thus maintaining diversity in the gene pool.

## Execution

4 experiments will be carried out: 

1. Selection Fittest
2. Selection Ranking Low Pressure
3. Selection Ranking Medium Pressure
4. Selection Ranking High Pressure

Selection Fittest is the most elitist, removing all individuals in the worse half of the population

Strategies 2-4 use selection ranking with different selection pressure.


See <a href='https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)'>here</a> for more.

Every configuration will be executed against the same problem. Since the algrithm is probabilistic, every configuration will be executed multiple times and then the average result will be compared.

The mutation rate will be set to a medium rate of 5% for every experiment.

## Evaluation

The selection fittest strategy performed worse than all other experiments. Accordingly, the lack of diversity in the gene pool leads to early convergence of the algorithm. The other experiments with selection pressure had better results. However, there was no significant difference between selection with low pressure, medium pressure or high pressure. It seems that the presence of diversity its self is the important ingredient, rather than the actual pressure on the population.

Ranking by result quality, the result is, starting with the best one:

1. Low Pressure
2. Medium Pressure
3. High Pressure
4. Fittest

<img src='files/sum.png'>
