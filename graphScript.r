library(ggplot2)

combo1 <- read.csv(file = "C://Users//Luke//Desktop//combo1.csv")

comp <- ggplot(data=combo1, aes(x=Year, y=Citation_Count, fill=Author)) +
  geom_bar(stat="identity", position=position_dodge())

png(filename = "C://Users//Luke//Desktop//plot.png")
plot(comp)
dev.off()