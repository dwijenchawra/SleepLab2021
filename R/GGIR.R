rm(list=ls()) 

#install.packages("GGIR")
library("GGIR")

g.shell.GGIR(datadir="F:/dataggirtest",
             outputdir="F:/ggirmodifications",
             studyname="Jones 2019 check", #specify above
             mode=c(1,2,3,4),
             overwrite = TRUE, #overwrite previous milestone data? #default=FALSE
             do.imp=TRUE, # Do imputation? (recommended)
             idloc=1, #id location (1 = file header, 2 = filename)
             print.filename=TRUE,
             storefolderstructure = FALSE, 
             #-------------------------------
             # Part 1 parameters:
             #-------------------------------
             # Key functions: reading file, auto-calibration, and extracting features
             windowsizes = c(5,900,3600), #Epoch length, non-wear detection resolution, non-wear detection evaluation window
             do.cal=TRUE, # Apply autocalibration? (recommended)
             do.enmo = TRUE, #Needed for physical activity analysis
             do.anglez=TRUE, #Needed for sleep detection
             chunksize=1, #size of data chunks to be read (value = 1 is maximum)
             printsummary=TRUE, 
             #-------------------------------
             # Part 2 parameters:
             #-------------------------------
             # Key functions: Non-wear detection, imputation, and basic descriptives
             strategy = 2, #Strategy (see tutorial for explanation)
             ndayswindow=7, #only relevant when strategy = 3
             hrs.del.start = 1, # Only relevant when strategy = 2. How many HOURS need to be ignored at the START of the measurement?
             hrs.del.end = 1, # Only relevant when strategy = 2. How many HOURS need to be ignored at the END of the measurement?
             maxdur = 9, # How many DAYS of measurement do you maximumally expect?
             includedaycrit = 16, # number of minimum valid hours in a day to attempt physical activity analysis
             L5M5window = c(0,24), #window over which to calculate L5 and M5
             M5L5res = 10, #resolution in minutes of M5 and L5 calculation
             winhr = c(5,10), # size of M5 and L5 (5 hours by default),
             qlevels = c(c(1380/1440),c(1410/1440)), #quantiles to calculate, set value at c() if you do not want quantiles
             qwindow=c(0,24), #window over which to calculate quantiles
             ilevels = c(0,45.2,93.2,150,8000), #acceleration values (metric ENMO) from which a frequency distribution needs to be derived, set value at c() if you do not want quantiles
             mvpathreshold =c(100,120), #MVPA (moderate and vigorous physical activity threshold
             mvpadur=c(0,1,3,5,10), 
             #-------------------------------
             # Part 3 parameters:
             #-------------------------------
             # Key functions: Sleep detection
             timethreshold= c(5), #10
             anglethreshold=5,
             ignorenonwear = FALSE, # if TRUE non-wear is not detected as sleep (if FALSE then it will work with imputed data)
             #-------------------------------
             # Part 4 parameters:
             #-------------------------------
             # Key functions: Integrating sleep log (if available) with sleep detection, storing day and person specific summaries of sleep
             excludefirstlast = FALSE, # Exclude first and last night for sleep analysis?
             includenightcrit = 16, # number of minimum valid hours in a day to attempt sleep analysis
             def.noc.sleep = 1,
             outliers.only = TRUE,
             criterror = 4,
             relyonsleeplog = FALSE,
             sleeplogidnum = TRUE, # Is the participant in the sleep log stored as a number (TRUE) or as a character (FALSE)
             colid=1, #colomn in which the participant id or filename is stored
             coln1=2, #column number for first day
             do.visual = TRUE,
             nnights = 9, #number of nights in the sleep log
             IVIS.activity.metric=1,
             epochvalues2csv=TRUE,
             #-----------------------------------
             # Report generation
             #-------------------------------
             # Key functions: Generating reports based on meta-data
             do.report=c(2), #for what parts does and report need to be generated? (option: 2, 4 and 5)
             visualreport=FALSE,
             dofirstpage = FALSE, #first page of pdf-report with simple summary histograms
             viewingwindow=1, #viewingwindow of visual report: 1 centres at day and 2 centers at night
             IVIS_epochsize_seconds=3600,
             IVIS_windowsize_minutes=60, 
             epochvalues2csv=TRUE)
