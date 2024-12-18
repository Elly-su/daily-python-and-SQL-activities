---
title: "Practical Activity  3 Report"
author: "Elly Ochieng"
date: "`r Sys.Date()`"
output:
 pdf_document: default
---

  
#This is to load the required libraries to handle this assignment
library(readxl)  
library(dplyr)    
library(ggplot2) 

# This is to load the dataset
Birthweight_data <- read_excel("C:/Users/ellywyx/OneDrive/Documenti/Birthweight_data.xlsx")
head(Birthweight_data)

# Creating new dataframes
id_t <- Birthweight_data
newborn_data <- Birthweight_data %>% select(id, contains("newborn"))
smokers_data <- Birthweight_data %>% filter(smoker == 1)
lowbwt_mage35_data <- Birthweight_data %>% filter(lowbwt == 1, mage35 == 1)

# Adding total cigarettes column
Birthweight_data <- Birthweight_data %>%
  mutate(total_cigarettes = coalesce(mnocig, 0) + coalesce(fnocig, 0))

# Compute average birthweight
avg_birthweight <- Birthweight_data %>%
  group_by(mage35) %>%
  summarise(avg_birthweight = mean(Birthweight, na.rm = TRUE))

# Selecting and processing  specific variables used 
selected_data <- Birthweight_data %>%
  select(id, length, Birthweight, headcirumference, Gestation, smoker, mnocig, lowbwt, mage35) %>%
  mutate(
    id = as.factor(id),
    smoker = as.factor(smoker),
    lowbwt = as.factor(lowbwt),
    mage35 = as.factor(mage35)
  )

# Descriptive summaries
summary(selected_data)

# Graphical summaries
par(mfrow = c(2, 2))
hist(selected_data$Birthweight, main = "Histogram of Birthweight", xlab = "Birthweight")
boxplot(selected_data$Gestation, main = "Boxplot of Gestation", ylab = "Gestation")
barplot(table(selected_data$smoker), main = "Barplot of Smokers", ylab = "Count")
par(mfrow = c(1, 1))

# Scatterplot with regression line
ggplot(selected_data, aes(x = Gestation, y = Birthweight)) +
  geom_point() +
  geom_smooth(method = "lm", col = "blue") +
  labs(title = "Birthweight vs Gestation", x = "Gestation (weeks)", y = "Birthweight (grams)")

# Locust data
County <- c("Meru", "Embu", "Tharaka", "Isiolo", "Kajiado")
number_of_swarms <- c(90, 50, 42, 180, 120)
pie(number_of_swarms, labels = County, main = "Locust Swarms by County", col = rainbow(length(County)))
legend("topright", 
       legend = County,           # Names of the counties
       fill = rainbow(length(County)))  # Colors corresponding to each county

