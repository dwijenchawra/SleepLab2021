# SleepLab2021

This repository hosts all the scripts and code I've written for my summer internship at the Stanford Sleep Sciences Lab. I worked extensively with Python, and a little bit of R. I was responsible for processing actigraphy data from the UK BioBank study. The .cwa files were processed using the R library GGIR, and analyzed in Python to produce IV/IS values. Clean actigraphy files were then masked in different intervals to simulate missing data, then imputed using different algoritms to determine <b>how much missing data is too much?</b>

Languages and Libraries used:
- Python
  - numpy
  - pandas
  - datetime
  - os
  - tqdm
- R
  - GGIR
  - nparact
