import twitter
import argparse

# Set up authentication
api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                  access_token_key='access_token_key',
                  access_token_secret='access_token_secret')

def get_stock_tweets(symbol):
    # Search for tweets containing the stock symbol
    query = api.GetSearch(term=symbol, count=10, result_type='recent')
    # Extract the text of each tweet and return as a list
    return [tweet.text for tweet in query]

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--twitter', help='Get latest feedback on stock', action='store_true')
    parser.add_argument('symbol', help='Stock symbol to search for')
    args = parser.parse_args()

    if args.twitter:
        tweets = get_stock_tweets(args.symbol)
        print('\n'.join(tweets))
