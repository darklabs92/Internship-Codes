library(smappR)
library(twitteR)
library(ROAuth)

ckey <- c("2UYdNCfHpmfzOIHKzKqVGFTE6","SYAvckFdp4ac1OxTyNEIiC0Wy","UTsgj7mjFCyutURQ9hFLUsJx6","yRUjMx3KWimhurc4fEOT8syqq")
csecret <- c("Gn87XSc1hLxbt8mbk9cQ4fmR9cKeOToIR9Ei2XKMt3KI7u0hUL","sTTddY36IcAozFHNr0gdRfs1to4Pg3CfEEqsllSGpCEBSxIywX","vPwzl6L0hCtGMKGeIJHxPTcw6jOub4fB7NrOx6YQyuslU8sveK","XG4TN1atbIkt4nxMIcKIbbFr4EQQYxYuHKFP9aijLpmT29AhxG")
atoken <- c("16280903-EgpG7X9XQbmcajILrMAK7Tf6FOmqHEnNc8sCvZDbf","16280903-hNz3jkAo2PePYt42gF0MaJLurEd6VWV744X0N52DO","16280903-SHcxm2NHJy1CpFYa1muJ7tdulN99Dlhql45Nj5LpY","16280903-RvkGJ55mNd25DQiEplnd8a2OzIqroW4BoF63S7NZY")
asecret <- c("GWrIwseUzVQwxJx2L1VfkF4gBs9hNu6Bq1UbtjBSvmhSG","pCt3HJLZ0ia3dlGQqAfmkY6erKIFaxtvpeH6CXwy5e5SG","ehoStGnleKxgLl6tKxrwUjgWTTJ3rKp5PWhCHmKF2NTTf","oqWZg5sdVQkkFITq8VmQ2o7uTo599duFehU6tJ3uWKCtZ")

consumerKey <- ckey[1]
consumerSecret <- csecret[1]
access_token <- atoken[1]
access_token_secret <- asecret[1]

setup_twitter_oauth(consumerKey,consumerSecret,access_token,access_token_secret)

followers = getFollowers(screen_name = "awryaditi", oauth_folder="C:\\Users\\Vidyut Singhania\\Downloads\\New_Business_Cases\\twitter_research\\Twitter\\ibt2")

follow <- split(followers, ceiling(seq_along(followers)/100))

for (i in follow) {
  t=i[1]
  for (j in i) {
    t=paste(t,j,",")
  }
  users <- getUsersBatch(t)
} 
