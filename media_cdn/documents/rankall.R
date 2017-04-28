rankall <- function(outcome, num = "best") {
  ## Read outcome data
  dataset <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  ## Check that state and outcome are valid
  if (outcome == "heart attack"){
    column <- 11
  }else if (outcome == "heart failure"){
    column <- 17
  }else if (outcome == "pneumonia"){
    column <- 23
  }else{
    stop('invalid outcome')
  }
  ## For each state, find the hospital of the given rank
  states <- split(dataset, dataset$State)
  #total <- data.frame()
  total <- data.frame( "hospital" = character(0), "state" = character(0), stringsAsFactors=FALSE)
  
  for (name in names(states)) {
    
    states[[name]][, column] <- as.numeric(states[[name]][, column])
    x <- is.na(states[[name]][, column])
    not_missing_dataset <- states[[name]][!x, ]
    
    result <- not_missing_dataset[order(not_missing_dataset[,column], not_missing_dataset$Hospital.Name), , drop = FALSE]
    result$Rank <- 1:nrow(result)
    
    if (num == "best"){
      selection <- 1
    }else if (num == "worst"){
      selection <- nrow(result)
    }else{
      selection <- num
    }
    
    if (selection > nrow(result)){
      final_res <- NA
    }else{
      final_res <- result[result$Rank == selection, 'Hospital.Name']
    }
      
    total[nrow(total) + 1, ] <- c( final_res, name)
  }
  
  ## Return a data frame with the hospital names and the
  total
  ## (abbreviated) state name
}