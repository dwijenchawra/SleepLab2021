library("nparACT")

files <- list.files(path="C:/Users/Jamie/PycharmProjects/SleepLab2021/nparACTPreppedFiles", pattern="*.csv", full.names=TRUE, recursive=FALSE)

all_data <- data.frame()

counter <- 0

for (i in files){
  counter <- counter + 1
  print(counter)
  fullfilename <- read.csv(i)
  filename <- strsplit(i, split = "/")
  filename <- filename[[1]][length(filename[[1]])]
  
  if (grepl("ZERODIV", filename)) {
    all_data <- rbind(all_data, cbind(filename = filename, setNames(data.frame(matrix(ncol = 7, nrow = 1)), c("IS", "IV", "RA", "L5", "L5_starttime", "M10", "M10_starttime"))))
  } else {
    single_result <- nparACT_base("fullfilename", SR = 12/60, plot = F)
    print(single_result)
    single_result <- cbind(filename = filename, single_result)
    all_data <- rbind(all_data, single_result)
  }
  
}

print(all_data)
write.csv(all_data,"C:/Users/Jamie/PycharmProjects/SleepLab2021/nparACTPreppedFiles/IVIS_data_completefiles.csv", row.names = FALSE)

