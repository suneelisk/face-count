txt <- "He served both as Attorney General and Lord Chancellor of England. After his death, he remained extremely influential through his works, especially as philosophical advocate and practitioner of the scientific method during the scientific revolution. Bacon has been called the father of empiricism.[6] His works argued for the possibility of scientific knowledge based only upon inductive and careful observation of events in nature. Most importantly, he argued this could be achieved by use of a skeptical and methodical approach whereby scientists aim to avoid misleading themselves. While his own practical ideas about such a method, the Baconian method, did not have a long lasting influence, the general idea of the importance and possibility of a skeptical methodology makes Bacon the father of scientific method. This marked a new turn in the rhetorical and theoretical framework for science, the practical details of which are still central in debates about science and methodology today. Bacon was knighted in 1603 and created Baron Verulam in 1618[4] and Viscount St. Alban in 1621;[3][b] as he died without heirs, both titles became extinct upon his death. Bacon died of pneumonia in 1626, with one account by John Aubrey stating he contracted the condition while studying the effects of freezing on the preservation of meat."
stringr::str_extract(txt, "([^\\s]+\\s){3}Verulam(\\s[^\\s]+){3}")
stringr::str_extract(txt, "(?:[^\\s]+\\s){3}Verulam(?:\\s[^\\s]+){3}")

#install.packages("devtools")
library("devtools")
#devtools::install_github("cloudyr/RoogleVision")
library(RoogleVision)
#BiocManager::install("EBImage")
library(EBImage)

id="1049450539767-1ht9e2epl8unh0dr133qs010flurbhlm.apps.googleusercontent.com"
secret="xIk8p9RQc_z8aE54o3_m1xEZ"

options("googleAuthR.client_id" = id)
options("googleAuthR.client_secret" = secret)
options("googleAuthR.scopes.selected" = c("https://www.googleapis.com/auth/cloud-platform"))
googleAuthR::gar_auth("F:\\karthick\\scanned pdf\\httr-oauth")

pic <- readImage('F:\\suneel\\face count\\image_data\\10006.jpg')
plot(pic)

us_hats = getGoogleVisionResponse('F:\\suneel\\face count\\image_data\\10006.jpg',
                                  feature = 'FACE_DETECTION')
#head(us_hats)
for(i in 1:length(us_hats$boundingPoly$vertices)){
  a = us_hats$boundingPoly$vertices[[i]]$x
  b = us_hats$boundingPoly$vertices[[i]]$y
  polygon(x=a, y=b, border = "red", lwd=5)}
