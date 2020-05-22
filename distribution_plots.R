###
### Generate Data distribution plots
### Author: Jared Sharpe
### Plots are saved to .png files.

install.packages(c('dplyr','stringr','readxl','ggplot2','ggthemes'),dependencies = F, repos = "http://cran.us.r-project.org" )

library(dplyr)
library(stringr)
library(readxl)
library(ggplot2)
library(ggthemes)

## Compile store data and display distribution of promotions
files <- list.files(paste0(getwd(),"/Data"), pattern = "_Data.xlsx", full.names = TRUE)

## Our Master data set 
data_master = as.data.frame(matrix(nrow = 0, ncol = 10))
c_names <- c("Index","Week","year","retailer","Free Shipping",	"code",	"Minimum Free Shipping",	"Retailer Style",	"Product",	"Promotion")
colnames(data_master) <- c_names

## Compile....
for (f in files){
  #print(f)
  data = read_xlsx(f)
  colnames(data) <- c_names
  data_master = rbind(data_master,data)
  
}

## Reset Factors for plotting and data management
factor_cols <- c("Week","year","retailer","Retailer Style","Product")
data_master[factor_cols] <- lapply(data_master[factor_cols],as.factor)



## How much data is there for each retialer for each product category
pos_data_points_product <- data_master %>%
  group_by(retailer, Week, Product) %>%
  mutate(ObservedPromotions = sum(Promotion)) %>%
  ungroup()

pos_data_points_product %>%
  ggplot()+
  geom_bar(aes(x=Week,y=ObservedPromotions, fill = Product),stat = 'identity', position = 'dodge') +
  facet_wrap(pos_data_points_week$retailer) +
  scale_y_continuous(name = "Observed Promotions by Product") +
  theme(axis.title.y = element_text(face = "bold", size = 18),
        axis.title.x = element_text(face = "bold", size = 18),
        axis.text.x = element_text(size = 2),
        axis.text.y = element_text(size = 16),
        strip.text = element_text(size = 18),
        legend.text = element_text(size = 18),
        legend.title = element_text(face = "bold", size = 18),
        legend.position = 'bottom')
ggsave("Observed_Promotions_by_Product.png", dpi = 'retina', scale = 2)


## How much data is there for each retailer for each year:
pos_data_points <- data_master %>%
  group_by(retailer, year, Product) %>%
  mutate(ObservedPromotions = sum(Promotion))

## Plot Observed Promotions by Year
pos_data_points %>%
  ggplot()+
  geom_bar(aes(x=year,y=ObservedPromotions, fill = Product), stat = 'identity', position = 'dodge')+
  facet_wrap(pos_data_points_week$retailer) +
  scale_y_continuous(name = "Observed Promotions by Product") +
  theme(axis.title.y = element_text(face = "bold", size = 18),
        axis.title.x = element_text(face = "bold", size = 18),
        axis.text.x = element_text(size = 6),
        axis.text.y = element_text(size = 16),
        strip.text = element_text(size = 18),
        legend.text = element_text(size = 18),
        legend.title = element_text(face = "bold", size = 18),
        legend.position = 'bottom')
ggsave("Observed_Promotions_by_Year_Bar.png", dpi = 'retina', scale = 2)



