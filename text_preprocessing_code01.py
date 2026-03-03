import marimo

__generated_with = "0.19.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    data = [
        "When life gives you lemons, make lemonade! 🙂",
        "She bought 2 lemons for $1 at Maven Market.",
        "A dozen lemons will make a gallon of lemonade. [AllRecipes]",
        "lemon, lemon, lemons, lemon, lemon, lemons",
        "He's running to the market to get a lemon — there's a great sale today.",
        "Does Maven Market carry Eureka lemons or Meyer lemons?",
        "An Arnold Palmer is half lemonade, half iced tea. [Wikipedia]",
        "iced tea is my favorite"
    ]
    return (data,)


@app.cell
def _(data):
    data
    return


@app.cell
def _(pd):
    pd.set_option('display.max_colwidth', None)
    return


@app.cell
def _(data, pd):
    data_df = pd.DataFrame(data, columns=["sentence"])
    return (data_df,)


@app.cell
def _(data_df):
    data_df
    return


@app.cell
def _(pd):
    test = [
        "We're going to start this course with traditional NLP applications.",
        "Then we'll move on to modern NLP theory.",
        "Finally, we'll wrap things up with modern NLP applications."
    ]

    test_series = pd.Series(test)
    test_series
    return (test_series,)


@app.cell
def _():
    # Text preprocessing with Pandas
    return


@app.cell
def _(data_df):
    data_df
    return


@app.cell
def _(data_df):
    df = data_df.copy()
    df
    return (df,)


@app.cell
def _(df):
    # lowercase

    df['sentence_clean'] = df['sentence'].str.lower()
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # remove []
    df['sentence_clean'] = df['sentence_clean'].str.replace(r'\[.*?\]', '', regex=True)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # remove punctuation
    df['sentence_clean'] = df['sentence_clean'].str.replace(r'[^\w\s]', '', regex=True)
    #df['sentence_clean'] = df['sentence_clean'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    df
    return


@app.cell
def _():
    # little tip for the function to do all the previous
    return


@app.cell
def _():
    return


@app.function
def lower_replace(series):
    output = series.str.lower()
    output = output.str.replace(r'\[.*?\]', '', regex=True)
    output = output.str.replace(r'[^\w\s]', '', regex=True)
    return output


@app.cell
def _(test_series):
    test_series
    return


@app.cell
def _(test_series):
    lower_replace(test_series)
    return


@app.cell
def _(df):
    lower_replace(df.sentence)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Text Preprocessing with spaCy
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    # do text preprocessing with spacy
    import spacy
    nlp = spacy.load('en_core_web_sm')
    return (nlp,)


@app.cell
def _():
    # pip install spacy
    return


@app.cell
def _():
    phrase = "im selling lemons for $5 today"
    phrase
    return (phrase,)


@app.cell
def _(nlp, phrase):
    doc = nlp(phrase)
    doc
    return (doc,)


@app.cell
def _():
    # Tokenizationa
    return


@app.cell
def _(doc):
    # break up the text into tokens

    [token.text for token in doc]
    return


@app.cell
def _(doc):
    # Lemmatization

    [token.lemma_ for token in doc]
    return


@app.cell
def _(doc):
    # Stop Words

    norm = [token.lemma_ for token in doc if not token.is_stop]
    norm
    return


@app.cell
def _(doc):
    # PARTS OF SPEECH TAGGING

    pos = [(token.text, token.pos_) for token in doc]
    pos
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    phrase_02 = df.sentence_clean[0]
    phrase_02
    return (phrase_02,)


@app.cell
def _(nlp, phrase_02):
    doc_02 = nlp(phrase_02)
    doc_02
    return (doc_02,)


@app.cell
def _(doc_02):
    # tokenize
    [token.text for token in doc_02]
    return


@app.cell
def _(doc_02):
    # lemmatize
    [token.lemma_ for token in doc_02]
    return


@app.cell
def _(nlp):
    # stop words
    list(nlp.Defaults.stop_words)[:10]
    return


@app.cell
def _(phrase_02):
    # stop words
    [token.lemma_ for token in phrase_02 if not token.is_stop]
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
