// ==UserScript==
// @name          IMDB info + .torrent from magnet
// @version       2.20190525
// @description   Show info of movies/series's (rating, poster, actors, ...) from IMDB on almost any torrent domain (thepiratebay, *torrent* , ...) as well as showing .torrent download links from any magnet:?url
// @namespace     hossam6236
// @author        hossam6236
// @license       GPL-3.0-or-later
// @include       http*://*torrent*.*/*
// @include       http*://*piratebay*.*/*
// @include       http*://*isohunt*.*/*
// @include       http*://*1337x*.*/*
// @include       http*://*rarbg*.*/*
// @include       http*://*zooqle*.*/*
// @include       http*://*bitsnoop*.*/*
// @include       http*://*dnoid*.*/*
// @include       http*://*torlock*.*/*
// @include       http*://*eztv*.*/*
// @include       http*://*idope*.*/*
// @include       http*://*toorgle*.*/*
// @include       http*://*demonoid*.*/*
// @include       http*://*kickass*.*/*
// @include       http*://*kat*.*/*
// @include       http*://*boxofficemojo*.*/*
// @include       http*://*.imdb.*/*
// @grant         GM_xmlhttpRequest
// @connect       imdb.com
// @connect       omdbapi.com
// @connect       media-amazon.com
// ==/UserScript==

// Find at:
// https://greasyfork.org/en/scripts/16946-imdb-info-torrent-from-magnet
// https://openuserjs.org/scripts/hossam6236/IMDB_info_%2B_.torrent_from_magnet

((document, hostname) => {
    const styleNode = document.createElement('style');
    styleNode.type = 'text/css';
    styleNode.textContent = `
        .imdb-download-link::before {
            content: '⇩';
        }
        .title_wrapper .imdb-download-link {
            font-size: .5em;
        }
        a.movie-preview {
            display: inline-block !important;
        }
        .movie-preview-starter {
            display: inline-block;
            position: fixed;
            opacity: 0.85;
            top: 0;
            right: 0;
            z-index: 10000;
            text-align: center;
        }
        .movie-preview-starter--button {
            display: inline-block;
            cursor: pointer;
            margin: 7px;
            padding: 7px;
            font-size: 12pt;
            font-family: Tahoma, Arial;
            border-radius: 5px;
        }
        .movie-preview-box {
            position: fixed;
            z-index:9999;
            width:475px;
            height:283px;
            top: calc(50vh - 150px);
            left: 50vw;
            display: flex;
            color: #000;
            background-color: white;
            border: 3px solid #222;
            border-radius: 5px;
            overflow: hidden;
            opacity: 0;
            visibility: hidden;
            transition: all 0.5s ease-in-out;
        }
        .movie-preview-box.visible {
            opacity: 1;
            visibility: visible;
        }
        .movie-preview-box *,
        .movie-preview-unique-list > * {
            font-size: 10pt;
            font-family: Tahoma, Arial;
            line-height: initial;
        }
        .movie-preview-box.no-trailer .preview--info--trailer {
            display: none;
        }
        .torrent-download-links {
            opacity: 0.8;
            font-size: 90%;
            position: absolute;
            display: none;
        }
        .assisted-torrent-link:hover .torrent-download-links {
            display: inline-block;
        }
        .movie-preview-unique-list {
            width: 50%;
            max-width: 400px;
            max-height: 200px;
            margin: auto;
            overflow: auto;
            text-align: left;
            padding: 5px;
            line-height: 15px;
            color: #000;
            background-color: white;
            border: 3px solid #222;
            border-radius: 5px;
        }
        .movie-preview-unique-list > * {
            margin: 2px;
        }
        .movie-preview-unique-list a {
            border: 0;
        }
        .movie-preview-unique-list a:hover {
            border: 0;
            text-decoration: underline;
        }
        a.movie-preview {
            cursor: pointer;
        }
        a.movie-preview.highlight {
            background-color: rgba(255, 231, 58, 0.59);
        }
        .movie-preview-enhancement {
            display: inline-block;
            max-width: 30px;
            min-width: 30px;
            font-size: 85%;
            margin:0 4px 0 0;
        }
        .movie-preview-enhancement.remarkable {
            font-weight: bold;
        }
        .preview--poster {
            flex-shrink: 0;
            width: 200px;
            height: 283px;
        }
        .preview--poster--img {
            cursor: pointer;
            width: 100%;
            height: 100%;
        }
        .preview--info {
            text-align:left;
            padding:3px;
            height:277px;
            overflow:auto;
            display:inline-block;
        }
        .preview--info--title {
            text-align:center;
            font-size:125%pt;
            font-weight:bold;
        }
        .preview--info--trailer {
            color: #369;
            cursor: pointer;
            display: inline-block;
        }
        .preview--info--trailer:hover {
            text-decoration: underline;
        }
        .preview--info--trailer::before {
            content: '(';
        }
        .preview--info--trailer::after {
            content: '), ';
        }
        .preview--info--imdb-rating,
        .preview--info--imdb-votes {
            font-weight: bold;
        }
    `;
    document.head.append(styleNode);

    if (hostname.endsWith('imdb.com')) {
        const movieTitleNodes = document.querySelectorAll('div.titleBar > div.title_wrapper > h1, td.titleColumn, div.lister-item-content .lister-item-header, div.title > a.title-grid, td.overview-top > h4 > a');
        for (let movieTitleNode of movieTitleNodes) {
            if (movieTitleNode.hasAttribute('with-download-link')) continue;
            movieTitleNode.setAttribute('with-download-link', true);

            let movieTitle = movieTitleNode.textContent;
            if (movieTitleNode.querySelector('.lister-item-index')) {
                let movieTitleNodeClone = movieTitleNode.cloneNode(true);
                movieTitleNodeClone.removeChild(movieTitleNodeClone.querySelector('.lister-item-index')).textContent;
            }
            movieTitle = movieTitle.replace(/\s+/g, " ").trim()

            const linkNode = document.createElement('a');
            linkNode.classList.add('imdb-download-link');
            linkNode.setAttribute('href', `https://thepiratebay.org/search/${encodeURIComponent(movieTitle)}/0/99/0`);

            movieTitleNode.append(linkNode);
        }
    } else {
        const starterNode = document.createElement('form');
        starterNode.classList.add('movie-preview-starter');
        starterNode.insertAdjacentHTML('beforeend', `
            <button class="movie-preview-starter--button"> load IMDb info </button>
        `);
        document.body.prepend(starterNode);

        starterNode.onsubmit = (e) => {
            e.preventDefault();
            starterNode.remove();

            const posterPlaceholder = 'http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB379391879_.png';
            const previewNode = document.createElement('div');
            previewNode.classList.add('movie-preview-box');
            previewNode.insertAdjacentHTML('beforeend', `
                <div class="preview--poster">
                    <img class="preview--poster--img" src="${posterPlaceholder}">
                </div>
                <div class="preview--info">
                    <div class="preview--info--title">
                        <a href="" target="_blank">
                            <span class="title">The Martian</span> (<span class="year">2015</span>)
                        </a>
                    </div>
                    <div class="preview--info--trailer" title="Play trailer" data-trailer-url="http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB379391879_.png">▶</div>
                    <span class="preview--info--imdb-rating">8.1</span><span style="color:grey;">/10</span> (<span class="preview--info--imdb-votes">275,300</span> votes), <span class="preview--info--imdb-metascore">-</span> Metascore
                    <br /><u>Awards</u>: <span class="preview--info--awards"></span>
                    <br /><u>Genre</u>: <span class="preview--info--genre">Adventure, Comedy, Drama</span>
                    <br /><u>Released</u>: <span class="preview--info--released">17 Oct 2017</span>
                    <br /><u>Box Office</u>: <span class="preview--info--boxofficegross">$123,456,789</span>
                    <br /><u>Rated</u>: <span class="preview--info--mpaa-rating">PG-13</span>, <u>Runtime</u>: <span class="preview--info--runtime">144 min</span>
                    <br /><u>Actors</u>: <span class="preview--info--actors">Matt Damon, Jessica Chastain, Kristen Wiig, Jeff Daniels</span>
                    <br /><u>Director</u>: <span class="preview--info--director">Ridley Scott</span>
                    <br /><u>Plot</u>: <span class="preview--info--plot">During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.</span>
                </div>
            `);

            previewNode.querySelector('.preview--poster--img').onclick = (e) => {
                e.preventDefault();
                const poster = e.currentTarget.src;
                if (poster === posterPlaceholder || !poster.startsWidth('http')) return;
                window.open(poster, '', 'width=600, height=600');
            };

            previewNode.querySelector('.preview--info--trailer').onclick = (e) => {
                e.preventDefault();
                window.open(e.currentTarget.getAttribute('data-trailer-url'), '', 'width=900, height=500');
            };

            previewNode.show = () => {
                previewNode.classList.add('visible');
                clearTimeout(previewNode.hiding);
            };

            previewNode.hide = () => {
                previewNode.hiding = setTimeout(
                    () => previewNode.classList.remove('visible'),
                    1500
                );
            };

            previewNode.onmouseover = previewNode.show;
            previewNode.onmouseout = () => {
                previewNode.hide();
            };

            previewNode.setMovie = movie => {
                previewNode.querySelector('.preview--info--title > a').setAttribute('href', `http://www.imdb.com/title/${movie.imdbID}`);
                previewNode.querySelector('.preview--info--title .title').textContent = movie.Title;
                previewNode.querySelector('.preview--info--title .year').textContent = movie.Year;

                const imageNode = previewNode.querySelector('.preview--poster--img');
                if (!movie.Poster) previewNode.classList.add('no-poster'); else previewNode.classList.remove('no-poster');
                imageNode.src = movie.Poster || posterPlaceholder;
                imageNode.onerror = (e) => {
                    if (!imageNode.src.startsWith('http')) return;
                    GM_xmlhttpRequest({
                        url: imageNode.src,
                        method: 'GET',
                        responseType: 'blob',
                        onload: (data) => {
                            const reader = new FileReader();
                            reader.onloadend = () => (imageNode.src = reader.result);
                            reader.readAsDataURL(data.response);
                        }
                    });
                };

                if (!movie.Trailer) previewNode.classList.add('no-trailer'); else previewNode.classList.remove('no-trailer');
                previewNode.querySelector('.preview--info--trailer').dataset.trailerUrl = movie.Trailer || '';

                previewNode.querySelector('.preview--info--imdb-rating').textContent = movie.imdbRating;
                previewNode.querySelector('.preview--info--imdb-votes').textContent = movie.imdbVotes;
                previewNode.querySelector('.preview--info--imdb-metascore').textContent = movie.Metascore;
                previewNode.querySelector('.preview--info--released').innerHTML = movie.Released;
                previewNode.querySelector('.preview--info--boxofficegross').innerHTML = movie.BoxOffice || 'N/A';
                previewNode.querySelector('.preview--info--genre').textContent = movie.Genre;
                previewNode.querySelector('.preview--info--mpaa-rating').textContent = movie.Rated;
                previewNode.querySelector('.preview--info--runtime').textContent = movie.Runtime;
                previewNode.querySelector('.preview--info--awards').innerHTML = movie.Awards
                    .replace('Oscars.', '<b>Oscars</b>.')
                    .replace('Oscar.', '<b>Oscar</b>.')
                    .replace('Another ', '<br />Another ');
                previewNode.querySelector('.preview--info--actors').textContent = movie.Actors;
                previewNode.querySelector('.preview--info--director').textContent = movie.Director;
                previewNode.querySelector('.preview--info--plot').textContent = movie.Plot;
            };

            const getMovieHashFromTitleAndYear = (title, year = '') => {
                return `${title}_${year}`.trim().replace(/[^a-zA-Z0-9]+/g, '-');
            };

            const getMovieTitleAndYearFromLinkNode = (linkNode) => {
                const linkText = linkNode.textContent;
                const linkHref = linkNode.getAttribute('href');
                const boxofficemojo = /^\/movies\/\?id=(.+)\.htm/i.exec(linkHref);
                let title = linkText.toLowerCase().replace(',', ' ').replace('.', ' ').replace('(', ' ').replace('1080p', '').replace('720p', '');
                let year = '';
                if (boxofficemojo) {
                    title = linkText.toLowerCase();
                    if (!year) {
                        year = /\(([0-9]{4}).*\)/.exec(title);
                        if (year) { // year from link text (if available)
                            title = title.replace(year[0], ' ').trim();
                            year = year[1];
                        } else {
                            year = /([0-9]{4})\.htm$/.exec(linkHref);
                            if (year && year[1] && year[1] > 1950) { // year from link href (if available)
                                year = year[1];
                            } else { // year from GET parameter (if available)
                                year = (new URL(window.location.href)).searchParams.get('yr');
                                if (!year) { // year is current year
                                    year = (new Date()).getFullYear();
                                }
                            }
                        }
                    }
                    return { title, year };
                } else {
                    const reM = /[0-9]{4}/i;
                    const reS = /S[0-9]{2}E[0-9]{2}|[0-9]{1}x[0-9]{2}/i;
                    let matchYear = reM.exec(title);
                    matchYear = matchYear && matchYear.length ? parseInt(matchYear[0]) : null;
                    const matchSeries = reS.exec(title);
                    if (matchYear > 1900) {
                        year = matchYear;
                        title = title.substr(0, title.search(reM)).trim();
                        return { title, year };
                    } else if (matchSeries) {
                        year = '-';
                        title = title.substr(0, title.search(reS)).trim();
                        return { title, year };
                    }
                }
                return { title: null, year: null };
            };

            const storage = localStorage.getItem('movie_preview');

            const fetchSafe = (url) => {
                return new Promise((resolve, reject) => {
                    GM_xmlhttpRequest({
                        url,
                        method: 'GET',
                        onload: (data) => {
                            resolve(data.responseText);
                        },
                        onerror: reject
                    });
                });
            };

            const loadMovie = (title, year) => {
                const url = `https://www.omdbapi.com/?apikey=c989d08d&t=${title}&y=${year}&plot=full&r=json`;
                // const url = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=' + encodeURIComponent(title + ' (' + year + ')');
                return fetchSafe(url)
                    .then(responseText => JSON.parse(responseText))
                    .then(movieResolvedData => {
                        return movieResolvedData;
                    });
            };

            const updateLinkNodesWithMovieData = (nodes, resolvedMovieData) => {
                for (let linkNode of nodes) {
                    if (resolvedMovieData.Error) continue;
                    linkNode.onmouseover = () => {
                        previewNode.setMovie(resolvedMovieData);
                        previewNode.show();
                    };
                    linkNode.onmouseout = () => {
                        previewNode.hide();
                    };
                    const enhancementNode = document.createElement('div');
                    enhancementNode.classList.add('movie-preview-enhancement');
                    linkNode.parentNode && linkNode.parentNode.insertBefore(enhancementNode, linkNode);

                    const awards_text = resolvedMovieData.Awards.toLowerCase(); //awards_text = awards_text ? awards_text : 'N/A';
                    const el_tip = `${resolvedMovieData.imdbVotes} votes - ${resolvedMovieData.Runtime} - Rated ${resolvedMovieData.Rated} - Awards: ${awards_text}`;
                    let star = '';
                    const reg_wins = /([0-9]+) win(s|)/;
                    const reg_noms = /([0-9]+) nomination(s|)/;
                    const reg_wins_sig = /Won ([0-9]+) Oscar(s|)/;
                    const reg_noms_sig = /Nominated for ([0-9]+) Oscar(s|)/;
                    let wins = reg_wins.exec(awards_text); if (wins) wins = parseFloat(wins[1]);
                    let noms = reg_noms.exec(awards_text); if (noms) noms = parseFloat(noms[1]);
                    let wins_sig = reg_wins_sig.exec(awards_text); if (wins_sig) wins_sig = parseFloat(wins_sig[1]);
                    let noms_sig = reg_noms_sig.exec(awards_text); if (noms_sig) noms_sig = parseFloat(noms_sig[1]);

                    const rating = parseFloat(resolvedMovieData.imdbRating);
                    const votes = parseFloat(resolvedMovieData.imdbVotes.replace(',', ''));
                    if (rating >= 7.0 && votes > 50000) {
                        enhancementNode.classList.add('remarkable');
                    }

                    if ((wins_sig >= 1 || noms_sig >= 2) && (wins >= 5 || noms >= 10)) {
                        star = '<span style="color:#DD0000">&#9733;</span>';
                    } else if (wins >= 10 || (noms_sig >= 1 && noms >= 5) || (rating > 8.0 && votes > 50000)) {
                        star = '<span style="color:#660000">&#9733;</span>';
                    } else if (wins >= 5 || noms >= 10 || noms_sig >= 1 || votes > 150000) {
                        star = '&#9733;';
                    } else if (wins + noms > 1) {
                        star = '&#9734;';
                    }

                    enhancementNode.innerHTML = `<a href="http://www.imdb.com/title/${resolvedMovieData.imdbID}" target="_blank" title="${el_tip}">${resolvedMovieData.imdbRating}${star}</a>`;
                    let opacity = 1.0;
                    if (rating <= 5.0 || votes <= 1000) {
                        opacity = Math.max(0.15, Math.min(rating / 10, votes / 1000));
                    } else if (resolvedMovieData.imdbRating == "N/A" || resolvedMovieData.imdbVotes == "N/A") {
                        opacity = 0.15;
                    }
                    enhancementNode.style.opacity = opacity;
                }
            };

            const createUniqueMovieList = (moviesDataMap) => {
                let wrapperNode = document.createElement('div');
                wrapperNode.classList.add('movie-preview-unique-list');
                for (let movieData of moviesDataMap.values()) {
                    let parentNode, linkNode;
                    parentNode = document.createElement('div');
                    linkNode = document.createElement('a');
                    linkNode.textContent = movieData.hash;
                    linkNode.classList.add('movie-preview');
                    linkNode.dataset.movieHash = movieData.hash;
                    linkNode.onclick = () => {
                        for (let movPreview of document.querySelectorAll('.movie-preview')) {
                            movPreview.classList.remove('highlight');
                        }
                        for (let movPreview of document.querySelectorAll(`.movie-preview[data-movie-hash="${movieData.hash}"]`)) {
                            movPreview.classList.add('highlight');
                        }
                    };
                    movieData.promise.then(resolvedData => {
                        if (resolvedData.Title) {
                            linkNode.textContent = `${resolvedData.Title} (${resolvedData.Year})`;
                        }
                    });
                    wrapperNode.appendChild(parentNode);
                    parentNode.appendChild(linkNode);
                }
                return wrapperNode;
            };

            const moviesDataMap = new Map();

            for (let linkNode of document.querySelectorAll('a')) {
                const href = linkNode.getAttribute('href');
                const torrentz = /^\/([a-zA-Z0-9]{40})/i.exec(href);
                const piratebay = /^\/torrent\/([0-9])/i.exec(href);
                const hashMatch = /(^\/|^magnet\:\?xt\=urn\:btih\:)([a-zA-Z0-9]{40})/i.exec(href);

                const cleanupPorn = (node) => {
                    const innerHTML = node.innerHTML.toLowerCase();
                    if (innerHTML.includes('xxx') || innerHTML.includes('porn')) node.outerHTML = '';
                };
                cleanupPorn(linkNode);

                const linkText = linkNode.textContent;
                if (hashMatch) {
                    const hash = hashMatch[2].toUpperCase();
                    /////////////////////////////////////////////////////// Loading Magnet from piratebay
                    const assistingNode = document.createElement('div');
                    assistingNode.classList.add('torrent-download-links');
                    assistingNode.insertAdjacentHTML('beforeend', `
                        <a target="_blank" href="http://torrage.info/torrent.php?h=${hash}"         style="display: inline-block; padding:0 5px 0 5px; background-color:#748DAB; text-align:center;">t1</a>
                        <a target="_blank" href="http://www.btcache.me/torrent/${hash}"             style="display: inline-block; padding:0 5px 0 5px; background-color:#748DAB; text-align:center;">t1</a>
                        <a target="_blank" href="http://torrentproject.se/torrent/${hash}.torrent"  style="display: inline-block; padding:0 5px 0 5px; background-color:#748DAB; text-align:center;">m</a>
                    `);
                    linkNode.parentNode && linkNode.parentNode.classList.add('assisted-torrent-link');
                    linkNode.parentNode && linkNode.parentNode.append(assistingNode);
                }

                let { title, year } = getMovieTitleAndYearFromLinkNode(linkNode);

                if (title && year) {
                    const movieHash = getMovieHashFromTitleAndYear(title, year);
                    linkNode.classList.add('movie-preview');
                    linkNode.dataset.movieHash = movieHash;
                    linkNode.style.display = (linkNode.style.display === 'block') ? 'inline-block' : linkNode.style.display;
                    if (!moviesDataMap.has(movieHash)) {
                        moviesDataMap.set(
                            movieHash,
                            {
                                title,
                                year,
                                hash: movieHash,
                                promise: loadMovie(title, year)
                            }
                        );
                    }
                }
            }

            console.log(moviesDataMap);

            document.body.prepend(createUniqueMovieList(moviesDataMap));

            for (let movieData of moviesDataMap.values()) {
                movieData.promise.then(resolvedData => {
                    updateLinkNodesWithMovieData(
                        document.querySelectorAll(`.movie-preview[data-movie-hash="${movieData.hash}"]`),
                        resolvedData
                    );
                });
            }
            document.body.append(previewNode);
        };
    }

    if (hostname.endsWith('thepiratebay.org')) {
        document.querySelector('#main-content').style.marginLeft = 0
        document.querySelector('#main-content').style.marginRight = 0
    }

})(document, window.location.hostname);
