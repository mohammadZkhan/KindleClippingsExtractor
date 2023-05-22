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
  - [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

![Kindle2Notion Demo][product-demo]

A Python package to export all the clippings from your Kindle device to a page in Notion. Run this script whenever you plug in your Kindle device to your PC.

A key inspiration behind this project was the notes saving feature on Google Play Books, which automatically syncs all your highlights from a book hosted on the service to a Google Doc in real time. I wanted a similar feature for my Kindle and this project is one step towards a solution for this problem.

**Intended for**
- Avid readers who would want to browse through their prior reads and highlights anytime anywhere.
- For those who like to take notes alongside their highlights.


<!-- GETTING STARTED -->
## Getting Started


> **NOTE**
> Need a step-by-step guide to setting this package up? Click [here](https://kindle2notion.notion.site/Kindle2Notion-8a9683c9b19546c3b1cf42a68aceebee) for the full guide. 

To get a local copy up and running follow these simple steps:

### Prerequisites

* A Kindle device.
* A Notion account to store your links.
* Python 3 on your system to run the code.

### Installation & Setup

> **NOTE** 
> As of 10-07-2022, the latest update to this package relies on the offical Notion API for sending API requests. This requires you to create an integration token from [here](https://www.notion.so/my-integrations). For old users, you'd have to switch to this method as well since `notion-py` isn't being maintained anymore.
 
1. Install the library.
    ```sh
    pip install kindle2notion
    ```
2. Create an integration on Notion.
      1. Duplicate this [database template](https://kindle2notion.notion.site/6d26062e3bb04dd89b988806978c1fe7?v=0d394a8162cc481280966b35a37465c2) to your the workspace you want to use for storing your Kindle clippings.
      2. Open _Settings & Members_ from the left navigation bar.
      3. Select the _Integrations_ option listed under _Workspaces_ in the settings modal.
      4. Click on _Develop your own integrations_ to redirect to the integrations page.
      5. On the integrations page, select the _New integration_ option and enter the name of the integration and the workspace you want to use it with. Hit submit and your internal integration token will be generated.
3. Go back to your database page and click on the _Share_ button on the top right corner. Use the selector to find your integration by its name and then click _Invite_. Your integration now has the requested permissions on the new database. 


<!-- USAGE EXAMPLES -->
## Usage

1. Plug in your Kindle device to your PC.
    
2. You need the following three arguments in hand before running the code:
   1. Take `your_notion_auth_token` from the secret key bearer token provided.
   2. Find `your_notion_database_id` from the URL of the database you have copied to your workspace. For reference,
      ```
      https://www.notion.so/myworkspace/a8aec43384f447ed84390e8e42c2e089?v=...
                                        |--------- Database ID --------|
      ```
   3. `your_kindle_clippings_file` is the path to your `My Clippings File.txt` on your Kindle.

3. Additionally, you may modify some default parameters of the command-line with the following options of the CLI:
   - ```--enable_highlight_date```  Set to False if you don't want to see the "Date Added" information in Notion.
   - ```--enable_book_cover```      Set to False if you don't want to store the book cover in Notion.
    
4. Export your Kindle highlights and notes to Notion!
   - On MacOS and UNIX,
   ```sh
   kindle2notion 'your_notion_auth_token' 'your_notion_table_id' 'your_kindle_clippings_file'
   ```
   - On Windows
   ```sh
   python -m kindle2notion 'your_notion_auth_token' 'your_notion_table_id' 'your_kindle_clippings_file'
   ```
You may also avail help with the following command:
   ```sh
   kindle2notion --help
   python -m kindle2notion --help
   ```

> **NOTE**
> This code has been tested on a 4th Gen Kindle Paperwhite on both MacOS and Windows.



<!-- CONTRIBUTING -->
## Contributing
The people who contribute will be honored here.

<!-- Contributions. -->
Would **love it** it if you contribute to make this project better.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some New Feature (describe it out)'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/mohammadZkhan/KindleClippingsExtractor/blob/main/LICENSE) for more information.



<!-- CONTACT -->
## Contact

Mohammad Zainullah KHan ([My Website](https://www.zainullah.com) | [Email](mailto:mohammad.zainullah.khan@gmail.com) | [LinkedIn](https://www.linkedin.com/in/mohammad-zainullah-khan/))
