
x <- c(1, 2, 7, 5, 8, 77)

oddcount <- function(x) {
  k <- 0
  for (n in x) {
    if (n %% 2 == 1)
      k <- k+1
  }
  return (k)
}

oddcount(x)
