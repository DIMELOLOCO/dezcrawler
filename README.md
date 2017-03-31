**WORKING VIABLE PRODUCT**

Create a product that works first. Focus on adding features later.



**PLAN OF ACTION**

Capture data using web crawler

Organize captured data into database

Create Website to run Database publically.

Analyze Images with OpenCV

​	find in vs. out

​		find sky. output percentage of image

​	find material types

​		wood, water, tree. output percentage of image

Analyze Image Content: with OpenCV/DeepLearning

​	look into the artist that created autonomous car salt circle and use his double machine learning system

Save out database of analyzed images.



**PARTS OF WEBSITE**

Error Handling

Error Logging

Optimization



**PARTS OF THE WEBSITE**

.main-article-body - IMGS, SUMMARY, HEADER

.article-tags - Tags and HREFS

.related-in-article-wrapper



**JSON DATABASE FORMAT**

Hyperlink :{

​	Page Data: {

​		Page Title: string

​		Page Author: string

​		Page Date:  string

​		Page Text: Long String

​		}

​	Image: {

​		Image hyperlink: String

​		SRCset  hyperlinks: [string 0, string 1 ]

​		Image SRC

​		}

​	Project Credits: {

​		'Design Architect' : 'string'

​		Project Architect: string

​		Contractor: string

​		Structural Engineer: string

​		Mechanical and Electrical Engineers: string

​		Quantity Surveyor: string

​		Planning Consultant: string

​		Landscape Architect: string

​		Heritage Consultants: string

​		If not in list above add to this one: string

​			}

​	Image Content {

}



**Create a dictionary to collect the data above.**
​	Parse the website for all relevant information. Classify.

​	Only use projects that have an "architecture" tag.

​	Figure out how to parse "design" tag too.

​	and interiors tag.

​	Add parsed data to dictionary. Ensure that the dictionary can do this.

**Collect all text on page to dictionary.**
​	use bs4 to parse text.
​	write text to dictionary.
​	do for every page.

**Collect all file paths to images on page saves to dictionary.**
​	use bs4 to parse images and collect hrefs from img
​	write text to dictionary
