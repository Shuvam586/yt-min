from youtubesearchpython import VideosSearch
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
searchResults = []

def lookupYT(query):
    videos_search = VideosSearch(query, limit = 4)
    results = videos_search.result()
    search_results = []
    for video in results['result']:
        title = video['title']
        link = video['link']
        vidId = video['link'].replace('https://www.youtube.com/watch?v=', '')
        search_results.append({'title': title, 'link': link, 'vidId':vidId})
    global searchResults
    searchResults = search_results

def lookupVID(query):
    videos_search = VideosSearch(query, limit = 1)
    results = videos_search.result()
    search_results = []
    for video in results['result']:
        title = video['title']
        link = video['link']
        vidId = video['link'].replace('https://www.youtube.com/watch?v=', '')
        search_results.append({'title': title, 'link': link, 'vidId':vidId})
    
    return search_results

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        query = request.form['yoo']
        lookupYT(query)
        print(searchResults)
        return redirect(url_for('results'))

    return render_template('home.html')

@app.route('/results')
def results():

    r1, r2, r3, r4 = searchResults

    return render_template('results.html', r1=r1, r2=r2, r3=r3, r4=r4)

@app.route('/view/<ytid>')
def view(ytid):

    print(lookupVID(ytid))

    return render_template('view.html', vid=ytid, title=lookupVID(ytid)[0]['title'])

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
