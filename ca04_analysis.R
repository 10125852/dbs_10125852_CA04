# CA04 - Analysis
# 10125852 InSun Ahn

setwd("C:/Users/InsunHand/dbs_10125852_CA04")
my_data <- read.csv("commits.csv", header = TRUE, stringsAsFactors = F) 

library(dplyr)
library(tidyr)
library(qdap)
summary(my_data)
str(my_data)
names(my_data)

# Get date colum
str_date <- c(my_data[, "date"])
str_date

date_col_split <- strsplit(str_date, split = " ")

# Group data by Author.
byAuthor <- group_by(my_data, author)
unique(my_data$author)
unique(my_data$number_of__comment_lines)

# Filter out the records with unusual author names and verify them.
# Filter out the author seems not to be a real author.
url_author <- filter(my_data, author == "/OU=Domain Control Validated/CN=svn.company.net")
# Check comments in the subset if they are the same(auto-generated message.)
unique(url_author$comment)

# Filter out the author with a seemingly username and check comments.
ajon0002 <- filter(my_data, author == "ajon0002")
# Check comments in the subset if they are natural language.
unique(ajon0002$comment)

# Remove the url author records and leave only genuine authors.
new_data <- subset(my_data, author != "/OU=Domain Control Validated/CN=svn.company.net")
unique(new_data$author)

# number of commits grouped by author
summary1 <- summarise(byAuthor, count = n())

# Average commits by author
ave_commits <- 422/10

# Average of comment lines made by an author
ave_c_lines <- sum(my_data$number_of__comment_lines)/10


# Average number of comment lines.
ave_of_comment_lines <- mean(byAuthor$number_of__comment_lines) 
median_of_comment_lines <- median(byAuthor$number_of__comment_lines) 

# Group by Author on new data set.
NewbyAuthor <- group_by(new_data, author)
unique(new_data$number_of__comment_lines)

summary_new <- summarise(NewbyAuthor, count=n(), ave_c_lines = mean(new_data$number_of__comment_lines))
str(new_data)

date_split <- colSplit(new_data$date, col.sep = " ")
day_split1 <- colSplit(date_split$X4, col.sep = "(")
day_split2 <- colSplit(day_split1$X2, col.sep = ",")

str(day_split2)

# Data cleansing and pre-processing

as.character(date_split$X1)
as.Date(date_split$X1)

total <- cbind(new_data, as.Date(date_split$X1))
total2 <- cbind(total, as.character((day_split2$do.call..rbind...svar.)))

names(total2)
colnames(total2)

colnames(total2)[6] <- "date"
colnames(total2)[7] <- "day"
colnames(total2)[4] <- "count_comment_lines"
colnames(total2)[2] <- "str_date"

my_final_data <- subset(total2, select = - str_date)
summary(data)
str(my_final_data)

mydate <- my_final_data$date
mycount <- count(my_final_data, vars = "revision")






