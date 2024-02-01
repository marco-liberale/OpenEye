# OpenEye
**Note: This tool is in pre-alpha, more updates will be coming soon.**
# Documentation

## Introduction
OpenEye is a powerful tool for Open Source Intelligence (OSINT) that allows you to search and summarize information about a specific target. It uses the OpenAI GPT-3 model for summarizing the search results.

## Installation
To install OpenEye, you need to have Python installed on your system. If you don't have Python installed, you can download it from the official Python website.

Once you have Python installed, follow these steps:

1. Clone the OpenEye repository to your local machine.
   ```
   git clone https://github.com/marco-liberale/OpenEye.git
   ```
2. Navigate to the directory containing the OpenEye files.
   ```
   cd OpenEye
   ```
3. Install the required Python packages using the following command:
   ```
   pip install -r requirements.txt
   ```

## Getting the API Keys
OpenEye requires two API keys to function:

- **You.com Websearch API Key**: This is used to search the web for you target. You can obtain this key by registering on the You.com Developers [website](https://api.you.com/).
- **OpenAI API Key**: This is used to access the GPT-3 model for summarizing the search results. You can obtain this key by registering on the OpenAI [website](https://platform.openai.com/).

## Usage
Once you have the API keys, you can use OpenEye by running the main Python script with the following command-line options:

- `-t` or `--target`: Specify the target to search.
- `-k` or `--key`: Specify the You.com Websearch API Key.
- `-o` or `--output`: Specify the output file. If not specified, the output will be printed to the console.
- `-s` or `--summarize`: Enable summary mode. This uses the GPT-4 model to summarize the search results. Note: if a Chatgpt API key is not specifed with `-c` this will be ignored 
- `-c` or `--chatgpt`: Specify the OpenAI API key.

Here is an example of how to use OpenEye:

```
python main.py -t "John Doe" -k "your_youdotcom_websearch_api_key" -c "your_openai_api_key" -s
```

This will search for "John Doe" using the specified You.com Index API key, summarize the results using the specified OpenAI API key, and print the summarized results to the console.

If you want to save the results to a file, you can use the `-o` option:

```
python main.py -t "John Doe" -k "your_youdotcom_websearch_api_key" -c "your_openai_api_key" -s -o "output.txt"
```



This will save the summarized results to "output.txt".

Please note that both the target and the You.com Websearch API Key must be specified. If they are not, OpenEye will display an error message and exit.

## Legal Disclamer
By using the repository, you acknowledge that you have read this [Disclaimer](https://github.com/marco-liberale/OpenEye/blob/main/legal_disclamer.pdf) and agree to be bound by the terms hereof.
If you do not agree to abide by the above, please do not use the repository.

Enjoy :)
