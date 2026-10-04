# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under Pw<n>/Lab <X>/

## Setup
Create the environment for a given lab: 
    conda env create -f PW<n>/Lab <X>/environment.yml
    conda activate cspc




## PW1 - Lab A: REproducible Foundations

**What I build:**
- A radioactive decay simulation with 2 implementations(pure-python loop and vectorised numpy) plus tests to validate correctness and script to compare their performance

**Speed comparison (loop vs numpy):**
-loop: 1.9479s
-numpy: 0.0002s
-speed-up: 10316.4x faster

**Tests:** all passing? yes

**Conclussion:**
-All 3 tests passed, confirming that simulation correctly rejects invalid input(negative decay rate) and that its statistical output matches the theoretical decay law within tolerance. Numpy version is much more faster than pure-python loop because it replaces per-atom python-level iteration with a single vectorised call that operates on the whole population at once. this showed how much overhead comes from python`s loop itself, and why numpy is essntial for simulations at realistic scale

## PW1 - Lab B: Data, Plotting, and Automation

**What I build:**
- loaded observed decay data from "decay_observed.csv" and plotted it against the analytical decay laq N0*e^(-lambda*t) as a shared axis 1x2 figure, then wrapped the whole thing in a one-rule Snakemake pipeline

**Observed vs analytical comparison:**
- The observed points closely follow the analytical curve across the whole range both starting near N0 = 5000 and dropping off with the same shape
- Small deviations appear at low counts (t>15), where the data gets noisier -expected, since low counts carry more relative statistical noise

**Automation (Snakemake):** 
- one rule ("plot") builds "figure.png" from "decay_observed.csv" by rummimg "plot.py"
- Confirmed it rebuilds after deleting "figure.png" and does nothing on a repeat run when nothong has changed(Snakemake compares file timestamps, so unchanged inputs mean no work)

**Conclussion:**
-The observed data matches the analytical decay law well, confirming the process follows simple exponential decay wuth lambda = 0.3
- learned how Snakemake avoids unnecessary reruns bytracking input/output timestamps, keeps a multistep pipeline consistent with a single command

## PW2 - Lab A: from noisy position to velocity and acceleration

**What I build:**
- Starting from noisy height measurements of falling object , I calculated its velocityand acceleration, then added the nois acceleration back up to see if I could rebuild the original height

**What I measured:**
-average acceleration: -8.5797m/s^2
-standart deviation: 28.716m/s^2
-largest difference: 0.63975 m

**Why acceleration came out so noisy:** 
The height data looked fairly smooth, but acceleration is calculated by comparing difference between nearby points - and doing that twice in a row(once for velocity, again for acceleration) makes any small error in the original measuremenets get bigger each time. So even though position data looked clean accceleration ended up jumping around a lot

**what happened when I added everything back up:**
When I summed the noisy acceleration values back up to get velocity, then position again, result ended up very close to the original height data(largest difference 0.639m) This makes sense because adding numbers together tend to cancel out random noise , so errors are a bit too high, some a bit too low and they average each other out. So going backwards(integration) actually cleaned the noise up while going forward made it worse 
**Conclussion:**
-This lab showed that these operations behave in opposite ways with noisy data: comparing differences(differentiating) makes noise worse while adding values up (integrating) makes it better even with the exact same noisy numbers. Acceleration I measured still matched graviy`s real value 

## PW2 - Lab B: Optimisation in Chemistry

**What i build**
Compared gradient descent, Newton's method and SLSQP, then used optimisation for reaction rate, chemical equilibrium and titration.

**Part 2 - Optimisation methods:**
For f(x), all three methods reached x = 3(approximately)
For g(x), the result depended on the starting point. Newton's method could reach another stationary point, while gradient descent and SLSQP reached local minima. Smaller learning rates made gradient descent slower.

**Part 3 - Reaction rate:**
Fitted the first-order reaction model to the measured data using SLSQP. Fitted rate constant: k = 0.25(approximately)

**Part 4 - Chemical equilibrium:**
Used Newton's method and SLSQP to find the equilibrium extent. Both methods gave x = 0.60(approximately)
Equilibrium amounts:
    H2 = 0.39 mol
    I2 = 0.39 mol
    HI = 1.21 mol

**Part 5 - Titration(bonus):**
Used the pH slope to find the equivalence point.
Equivalence point: 50 ml

**Counclusion:**
This lab showed how different optimisation methods can be used for both mathematical functions and real chemistry problems. The starting point and learning rate can affect the optimisation result.

