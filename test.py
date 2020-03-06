import json

def main():
    json_open = open('fwd_api_sample_exception.json', 'r')
    json_obj = json.load(json_open)
    print(json_obj['shipments_exceptions'][0]['HAWB'])

if __name__ == "__main__":
    main()
