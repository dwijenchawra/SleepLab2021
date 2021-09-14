library("nparACT")

imputed = "C:/Users/Zeitzer Lab/Desktop/DWIJEN_FILES/PycharmProjects/SleepLab2021/biobank_nparACTPreppedFiles"
#imputed = "C:/Users/Zeitzer Lab/Desktop/DWIJEN_FILES/PycharmProjects/SleepLab2021/ukbb_imputed"
#masked = "C:/Users/Zeitzer Lab/Desktop/DWIJEN_FILES/PycharmProjects/SleepLab2021/ukbb_masked"

# IMPUTED

files <- list.files(path=imputed, pattern="*.csv", full.names=TRUE, recursive=FALSE)

all_data <- data.frame()

counter <- 0

pb <- progress::progress_bar$new(
  format = " running imputed ivis [:bar] :percent eta: :eta",
  total = length(files), clear = FALSE, width= 60)


for (i in files){
  pb$tick()
  counter <- counter + 1
  print(i)
  fullfilename <- read.csv(i)
  filename <- strsplit(i, split = "/")
  filename <- filename[[1]][length(filename[[1]])]
  
  if (grepl("ZERODIV", filename)) {
    all_data <- rbind(all_data, cbind(filename = filename, setNames(data.frame(matrix(ncol = 7, nrow = 1)), c("IS", "IV", "RA", "L5", "L5_starttime", "M10", "M10_starttime"))))
  } else {
    single_result <- nparACT_base("fullfilename", SR = 2/60, plot = T)
    print(single_result)
    single_result <- cbind(filename = filename, single_result)
    all_data <- rbind(all_data, single_result)
  }
  
}

print(all_data)
write.csv(all_data, paste(imputed, "IVIS_data_ORIGINAL.csv", sep = "_"), row.names = FALSE)

# MASKED

files <- list.files(path=masked, pattern="*.csv", full.names=TRUE, recursive=FALSE)

all_data <- data.frame()

counter <- 0

pb <- progress::progress_bar$new(
  format = " running masked ivis [:bar] :percent eta: :eta",
  total = length(files), clear = FALSE, width= 60)

for (i in files){
  pb$tick()
  counter <- counter + 1
  print(counter)
  fullfilename <- read.csv(i)
  filename <- strsplit(i, split = "/")
  filename <- filename[[1]][length(filename[[1]])]

  if (grepl("ZERODIV", filename)) {
    all_data <- rbind(all_data, cbind(filename = filename, setNames(data.frame(matrix(ncol = 7, nrow = 1)), c("IS", "IV", "RA", "L5", "L5_starttime", "M10", "M10_starttime"))))
  } else {
    single_result <- nparACT_base("fullfilename", SR = 2/60, plot = F)
    print(single_result)
    single_result <- cbind(filename = filename, single_result)
    all_data <- rbind(all_data, single_result)
  }

}

print(all_data)
write.csv(all_data, paste(masked, "IVIS_data_masked.csv", sep = "_"), row.names = FALSE)
