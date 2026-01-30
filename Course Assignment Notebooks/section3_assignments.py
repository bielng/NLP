import marimo

__generated_with = "0.19.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Text Preprocessing Assignments
    """)
    return


@app.cell
def _():
    import pandas as pd
    df = pd.read_csv(r"C:\Users\TAJ\Desktop\NLP\Data\childrens_books.csv")
    return df, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Text Preprocessing with Pandas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. Read the _childrens_books.csv_ file into a Jupyter Notebook
    2. Within the Description column:
    * Make all the text lowercase
    * Remove all \xa0 characters
    * Remove all punctuation
    """)
    return


@app.cell
def _(df):
    df.head(5)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Description']
    return


@app.cell
def _(pd):
    pd.set_option('display.max_colwidth', None)
    return


@app.function
def lower_replace(series):
    output = series.str.lower()
    output = output.str.replace(r'\[.*?\]', '', regex=True)
    output = output.str.replace(r'[^\w\s]', '', regex=True)
    return series


@app.cell
def _(df):
    df['Description'] = lower_replace(df['Description'])
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Description'].iloc[0]
    return


@app.cell
def _(df):
    df['Description'] = df['Description'].str.replace('\xa0', '')
    df['Description'].iloc[0]
    return


@app.cell
def _(df):
    df['Description'].iloc[0]
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Text Preprocessing with spaCy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In addition to the lowercasing and special character removal from the previous assignment, within the cleaned Description column:
    * Tokenize the text
    * Lemmatize the text
    * Remove stop words
    """)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Count Vectorizer
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. Vectorize the cleaned and normalized text using Count Vectorizer with the default parameters
    2. Modify the Count Vectorizer parameters to reduce the number of columns:
    * Remove stop words
    * Set a minimum document frequency of 10%
    3. Use the updated Count Vectorizer to identify the:
    * Top 10 most common terms
    * Top 10 least common terms that appear in at least 10% of the documents
    4. Create a horizontal bar chart of the top 10 most common terms
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. TF-IDF Vectorizer
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. Vectorize the cleaned and normalized text using TF-IDF Vectorizer with the default parameters
    2. Modify the TF-IDF Vectorizer parameters to reduce the number of columns:
    * Remove stop words
    * Set a minimum document frequency of 10%
    * Set a maximum document frequency of 50%
    3. Using the updated TF-IDF Vectorizer, create a  horizontal bar chart of the top 10 most highly weighted terms
    4. Compare the Count Vectorizer bar chart from the previous assignment with the TF-IDF Vectorizer bar chart and note the differences in the top term lists
    """)
    return


if __name__ == "__main__":
    app.run()
