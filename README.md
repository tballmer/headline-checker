# headline-checker (also known as "relAIbility")
Tests the reliability of news headlines 

## Inspiration
- In the past, society has always been fed mislabeled information that they would interpret their own way. From political discussions to opposing viewpoints, misinformation has caused much harm in people's lives. But up until now, it has never been this detrimental. With the current pandemic, many people are being fed wrong information about COVID such as the fake cons of vaccines that cause them to not know how to prevent it from reaching their household, specifically their kids. Deaths and cases are at an all-time high, and something needs to be done! To solve this issue, we thought that an impactful way to help people know how to act against COVID and other fake news was to use a revolutionary NLP model to create a more revolutionary, and more accurate misinformation detector than ever before. 

## What it does
- Our application allows the user to type in a news/media headline from any source on the internet and gives an in-depth analysis of how reliable the information based on the headline is through complex graphical visualizations.

## How we built it
- With the use of OpenAI's newest GTP-3 API, we trained a finalized NLP model after 7 iterations through multiple sources of data, such as the LIAR data set (contains 12.8K human-labeled short statements from Polifact.com's API), in addition to Kaggle's fake news dataset. To do this exactly, we created a data formatter so the data from the datasets could comply with the GTP-3 API, and train it properly. After multiple runs, our finalized model contains a whopping F1 score of .93 (see Model_Test_Results.csv for proof).
- We then created a web application using Flask and connected it with the GTP-3 function, where the user could type in a news headline into a text-box and click a button, which would then pass the news headline as a parameter to the GTP-3 function, and thus return the reliability statistics of the headline.
- On submit, a pie chart visualization of the statistics is produced. This was created using the matplotlib library.

## Challenges we ran into
- In our first implementation, we attempted to link our GTP-3 API to React, where the reliability statistics from the python script would be sent to the front-end to be displayed on the website. We were originally trying to use React.js due to its immense visualization libraries such as Chart.js and Recharts. However, when trying to use Flask to send the information to the React.js file, we ran into a block due to the policy key by the network, thus causing us to transition to pure Flask.

## Accomplishments that we're proud of
- Being able to communicate the data from the GTP-3 NLP model to the front-end using Flask
- Visualizing that data using an analytical python library
- Creating a local environment variable to be able to fetch the new API key from OpenAI instead of manually inputting it each time
- Working together, and maximizing efficiency no matter what problem comes up (dividing and conquering)
## What we learned
- Working web frameworks (Flask, matplotlib, HTML, JS), data visualization, training large scale AI models, formatting huge datasets, and working with API's

## What's next for RelAIbility
- Adding more intuitive and analytical breakdowns of news source articles (more graphs, tracked data)
- Passing more datasets to minimize bias and train our model to increase the F1 score of .93
- implementing a more user-friendly interface to enhance the user's experience as much as possible
