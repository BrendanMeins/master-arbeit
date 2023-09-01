# Table of contents
1. [Public API](#public-api)
    1. [Functions](#functions)
        1. [minimize](#minimize)
    2. [Parameters](#parameters)
    3. [Enums](#enums)
       1. [Initialization](#initialization)
       2. [Selection](#selection)
       3. [Replacement](#replacement)
    4. [Objects](#objects)
       1. [Individual](#individual)
2. [Internal](#internal)

# Public API
## Functions

### minimize
TODO: Describe Function input / output

## Parameters

TODO: Describe parameters for the qubo matrix

## Enums

### Initialization

Enum to determine the initialization strategy.

|   Value   |                                          Description                                          |  
|:---------:|:---------------------------------------------------------------------------------------------:|
|  Random   | Algorithm will initialize N random individuals<br/>according to the population_size parameter |    
 

### Selection

Enum to determine the selection strategy. The selection strategy will also determine the 
pairing of individuals.

|  Value  |                                                                              Description                                                                               |  
|:-------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Ranking |          Algorithm will select N / 2 individuals not only <br/> by their fitness, but by their position in the <br/> population, less elitist than "Fittest"           |
| Fittest | Algorithm will select N / 2 individuals strictly by their<br/>  fitness, and will replace all individuals that are in the <br/>  worse half of the population. Elitist |


### Replacement

Enum to determine the replacement strategy. Some replacement strategies do not work for some selection strategies.
Read more in the usage seaction.

|       Value        |                                                             Description                                                              |  
|:------------------:|:------------------------------------------------------------------------------------------------------------------------------------:|
|    Competitive     | Parents and their direct offsprings compete<br/>against each other, the stronger individuals<br/>will taken for the next generation. |    
| ParentAndOffspring |          Parents will remain in the population, offsprings will <br/> replace individuals from the worse half of population          |    
|   OffspringOnly    |                                                Offsprings will replace their parents                                                 |    

## Objects

### Individual

Object with two attributes that represents a Solution to the
QUBO Matrix.

| Attribute  |  Type   |                       Description                       |
|:----------:|:-------:|:-------------------------------------------------------:|
|   Value    | ndarray | Array of 0 and 1 which<br/> represents the chromosome.  |
|  Fitness   |  Float  |  Return value of the cost function, e.g. QUBO Matrix.   | 


# Internal