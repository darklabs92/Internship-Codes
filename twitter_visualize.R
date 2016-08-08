# import the twitteR library for use
if(!require(twitteR)) {
  install.packages("twitteR"); require(twitteR)}
if(!require(wordcloud)) {
  install.packages("wordcloud"); require(wordcloud)}
if(!require(igraph)) {
  install.packages("igraph"); require(igraph)}
if(!require(tm)) {
  install.packages("tm"); require(tm)}

# set the authentication keys of 4 different apps for usage
ckey <- c("","","","")
csecret <- c("","","","")
atoken <- c("","","","")
asecret <- c("","","","")


dat <- read.csv("C:\\Users\\Vidyut Singhania\\Downloads\\New_Business_Cases\\twitter_research\\TwitterUsers.csv", header = TRUE, stringsAsFactors = FALSE)

speakr<- unique(dat$Voice.Name)
speakr1<-speakr[45]
o<-speakr[1]
m=0
p<- 12
rm(finTime)
speakr<- speakr[30:length(speakr)]
finTime <- data.frame(stringsAsFactors = F)
while(length(unique(o))<100){
  if(m<4) {
    m<-m+1
  }
  else{
    m<-1
  }
  consumerKey <- ckey[m]
  consumerSecret <- csecret[m]
  access_token <- atoken[m]
  access_token_secret <- asecret[m]
  
  setup_twitter_oauth(consumerKey,consumerSecret,access_token,access_token_secret)
  
  #speakr1 <- speakr[p+length(unique(o))+1:p+length(unique(o))+30]
  nxt <-r<- 1
  for (i in nxt:length(speakr)){
    r <- r+1
    tweets <- try(userTimeline(speakr[i],n=3200,includeRts = TRUE),silent=TRUE)
    if(!(inherits(tweets ,'try-error'))){
      finTime <- rbind(finTime,twListToDF(tweets))  
    }
    nxt<- r
  }
  o<- unique(finTime$screenName)
}


write.csv(finTime,"C:\\Users\\Vidyut Singhania\\Downloads\\New_Business_Cases\\twitter_research\\Twitter\\list_post.csv")


#m<- finTime$text
#m1 <- finTime[finTime$screenName=="vsdaking",]
m1<- finTime
m<- m1$text
lo <- paste(m, collapse = "")
review_source <- VectorSource(lo)
corpus <- Corpus(review_source)
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
dtm <- DocumentTermMatrix(corpus)
dtm2 <- as.matrix(dtm)
frequency <- colSums(dtm2)
frequency <- sort(frequency, decreasing=TRUE)
words <- names(frequency)
wordcloud(words[1:100], frequency[1:100], colors = c("tomato", "wheat","lightblue"))
speakr1
#frequency[1:100]
write.csv(finTime,"C:\\Users\\Vidyut Singhania\\Downloads\\New_Business_Cases\\twitter_research\\newdata.csv")
