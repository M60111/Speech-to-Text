# Speech-to-Text
In order to train the code, the following five paragraphs were recorded in WAV format and accordingly the recorded voice from two developers; Braa and Mohamed; were pass to the code:

1.	“A massive coral reef garden the size of 60 football stadiums is to be created in the UAE - and is set to drive up eco tourism while safeguarding vital marine life.”

2.	“Work is under way on the Fujairah Cultured Coral Reef Gardens, the largest project of its kind in the country, which will include the cultivation of 1.5 million coral reef colonies over the next five years and will span 300,000 square metres, helping to provide a boost to food security efforts.”

3.	“The ambitious project was launched by the Ministry of Climate Change and Environment, in partnership with Fujairah Municipality, Dibba Fujairah Municipality and Fujairah Adventures and under the patronage of Sheikh Mohammed bin Hamad bin Mohammed Al Sharqi, Crown Prince of Fujairah, on Saturday.”

4.	“The preservation of the country’s biodiversity is also a prime area of focus for the UAE leadership today as outlined in the UAE Vision 2021. The Ministry of Climate Change and Environment has put in place multiple programs that aim to carry out the country’s national strategy for biodiversity in collaboration with other local environmental authorities in the country.”

5.	“ Ministry is keen on promoting the project as an ecotourism destination. It is also anticipated to encourage the spirit of volunteerism and community work as the cultivation of the coral reefs will depend heavily on the volunteering efforts of the youth.”

Reference: https://www.thenational.ae/uae/environment/major-coral-reef-garden-project-launched-in-fujairah-1.848464
Those recorded voices were saved and labels as following:
•	BTEST1.wav
•	BTEST2wav
•	BTEST3.wav
•	BTEST4.wav
•	BTEST5.wav
•	MTEST1.wav
•	MTEST2wav
•	MTEST3.wav
•	MTEST4.wav
•	MTEST5.wav
Where “B” stands for Person 1 (Braa), and “M” stands for Person 2 (Mohamed).

In the following detail description of application code:

1)	Training sound files were saved in AI_project folder, and tested files were saved in Test folder. Mkdir command was used to create a new folder and mv command used to move sound files to the relative correct folder. 


2)	Importing the required libraries. Firstly, Numpy library to handle and manipulate data. Then wave library to deal with sound files and convert them to data, then os library (operation system) to handle files and folders. Matplotlib library to show graphs and plot figures. Finally Wave file command to read the sound file and return the wave representation in time domain and the sample rate of the wave. Fft command to do Fast Fourier Transform and fftfreq to return Discrete Fourier Transform. 



3)	This code shows the loaddata function, as it reads each sound file and returns its Fourier Transform. This method was selected as that the sound print of each one is fixed and can be differentiated by training a model on Fourier Transform.   











4)	Creating empty lists for traindata and labels. The training files are listed in AI_project file. The listdir command will fetch all the files in this folder and save them in the variable (files). As shown in the output, there is unwanted file (checkpoint) and should be avoided in reading and appending to the training data.  

5)	To avoid fetching unwanted files, an IF loop was used to check the files before reading. This For loop will read the directory of each sound file and send it to the loaddata function, then FFT data will be returned and saved in data variable. Then The data file will be cropped to make sure that every file will have the same length. 


6)	This command will convert the lists to numpy arrays and do reshaping of the train label to fit in one column with multiple rows. 


7)	Checking that the train and label lists are in the correct shape before training the model.


8)	The Label column should be encoded to zero and one before do training, then reshape again to one column and multiple rows. 


9)	Using Logistic regression model to train the model and tune the parameters to find results with good prediction. 




10)	Train the model with train data and labels  

11)	Testing phase: This command will read the Test file and return FFT of the tested file. Then do cropping of the file and reshape with one row and multiple columns. Then pass to the prediction command.

12)	 Finally, inverting the predicted label to its original label. 



