import axios from 'axios';

const url = 'https://covid19.mathdro.id/api';


// Function to get data for the Number info pallets

export const fetchData = async (country) => {
    
    let changeableUrl = url;

    if(country)
    {
        changeableUrl = `${url}/countries/${country}`;
    }
    
    try {
        
        const { data: { confirmed, recovered, deaths, lastUpdate } } = await axios.get(changeableUrl);

        // If value and key have same name we can just write values
        const modifiedData = {
            confirmed: confirmed,
            recovered: recovered,
            deaths: deaths,
            lastUpdate: lastUpdate,
        }

        return modifiedData;
        

    } catch (error) {
        
    }
}



// Function for getting our time series chart shit

export const fetchDailyData = async () => {

    try {
        
        const { data } = await axios.get(`${url}/daily`);

        const modifiedData = data.map((dailyData) => ({
            confirmed: dailyData.confirmed.total,
            deaths: dailyData.deaths.total,
            date: dailyData.reportDate
        }));

        return modifiedData;

    } catch (error) {
        
    }

}


export const fetchCountries = async () => {

    try {

        const { data: { countries } } = await axios.get(`${url}/countries`);
        
        return countries.map((country) => country.name);

    } catch (error) {
        
    }

}