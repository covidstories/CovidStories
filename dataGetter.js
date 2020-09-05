const getCovidStats = async() => {
    try {
    const response = await fetch('https://covidtracking.com/api/us');
    const usa = await response.json();
    covid19 = usa[0];
    }
    catch (err) {
    console.log(`Error: ${err}`);
    }
    finally {
    markup = `
                Current Tests:          ${covid19['totalTestResults']}
                Tested Positive:       ${covid19['positive']}
                Tested Negative:       ${covid19['negative']}
                Hospitalized:   ${covid19['hospitalized']}
                Recovered: ${covid19['recovered']}`
    document.getElementById('data').innerText = markup;
    }
    };
    getCovidStats();
    