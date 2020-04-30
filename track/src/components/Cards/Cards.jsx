import React from 'react';
import CountUp from 'react-countup';

// import { Card, CardContent, Typography, Grid } from '@material-ui/core';

import styles from './Cards.module.css';


const Cards = ({ data: {confirmed , recovered, deaths, lastUpdate } }) => {

    if (!confirmed)
    {
        return 'Loading The Website...';
    }


    return(
        
    // <div className={styles.container}>
    //     <Grid container spacing={3} justify="center" >
    //         <Grid item component={Card}>
    //             <CardContent>
    //                 <Typography color="textSecondary" gutterBottom>Infected</Typography>
    //                 <Typography varaint="h5">Real DATA</Typography>
    //                 <Typography color="textSecondary">Real Date</Typography>
    //                 <Typography varaint="body2">Num cases</Typography>
    //             </CardContent>
    //         </Grid>
    //     </Grid>
    // </div>

    <div className={styles.container}  >
            <div className={styles.mycard} id={styles.infected}>
                <h1>Infected</h1>
                
                <CountUp 
                    start={0}
                    end={confirmed.value}
                    duration={2}
                    separator=","

                />


                <h3> {new Date(lastUpdate).toDateString()} </h3>
                <p>Active Number of Cases of Covid-19</p>
            </div>

            <div className={styles.mycard} id={styles.recovered}>
                <h1>Recovered</h1>
                <CountUp 
                    start={0}
                    end={recovered.value}
                    duration={2}
                    separator=","

                />
                <h3> {new Date(lastUpdate).toDateString()} </h3>
                <p>Recovered Number of Cases of Covid-19</p>
            </div>

            <div className={styles.mycard} id={styles.deaths}>
                <h1>Deaths</h1>
                <CountUp 
                    start={0}
                    end={deaths.value}
                    duration={2}
                    separator=","

                />
                <h3> {new Date(lastUpdate).toDateString()} </h3>
                <p>Total Death Toll because of Covid-19</p>
            </div>
    </div>



    )
}

export default Cards;