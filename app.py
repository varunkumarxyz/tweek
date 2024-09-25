from flask import Flask, request, render_template
import pandas as pd

class TweetAnalyzer:
    def __init__(self, file_path):
        """Initialize the TweetAnalyzer with the given TSV file."""
        self.tweets_df = pd.read_csv(file_path, sep='\t')
        self.tweets_df['created_at'] = pd.to_datetime(self.tweets_df['created_at'], utc=True)

    def query_tweets(self, term):
        """Query tweets containing the specified term."""
        filtered_tweets = self.tweets_df[self.tweets_df['text'].str.contains(term, case=False, na=False)]
        
        return {
            "daily_counts": self._get_daily_counts(filtered_tweets),
            "unique_users": self._get_unique_users(filtered_tweets),
            "average_likes": self._get_average_likes(filtered_tweets),
            "place_ids": self._get_place_ids(filtered_tweets),
            "times_of_day": self._get_times_of_day(filtered_tweets),
            "most_active_user": self._get_most_active_user(filtered_tweets),
        }

    def _get_daily_counts(self, filtered_tweets):
        return filtered_tweets['created_at'].dt.date.value_counts().to_dict()

    def _get_unique_users(self, filtered_tweets):
        return filtered_tweets['author_id'].nunique()

    def _get_average_likes(self, filtered_tweets):
        return filtered_tweets['like_count'].mean()

    def _get_place_ids(self, filtered_tweets):
        return filtered_tweets['place_id'].value_counts().to_dict()

    def _get_times_of_day(self, filtered_tweets):
        return filtered_tweets['created_at'].dt.hour.value_counts().to_dict()

    def _get_most_active_user(self, filtered_tweets):
        return filtered_tweets['author_id'].value_counts().idxmax()

# Initialize the Flask application
app = Flask(__name__)
analyzer = TweetAnalyzer('twitter_201904.tsv')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        term = request.form.get('term')
        if term:
            result = analyzer.query_tweets(term)
    return render_template('index.html', result=result)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
