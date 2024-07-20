import re
import pandas as pd
from collections import Counter
from urlextract import URLExtract
from wordcloud import WordCloud
import string
import emoji

extractor = URLExtract()


# analysis user selection option
def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    # for words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # removed the phrase media omitted
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # link extractor
    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    # print no. of link, media, messages, words shared
    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df_percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index() \
        .rename(columns={'index': 'name', 'user': 'percent'})

    return x, df_percent


def remove_stop_words(message):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read().split()

    filtered_words = [word for word in message.lower().split() if word not in stop_words]
    return " ".join(filtered_words)


def remove_punctuation(message):
    cleaned_message = re.sub('[%s]' % re.escape(string.punctuation), '', message)
    return cleaned_message


def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != '<Media omitted>\n']
    temp['message'] = temp['message'].apply(remove_punctuation)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] != 'group_notification']
        df = df[df['message'] != '<Media omitted>\n']

    df['message'] = df['message'].apply(remove_stop_words)
    df['message'] = df['message'].apply(remove_punctuation)

    words = []
    for message in df['message']:
        words.extend(message.split())

    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)

    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline= df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap
