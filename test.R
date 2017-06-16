# Title     : TODO
# Objective : TODO
# Created by: Diuy
# Created on: 2017/6/16


#print(1)
#list <- list(1,2,3,4)
#print(list)

# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))

# Create the data frame.
BMI <- 	data.frame(
   gender = c("Male", "Male","Female"),
   height = c(152, 171.5, 165),
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)

print(ls())

print(.libPaths())