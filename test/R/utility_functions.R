setwd("K:/Dropbox/Dropbox/Univer/II Anno/RW/Progetto");

# Aggregate datasets
get_aggregated_data <- function(my_df) {
  my_df[-which.min(my_df$x)];
  my_df[-which.max(my_df$x)];
  aggregate(my_df$elapsed, list(Label=my_df$label), mean)
}

# Load and aggregate datasets
load_datasets <- function(name) {
  for (i in seq(0,6)) {
    print(paste("Opening", paste0(getwd(), "/", name ,"/", toString(2**i), " thread/timetest.test")));
    x <- get_aggregated_data(read.csv(paste0(getwd(),
                                             "/", name ,"/", toString(2**i), 
                                             " thread/timetest.test")))
    x <- cbind(x, thread=rep(2**i, 16))
    assign(paste(name, 2**i, sep = ""), x, envir= .GlobalEnv);
    
  }
}

bind_total <- function(name) {
  total <- data.frame()
  for (i in seq(0,6)) { 
      total <- rbind(total, get(paste(name, 2**i, sep="")))
  }
  cbind(total, Name=rep(name, nrow(total)));
}


pumped_list <- function(a) {
  b <- rep("", length(a))
  idx <- order(c(seq_along(a), seq_along(b)))
  unlist(c(a,b))[idx]
}
interleave <- function(a, b) {
  idx <- order(c(seq_along(a), seq_along(b)))
  unlist(c(a,b))[idx]
}

