import optparse
import requests
from openai import OpenAI

class YouComOSINT:
    def __init__(self, api_key, chatgpt_key=None):
        self.api_key = api_key
        self.base_url = "https://api.ydc-index.io/search"
        if chatgpt_key:
            self.openai = OpenAI(api_key=chatgpt_key)

    def search(self, query):
        headers = {"X-API-Key": self.api_key}
        params = {"query": query}
        response = requests.get(self.base_url, params=params, headers=headers)
        return response.json()

    def summarize(self, text):
        chat = self.openai.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": "You will summarize any text that the user sends to you make it informational its for an OSINT scan report"},
              {"role": "user", "content": text}
          ])
        return chat.choices[0].message.content

    def print_data(self, data, output_file=None, summarize=False):
        url_list = []
        output = []
        for hit in data['hits']:
            output.append(f"Title: {hit['title']}")
            output.append(f"Description: {hit['description']}")
            for snippet in hit['snippets']:
                output.append(f"Snippet: {snippet}")
            output.append(f"Url: {hit['url']}")
            output.append(f"Thumbnail Url: {hit['thumbnail_url']}")
            output.append("=====================")
            url_list.append(hit['url'])
        output.append("All URLs:")
        for url in url_list:
            output.append(url)

        if summarize and self.openai:
            for line in output:
                print(line)
            print("=====================\nLoading summary...")
            summary = self.summarize('\n'.join(output))
            output = [summary]

        if output_file:
            print("Outputting to ", output_file)
            with open(output_file, 'w') as f:
                for line in output:
                    f.write(line + '\n')
        else:
            for line in output:
                print(line)


def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Specify the target to search")
    parser.add_option("-k", "--key", dest="api_key", help="Specify the API key")
    parser.add_option("-o", "--output", dest="output_file", help="Specify the output file")
    parser.add_option("-s", "--summarize", action="store_true", dest="summarize", help="Enable summary mode")
    parser.add_option("-c", "--chatgpt", dest="chatgpt_key", help="Specify the ChatGPT API key")
    (options, args) = parser.parse_args()

    if not options.target or not options.api_key:
        parser.error("Both target and API key must be specified. Use --help for more information.")

    osint_tool = YouComOSINT(options.api_key, options.chatgpt_key)
    person_info = osint_tool.search(f'"{options.target}"')
    osint_tool.print_data(person_info, options.output_file, options.summarize)


if __name__ == "__main__":
    main()
