# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under Pw<n>/Lab <X>/

## Setup
Create the environment for a given lab: 
    conda env create -f PW<n>/Lab <X>/environment.yml
    conda activate cspc

---

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
