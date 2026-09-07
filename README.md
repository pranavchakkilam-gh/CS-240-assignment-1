# CS-240-assignment-1
Assignment 1 
       <h1> The Repository</h1>
	   <p>This repository consists of 4 assignments that consist of ASCII-to-decimal converter, a number converter supporting binary, decimal, octal, and hexadecimal, an image-to-text converter, and finally a text-to-image converter coded in Python.</p>
            <h2>Question 1, ASCII-to-decimal</h2>
            <p>This program converts the word "Cool" into decimal ASCII values. The string "Cool" is saved in a variable s and passed to the ord() function, which loops through the characters in the string. The ord() function converts each character into an ASCII decimal value. In this example, for "Cool". </p>
			C -> 67
			o -> 111
			o -> 111
			l -> 108
			<p>The output for the file looks like this</p>
            <p align="left">
            <img alt="output for the ASCII decimal value for the string cool." src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/3f75e3828bbeeda76e3eca20bf14dd5c3d782921/Screenshot%202026-09-06%20161301.png">
            </p>
            <h2>Question 2, Number-converter</h2>
            <p>This program accepts a number in binary, decimal, octal, or hexadecimal and displays that number in all four number systems. The program takes user input for the number. Python stores the input as text. Asks which number system the input uses. .lower() changes the answer to lowercase, so inputs like BINARY and Binary both become binary; this is to keep consistency throughout the code. The 2 tells Python that the number is binary. The 10 tells Python that it is decimal. The 8 tells Python that it is octal. The 16 tells Python that it is hexadecimal. Then it prints out the value for each form respectively</p>
			<p>The output for the file looks like this</p>
            <p align="left">
            <img alt="output for the number-base converter supporting binary, decimal, octal, and hexadecimal." src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/6f15b5fb52c8c77472d45626ec656dbce19aaa7c/Screenshot%202026-09-06%20170004.png">
            </p>
            <h2>Question 3, Image-to-text file</h2>
            <p>This program opens an image called Landscape.png using the Pillow library and converts it to RGB format. The convert() function takes the red, green, and blue values of each pixel and checks whether they match one of seven known colors. Each known color is represented by a letter, such as B for blue, G for green, and W for white. If a pixel does not match any known color, its full RGB value is returned. The two loops examine every pixel from left to right and top to bottom. The converted pixel values are then written into output.txt, with spaces between pixels and a new line after every image row. (Used AI to fix wording and grammar)</p>
			<p>The Landscape.png file looks like this</p>
            <p align="center">
            <img alt="Landscape image" src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/09b6c233b5854463a9fd628b73a3acb5bfcfa5e7/Screenshot%202026-09-06%20171326.png">
            </p>
			<p> (Image is scaled up 10 times for better visibility)</p>
			<p>The output for the file looks like this</p>
			 <p align="left">
            <img alt="Landscape image text" src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/7c13b14d17ebd815eabf042481420d08ec924919/Screenshot%202026-09-06%20171826.png">
            </p>
            <h2>Question 4, text-to-image file</h2>
            <p>This program reads a text file containing pixel codes and uses those codes to create an image. First, it imports the Image class from the Pillow library. The convert() function translates each pixel code into an RGB color value. The letter R represents red, B represents black, and Y represents yellow. Any unrecognized code is converted to white.

The program opens awesome_picture.txt and stores all its lines. It calculates the image’s height using the number of lines and its width using the number of pixel codes in the first line. It then creates a blank RGB image. The nested loops move through every row and column, convert each letter into a color, and place that color at the appropriate coordinate. Finally, the program saves the finished image as smiley2.png and displays it.</p>
			<p>The input text file looks like this. (Used AI to fix wording and grammar)</p>
			<p align="left">
            <img alt="smilly text file" src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/4122e78e0dbde2696c7b7d0a04c3002894addd9f/Screenshot%202026-09-06%20172357.png">
            </p>
			<p>The output image that gets generated looks like this</p>
			<p align="center">
            <img alt="smilly image" src="https://github.com/pranavchakkilam-gh/CS-240-assignment-1/blob/468f9f8e19ff2e1366fee95391b80b61034fed20/Screenshot%202026-09-06%20173011.png">
            </p>
			<p> (Image is scaled up 10 times for better visibility)</p>
    	 <h2>License</h2>	
        <p>Copyright (c) madeUpFake Corporation. All rights reserved.</p>
	<p>Licensed under the madeUpFake license.</p>	
    
  </main>
</body>

</html>
