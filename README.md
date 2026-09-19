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
