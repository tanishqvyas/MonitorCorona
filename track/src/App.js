import React from 'react';

import { Cards, Chart, CountryPicker, } from './components'
import styles from './App.module.css';
import { fetchData } from './api';

import MapChart from "./MapChart";
import Tablee from './Tablee'

class App extends React.Component{

    state = {
        data: {},
        country: '',
    }



    async componentDidMount() {
        const fetchedData = await fetchData(); 

        this.setState({ data: fetchedData });

    }


    handleCountryChange = async (country) => {
        // fetch data
        const fetchedData = await fetchData(country); 

        // set state
        this.setState({ data: fetchedData, country: country});

    }




    render(){

        const { data, country } = this.state;



        return (
            <div className={styles.container}>

                <div className={styles.navbar}>
                        {/* <a className={styles.link} href="http://127.0.0.1:7000/">
                        <span className={styles.navele}>
                            Home
                        </span>
                        </a> */}
                        
                        <a className={styles.link} href="http://localhost:3000/">
                        <span className={styles.navele}>
                            Home
                        </span>
                        </a>
                        
                        <a className={styles.link} href="http://127.0.0.1:8000/subscribe">
                        <span className={styles.navele}>
                            Subscribe
                        </span>
                        
                        </a>
                        <a className={styles.link} href="http://127.0.0.1:8000/unsubscribe">
                        <span className={styles.navele}>
                            Unsubscribe
                        </span>
                        </a>

                        <a className={styles.link} href="http://127.0.0.1:8000/about">
                        <span className={styles.navele}>
                            About
                        </span>
                        </a>

                </div>


                <Tablee />
                <CountryPicker handleCountryChange={this.handleCountryChange} />
                <Cards data={data} />
                <Chart data={data} country={country} />
                <h2>Relative World Choropleth Map for Covid-19 Disease Spread</h2>
                <div className={styles.legendbox}>
                    <div className={styles.legend}>
                        <div className={styles.extreme}></div>
                        <h4>Extreme</h4>
                    </div>

                    <div className={styles.legend}>
                        <div className={styles.mild}></div>
                        <h4>Very Mild</h4>
                    </div>

                    <div className={styles.legend}>
                        <div className={styles.nodata}></div>
                        <h4>No Data</h4>
                    </div>

                </div>
                <MapChart />

            </div>
        )

    }
}

export default App;