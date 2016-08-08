if(!require(devtools)) {
  install.packages(c("devtools", "rjson", "bit64", "httr")); require(devtools)}

if(!require(twitteR)) {
  install.packages("twitteR"); require(twitteR)}

if(!require(smappR)) {
  install_github("smappR", "SMAPPNYU"); require(smappR)}

if(!require(plyr)) {
  install.packages("plyr"); require(plyr)}

if(!require(tm)) {
  install.packages("tm"); require(tm)}

if(!require(base64enc)) {
  install.packages("base64enc"); require(base64enc)}

if(!require("wordcloud")) {
  install.packages(c("wordcloud","tm"),repos="http://cran.r-project.org"); require("wordcloud")}

if(!require(httpuv)) {
  install.packages("httpuv"); require(httpuv)}

if(!require(ggplot2)) {
  install.packages("ggplot2"); require(ggplot2)}


#Setting up the OAuth Key 1
api_key <- ""

api_secret <- ""

atoken <- " "

atoken_secret <- ""

setup_twitter_oauth(api_key,api_secret,access_token=atoken)


#Setting up the OAuth Key 2
api_key1 <- ""

api_secret1 <- ""

atoken1 <- ""

atoken_secret1 <- ""

setup_twitter_oauth(api_key1,api_secret1,access_token=atoken1)


library(ROAuth)
requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"
consumerKey <- api_key1
consumerSecret <- api_secret1
my_oauth <- OAuthFactory$new(consumerKey=consumerKey, consumerSecret=consumerSecret, 
                             requestURL=requestURL, accessURL=accessURL, authURL=authURL)

my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))


setwd("C:\\Users\\Vidyut Singhania\\Downloads\\New Business Cases\\twitter research")
save(my_oauth, file="my_oauth")

m = getFollowers(screen_name = "McDonalds", oauth_folder="C:\\Users\\Vidyut Singhania\\Downloads\\New Business Cases\\twitter research")





# step 1: downloading list of friends for a user
user <- "sud47"
friends <- getFriends(screen_name=user, oauth_folder="C:\\Users\\Vidyut Singhania\\Downloads\\New Business Cases\\twitter research")

# step 2: estimate ideology
results <- estimate.ideology(user, friends)

# display trace plot to check convergence
traceplot.ideology(results)

# comparing with other ideology estimates
ideology.plot(results)

# downloading list of followers of a given user
followers <- getFollowers(screen_name=user, oauth_folder="C:\\Users\\Vidyut Singhania\\Downloads\\New Business Cases\\twitter research")
