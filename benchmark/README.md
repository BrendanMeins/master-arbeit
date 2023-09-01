# Benchmark Library

A library that contains benchmark QUBO instances. Every Problem has 
a QUBO Matrix, a description, a minimum and a name. 

## Code Example

`
import benchmark
`

Get Available Problem names as array

`problem_names = benchmark.get_names()
`

Get a specific instance:

`instance = benchmark.get_instance(problem_names[0])
`