tab01 <<- matrix (c(5,2,4,6,1,3), ncol=6)
#tab01 <<- matrix (c(6,5,4,3,2,1), ncol=6)
#tab01 <<- matrix (c(1,2,3,4,6,5), ncol=6)
a1 <<- ncol(tab01)
	w <<- 1
	f <<- 1
for (i in 1:a1){
  if(i == 1)
  {print(tab01)}
  cat("for:",f,"\n")
  s1 <- w
a1 <- ncol(tab01)
a2 <<- a1 - 1
	while(a2 > 0){
		if(tab01[1,a1] < tab01[1,a2]){
		p1 <- tab01[1,a1]
		p2 <- tab01[1,a2]
		tab01[1,a1] <- p2
		tab01[1,a2] <- p1
		a1 <- a1 - 1
		a2 <- a2 - 1
  cat("while",w,":",tab01,"\n")
  w <- w+1
		if(a2 == 0)
		{break}}
		if(tab01[1,a1] >= tab01[1,a2]){
		a1 <- a1 - 1
		a2 <- a2 - 1
			if(a2 == 0)
			{break}}}
  f <- f+1
  s2 <- w
if(s1 == s2)
{break}}
print(tab01)
