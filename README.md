<!-- PROJECT OVERVIEW -->
<p align="center">
  <img width="500" src="https://github.com/mohammadZkhan/KindleClippingsExtractor/blob/main/Media/Header.png?raw=true">
</p>
<!-- <h1 align="center">KindleClippingsExtractor</h1> -->
<p align="center">
A simple to use python script to extract and organize all the highlights from 'My Clippings.txt' file.
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
   - [Usage](#usage)
   - [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This is probably the simplest to use python script which allows you to extract all your clippings (highlights) from the 'My Clippings.txt' file. 

It automatically extracts the highlights, sorts and organizes them into individual files (one per book) and gives you nice looking '.txt' files which you can then use as you wish. The best part is, you can extract highlights not only from the books that you have purchased from Amazon but from all the documents that you have upload and highlighted on your kindle.

<p align="center">
  <img width="500" src="https://github.com/mohammadZkhan/KindleClippingsExtractor/blob/main/Media/Kindle_Book_List.png">
</p>

PS: I use these extracts to share my highlights with the world in my [digital library](https://www.notion.so/zainkhan/ab388ee65fb140ad967a5013a9768354?v=afc3169f9e9e49b59d2357bd1a46aa54). You can do the same or simply use them to review what resonated with you while you were reading those books. 


**Who is this for?**
- Readers who would want to browse through their highlights to review the crux of the books
- You!

<!-- GETTING STARTED -->
## Getting Started

This program was made to be easy to use. Follow the these simple steps:

### Prerequisites

* A Kindle device.
* Python 3 on your system to run the code.

<!-- USAGE EXAMPLES -->
### Usage

1. Clone this repository or simply download the files as `.zip`

2. Plug in your Kindle device to your PC. Navigate to the `documents` folder on your Kindle and copy `My Clippings.txt` file to the directory where you downloaded this repo (it must be in the same folder).

3. Execute `kinhigh.py` :
   ```
      $ python kinhigh.py
   ```
   or
   ```
      $ ./kinhigh.py
   ```


**You are all done. Simple, right?** <br>
If it was a success, you will see the following message:<br>
   > If you are seeing this message, everything has been done SUCCESSFULLY


 *Before this message, you will also see:* <br>
   (a) A message confirming that `My Clippings.txt` was found inside the directory (folder). The message will be `My clippings.txt' file has been loaded...`<br>
   (b) The list of all the books that have been found within your `My Clippings.txt` file. This will include any book on your kindle for which you have done atleast one highlight.<br>
   (c) The list of books for which highlights have been extracted and sorted into individual `.txt` files.<br>

 You will find the extracted highlights in a newly created folder `KindleBooks` within the same directory.
<p align="center">
  <img width="700" src="https://github.com/mohammadZkhan/KindleClippingsExtractor/blob/main/Media/Highlight%20files.gif">
</p>

### Notes
- To avoid books which just have a few highlights from having their own `.txt` file, there is a variable `minHighlights` which is set at `2` by default. This means that any book which has `2` or more highlights will have its own `.txt` file generated. You are free to change this value to whatever you choose to.
- Sometimes when highlighting on Kindle, one isn't able to highlight the required text accurately. So, one deletes (undo) it and highlights again. However, within the `My Clippings.txt` file, it doesn't get deleted or overwritten. The good news is that this program avoids these duplicate highlights from appearing in the final result.
- You can run this program again and again as you read more books and your `My Clippings.txt` file gets updated. It will create new files for each new book. 

<!-- CONTRIBUTING -->
## Contributing
*The people who contribute will be honored here.*

<!-- Contributions. -->
Would **love it** if you can contribute to make this project better.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some New Feature (describe it out)'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## Licenses

Distributed under the MIT License. See [LICENSE](https://github.com/mohammadZkhan/KindleClippingsExtractor/blob/main/LICENSE) for more information.



<!-- CONTACT -->
## Contact

Mohammad Zainullah Khan ([My Website](https://www.zainullah.com) | [Email](mailto:mohammad.zainullah.khan@gmail.com) | [LinkedIn](https://www.linkedin.com/in/mohammad-zainullah-khan/))
