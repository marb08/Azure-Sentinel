import json
import os.path
import base64

def main():
    creds = None
    if os.path.exists('token.json'):
                with open('token.json', 'rb') as token:
                    creds = json.load(token)
    if not creds:
        print("There is no token.json file in the current directory. Please check.")
        exit(0)
    print("\nCopy json encoded string and save it. Paste it during installation in 'GWorkspace Function App' field:\n\n{}\n".format(base64.b64encode(json.dumps(creds).encode())))
if __name__ == '__main__':
    main()